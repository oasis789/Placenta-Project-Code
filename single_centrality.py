import LoadCode as lc
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import generations as g

colors = ['b','g','r','c','m','y','k']
def get_color(i):
    if i>=len(colors):
        return colors[i-len(colors)]
    else:
        return colors[i]

def degree_centrality(G):
    """Compute the degree centrality for nodes."""
    centrality={}
    #s=1.0/(len(G)-1.0)
    centrality=dict((n,d) for n,d in G.degree_iter())
    return centrality

def plot_with_gen_cmap(adata,agens,vdata,vgens,ID,ylabel):
    plt.figure()
    plt.subplot(2,1,1)
    plt.scatter(adata.keys(),adata.values(),c=agens.values(),vmin=min(agens.values()),vmax=max(agens.values()))
    x = np.linspace(min(adata.keys()),max(adata.keys()))
    y = np.mean(adata.values())
    plt.plot(x,[y for i in x], 'k-',label='Mean')
    plt.legend(loc='best')
    plt.colorbar(label='Generation Number')    
    plt.xlabel('Node')
    plt.ylabel(ylabel) 
    plt.title(ID+' Artery Network')
    plt.subplots_adjust(hspace=.5)

    plt.subplot(2,1,2)
    plt.scatter(vdata.keys(),vdata.values(),c=vgens.values(),vmin=min(vgens.values()),vmax=max(vgens.values()))
    x = np.linspace(min(vdata.keys()),max(vdata.keys()))
    y = np.mean(vdata.values())
    plt.plot(x,[y for i in x], 'k-',label='Mean')
    plt.legend(loc='best')
    plt.colorbar(label='Generation Number')    
    plt.xlabel('Node')
    plt.ylabel(ylabel) 
    plt.title(ID+' Vein Network')
    
    plt.show()

def run(ID):
    aG, vG, p = lc.getPlacentaNetworks(ID)
    ag_list,ag = g.get_generations(aG,max(aG.nodes()))
    vg_list,vg = g.get_generations(vG,max(vG.nodes()))    
    
    #Closeness Centrality
    ac = nx.closeness_centrality(aG)
    vc = nx.closeness_centrality(vG.reverse())
    plot_with_gen_cmap(ac,ag,vc,vg,ID,'Directed Closeness')
    #'plot_with_gen_cmap(vc,vg,ID+' Vein Network','Directed Closeness')

    
    #Current Flow Closeness Centrality
    acc = nx.current_flow_closeness_centrality(aG.to_undirected())
    vcc = nx.current_flow_closeness_centrality(vG.to_undirected())
    plot_with_gen_cmap(acc,ag,vcc,vg,ID,'Current Flow Closeness')
    #plot_with_gen_cmap(vcc,vg,ID+' Vein Network','Current Flow Closeness')

    
    #Betweeness Centrality
    ab = nx.betweenness_centrality(aG)
    vb = nx.betweenness_centrality(vG.reverse())
    plot_with_gen_cmap(ab,ag,vb,vg,ID,'Betweenness')
    #plot_with_gen_cmap(vb,vg,ID+' Vein Network','Betweenneness')

    '''
    artery_c = nx.eccentricity(artery_G)
    vein_c = nx.eccentricity(vein_G)
    plt.figure()
    plt.title(ID+' Network Eccentricity')e
    plot_by_gen(artery_c,ag_list,'.')
    plot_by_gen(vein_c,vg_list,'+')'''
   
#run('BN0013990')
#run('E1020136')
run('BN2641672')
plt.show()