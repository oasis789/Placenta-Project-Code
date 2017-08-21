import LoadCode as lc
import generations as Gens
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def hierarchy_pos(G, root, width=8., vert_gap = .2, vert_loc = -0, xcenter = 0.5, 
                  pos = None, parent = None):
    '''If there is a cycle that is reachable from root, then this will see infinite recursion.
       G: the graph
       root: the root node of current branch
       width: horizontal space allocated for this branch - avoids overlap with other branches
       vert_gap: gap between levels of hierarchy
       vert_loc: vertical location of root
       xcenter: horizontal location of root
       pos: a dict saying where all nodes go if they have been assigned
       parent: parent of this branch.'''
    if pos == None:
        pos = {root:(xcenter,vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
    neighbors = G.neighbors(root)
    #if parent != None:
        #neighbors.remove(parent)
    if len(neighbors)!=0:
        dx = width/len(neighbors) 
        nextx = xcenter - width/2 - dx/2
        for neighbor in neighbors:
            nextx += dx
            pos = hierarchy_pos(G,neighbor, width = dx, vert_gap = vert_gap, 
                                vert_loc = vert_loc-vert_gap, xcenter=nextx, pos=pos, 
                                parent = root)

    return pos

def linear_equidistant_plot(G, root, dx_list=None,dy=0.2, xpos=0.5,ypos=0.,g=None,gen_list=None,pos=None,parent=None):
    '''Plots tree with homogenerational nodes spaced equidistantly apart from one another'''
    if pos == None:
        pos = {root:(xpos,ypos)}
        gen_list, g = Gens.get_generations(G,root)
        dx_list = np.zeros(len(gen_list.keys()))
        current_gen = 0

    else:
        pos[root] = (xpos, ypos)
        current_gen = g[root]

    neighbors = G.neighbors(root)
    #if parent != None:
     #   neighbors.remove(parent)

    if len(neighbors)!=0:
        for neighbor in neighbors:
            current_gen += 1
            no_of_nodes_in_current_gen = len(gen_list[current_gen])
            current_dx = 1./(no_of_nodes_in_current_gen+1)
            ypos = dy*(current_gen)
            xpos = current_dx+dx_list[current_gen]
            dx_list[current_gen] = xpos
            pos = linear_equidistant_plot(G,neighbor, dx_list=dx_list,dy=dy,xpos=xpos,ypos=ypos,g=g,gen_list=gen_list, pos=pos, 
                                parent = root)
            current_gen-=1

    return pos

def radial_equidistant_plot(G, root, dphi_list=None,dr=0.2, xpos=0.,ypos=0.,g=None,gen_list=None,pos=None,parent=None):
    '''Plots tree radially with homogenerational nodes radially spaced equidistantly apart from one another'''
    #Not working yet
    if pos == None:
        pos = {root:(xpos,ypos)}
        gen_list, g = Gens.get_generations(G,root)
        dphi_list = np.zeros(len(gen_list.keys()))
        current_gen = 0

    else:
        pos[root] = (xpos, ypos)
        current_gen = g[root]

    neighbors = G.neighbors(root)
    #if parent != None:
     #   neighbors.remove(parent)

    if len(neighbors)!=0:
        for neighbor in neighbors:
            current_gen += 1
            no_of_nodes_in_current_gen = len(gen_list[current_gen])
            #current_dx = 1./(no_of_nodes_in_current_gen+1)
            current_dphi = 2*np.pi/(no_of_nodes_in_current_gen)
            current_dphi += dphi_list[current_gen]
            ypos = dr*current_gen*np.sin(current_dphi)
            xpos = dr*current_gen*np.cos(current_dphi)
            dphi_list[current_gen] = current_dphi
            pos = radial_equidistant_plot(G,neighbor, dphi_list=dphi_list,dr=dr,xpos=xpos,ypos=ypos,g=g,gen_list=gen_list, pos=pos, 
                                parent = root)
            current_gen-=1

    return pos
    
    

def radial_plot(G,root,l=0.3,pos=None,parent=None,xpos=1.,ypos=0.5):
    if pos == None:
        pos = {root:(xpos,ypos)}
    else:
        pos[root] = (xpos,ypos)
        
    neighbors = G.neighbors(root)
    #print len(neighbors)
    yshift = 0

    #if parent != None:
     #   neighbors.remove(parent)
    if len(neighbors) != 0:
        print len(neighbors)
        angle = np.pi/(len(neighbors)+1)
        for neighbor in neighbors:
            nextx = xpos + l*np.cos(angle)
            nexty = ypos + l*np.sin(angle)
            angle += angle
            pos = radial_plot(G,neighbor,l,pos=pos,parent=root,xpos=nextx,ypos=nexty)
            yshift += 0.2

    return pos

def plot_with_graph_points(G,anetwork):
    '''Plot the tree using the coordinates supplied from dataset'''
    graph_points = anetwork.getGraphPoints()
    x_coords = graph_points[0]
    y_coords = graph_points[1]
    pos = {k : (x_coords[k-1],y_coords[k-1]) for k in G.nodes()}
    return pos
           
def plot_vascular_network(ID,isArtery=True):
    '''Plot a graphical representation of the tree network for a sepcified placenta
        ID: ID for the placenta
        isArtery: True to plot Artery Network, False to plot Vein Network'''
    plt.figure()
    placenta = lc.loadSinglePlacentafromdir(ID)
    if(isArtery):
        anetwork = placenta.getArteryNetwork()
    else:
        anetwork = placenta.getVeinNetwork()
    #allChildrenNodes = [b for a in anetwork.getChildren().values() for b in a] # Returns all children nodes in the network as a single list
    aG = nx.from_dict_of_lists(anetwork.getChildren())
    #pos=nx.graphviz_layout(aG,prog='twopi',args='')
    #plt.figure(figsize=(8,8))
    #nx.draw(aG,pos,node_size=20,alpha=0.5,node_color="blue", with_labels=False)
    #plt.axis('equal')
    #plt.savefig('circular_tree.png')
    #plt.show()
    pos = hierarchy_pos(aG,anetwork.getChildren().keys()[-1])#Root is key of last element in getChildren
    #pos = linear_equidistant_plot(aG,anetwork.getChildren().keys()[-1])
    #pos = radial_equidistant_plot(aG,anetwork.getChildren().keys()[-1])
   # pos = plot_with_graph_points(aG,anetwork)
    gen_list,gens = Gens.get_generations(aG,max(aG.nodes()))
    #nx.draw(aG, pos=pos,alpha=0.7,node_size=30,label=ID,style='dotted')
    nx.draw(aG,pos=pos,alpha=0.6,node_size=20)
    plt.show()

    
