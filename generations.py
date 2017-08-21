import numpy as np
import networkx as nx

def get_generation_dict(G,root,generations=None,parent=None,current_gen=0):
    '''Returns a dictionary with the nodes as keys and the values as the generation number for the node generations = {node:gen}'''
    if generations == None:
        generations = {root:current_gen}
    else:
        generations[root] = current_gen
    neighs = G.neighbors(root)
    if(nx.is_directed(G) == False):
        if parent != None:
            neighs.remove(parent)
    for neigh in neighs:
        #Add one to current gen before stepping into child
        current_gen += 1    
        generations = get_generation_dict(G,neigh,generations,parent=root,current_gen=current_gen)
        generations[neigh] = current_gen
        #Minus one from current gen after stepping back up to parent
        current_gen-=1
    return generations   

def get_generations(G,root):
    '''Returns a dictionary with the key as the generation number and the value as a list of nodes in that generation
        and a dictionary with the nodes as keys and the values as the generation number for the node generations
        gen_dict - Generation list
        gens - Dictionary with each node and its generation'''
    gens = get_generation_dict(G,root)
    no_of_gens = max(gens.values())
    gen_dict = {k : [] for k in range(no_of_gens+1)}
    for i in range(no_of_gens+1):
        #For each generation create a list of nodes in this generation
        gen_list = [key for key,value in gens.iteritems() if value == i]
        gen_dict[i].extend(gen_list)
    return gen_dict, gens

def get_parent_per_gen(G,root,max_gens,parents=None,parent=None,current_gen=0):
    '''Returns the number of parents per generation in a list with index corresponding to generation'''
    if parent == None:
        parents = np.zeros(max_gens+1)
    #else:
     #   parents[current_gen] = parent_count
    neighs = G.neighbors(root)

    ##if parent != None:
      #  neighs.remove(parent)
        
    if len(neighs) != 0 :
        parents[current_gen] += 1

    for neigh in neighs:
        #Add one to current gen before stepping into child
        current_gen += 1    
        parents = get_parent_per_gen(G,neigh,max_gens,parents,parent=root,current_gen=current_gen)
        #generations[neigh] = current_gen
        #Minus one from current gen after stepping back up to parent
        current_gen-=1
    return parents   