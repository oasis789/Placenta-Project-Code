import LoadCode as lc
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import generations as generations
import plotlib as plott


def get_data(G):
    out_d = nx.out_degree_centrality(G)
    barren_node_list = [i for i,j in out_d.iteritems() if j==0]
    gens , g = generations.get_generations(G,max(G.nodes()))
    avg_terminating_gen = np.mean([g[i] for i in barren_node_list])
    root_children = G.degree(max(G.nodes()))
    branching_ratio = np.mean(np.mean(G.out_degree().values()))
    gen_density = float(max(gens.keys()))/float(max(G.nodes()))
    #return len(barren_node_list)/float(max(G.nodes())), avg_terminating_gen, max(G.nodes()), max(gens.keys()), root_children, branching_ratio, gen_density
    return max(G.nodes()), max(gens.keys()), gen_density, len(barren_node_list)/float(max(G.nodes())), avg_terminating_gen, root_children, branching_ratio
    


ncs_list, earli_list = lc.getNCSAndEARLIIDList()
na_N = []
na_G = []
na_dg = []
na_bn = []
na_gt = []
na_c = []
na_k = []

nv_N = []
nv_G = []
nv_dg = []
nv_bn = []
nv_gt = []
nv_c = []
nv_k = []

ea_N = []
ea_G = []
ea_dg = []
ea_bn = []
ea_gt = []
ea_c = []
ea_k = []

ev_N = []
ev_G = []
ev_dg = []
ev_bn = []
ev_gt = []
ev_c = []
ev_k = []


#Collate NCS data
for ncs_id in ncs_list:
    aG, vG, placenta = lc.getPlacentaNetworks(ncs_id)
    #NCS A Collate
    N,G,dg,bn,gt,c,k = get_data(aG)
    na_N.append(N)
    na_G.append(G)
    na_dg.append(dg)
    na_bn.append(bn)
    na_gt.append(gt)
    na_c.append(c)
    na_k.append(k)

    #NCS V Collate
    N,G,dg,bn,gt,c,k = get_data(vG)
    nv_N.append(N)
    nv_G.append(G)
    nv_dg.append(dg)
    nv_bn.append(bn)
    nv_gt.append(gt)
    nv_c.append(c)
    nv_k.append(k)

#Collate EARLI data
for earli_id in earli_list:
    aG, vG, placenta = lc.getPlacentaNetworks(earli_id)
    #EARLI A Collate
    N,G,dg,bn,gt,c,k = get_data(aG)
    ea_N.append(N)
    ea_G.append(G)
    ea_dg.append(dg)
    ea_bn.append(bn)
    ea_gt.append(gt)
    ea_c.append(c)
    ea_k.append(k)

    #EARLI V Collate
    N,G,dg,bn,gt,c,k = get_data(vG)
    ev_N.append(N)
    ev_G.append(G)
    ev_dg.append(dg)
    ev_bn.append(bn)
    ev_gt.append(gt)
    ev_c.append(c)
    ev_k.append(k)

def plot_histograms():
    plott.plot_ncs_earli_histogram(na_N,nv_N,ea_N,ev_N,'',r'$N$')
    plott.plot_ncs_earli_histogram(na_N,nv_N,ea_N,ev_N,'',r'$^N / _{\langle N \rangle}$',scaled=True)

    plott.plot_ncs_earli_histogram(na_G,nv_G,ea_G,ev_G,'',r'$G$')
    plott.plot_ncs_earli_histogram(na_G,nv_G,ea_G,ev_G,'',r'$^G / _{\langle G \rangle} $',scaled=True)

    plott.plot_ncs_earli_histogram(na_dg,nv_dg,ea_dg,ev_dg,'',r'$d_{g} = ^N/_G$')
    plott.plot_ncs_earli_histogram(na_dg,nv_dg,ea_dg,ev_dg,'',r'$^{d_{g}} / _{\langle d_{g} \rangle}$',scaled=True)
    
    plott.plot_ncs_earli_histogram(na_bn,nv_bn,ea_bn,ev_bn,'',r'Barren Node Prob $b_n$')
    plott.plot_ncs_earli_histogram(na_bn,nv_bn,ea_bn,ev_bn,'',r'$^{b_{n}} / _{\langle b_{n} \rangle}$',scaled=True)

    plott.plot_ncs_earli_histogram(na_gt,nv_gt,ea_gt,ev_gt,'',r'Average Terminating Gen $g_t$')
    plott.plot_ncs_earli_histogram(na_gt,nv_gt,ea_gt,ev_gt,'',r'$^{g_t} / _{\langle g_t \rangle}$',scaled=True)
    
    plott.plot_ncs_earli_histogram(na_c,nv_c,ea_c,ev_c,'',r'Number of Children at Root $c$')
    plott.plot_ncs_earli_histogram(na_c,nv_c,ea_c,ev_c,'',r'$^{c} / _{\langle c \rangle}$',scaled=True)
    
    plott.plot_ncs_earli_histogram(na_k,nv_k,ea_k,ev_k,'',r'Branching Probability $k$')
    plott.plot_ncs_earli_histogram(na_k,nv_k,ea_k,ev_k,'',r'$^{k} / _{\langle k \rangle}$',scaled=True)



def plot_data_against_N():
    plott.plot_ncs_earli_xy(na_G,na_N,nv_G,nv_N,ea_G,ea_N,ev_G,ev_N,'',r'$N$',r'$G$')
    plott.plot_ncs_earli_xy(na_dg,na_N,nv_dg,nv_N,ea_dg,ea_N,ev_dg,ev_N,'',r'$N$',r'$d_g$')
    plott.plot_ncs_earli_xy(na_bn,na_N,nv_bn,nv_N,ea_bn,ea_N,ev_bn,ev_N,'',r'$N$',r'$b_n$')
    plott.plot_ncs_earli_xy(na_gt,na_N,nv_gt,nv_N,ea_gt,ea_N,ev_gt,ev_N,'',r'$N$',r'$g_t$')
    plott.plot_ncs_earli_xy(na_c,na_N,nv_c,nv_N,ea_c,ea_N,ev_c,ev_N,'',r'$N$',r'$c$')
    plott.plot_ncs_earli_xy(na_k,na_N,nv_k,nv_N,ea_k,ea_N,ev_k,ev_N,'',r'$N$',r'$k$')


def plot_k_bn_fitted():
    plott.plot_ncs_earli_xy(na_bn,na_k,nv_bn,nv_k,ea_bn,ea_k,ev_bn,ev_k,r'$b_n = (1-(c-1)(k-1)) / 2 $',r'Branching Prob $k$',r'Barren Node Prob $b_n$')
    x = np.linspace(0.95,1.0,100)
    colors = ['r','b','g','k']
    for c in range(1,5):
        y = 0.5-(c-1)*(x-1)*0.5
        plt.plot(x,y,'-'+colors[c-1],label=r'$c={:d}$'.format(c))
    plt.legend(loc='best')
    
    
def plot_N_bn_fitted():
    plott.plot_ncs_earli_xy(na_bn,na_N,nv_bn,nv_N,ea_bn,ea_N,ev_bn,ev_N,r'$b_n = (N+c-1)/2N$',r'$N$',r'Barren Node Prob $b_n$')
    x = np.linspace(20,250,100)
    colors = ['r','b','g','k']
    for c in range(1,5):
        y = 0.5+0.5*(c-1)*x**(-1)
        plt.plot(x,y,'-'+colors[c-1],label=r'$c={:d}$'.format(c))
    plt.legend(loc='best')

def plot_N_bn_with_c_cmap():
    plt.figure()
    x_data = na_N + nv_N + ea_N + ev_N
    y_data = na_bn + nv_bn + ea_bn + ev_bn
    color_data = na_c + nv_c + ea_c + ev_c
    vmax = max(color_data)
    cmap = plt.get_cmap('jet',4)
    plt.scatter(x_data,y_data,c=color_data,cmap=cmap,vmin=1,vmax=vmax,alpha=0.8)
    plt.colorbar(ticks=[1,2,3,4],label=r'# Children from Root $c$')
    plt.xlabel(r'$N$')
    plt.ylabel(r'Barren Node Prob $b_n$')

def plot_N_k_fitted():
    plott.plot_ncs_earli_xy(na_k,na_N,nv_k,nv_N,ea_k,ea_N,ev_k,ev_N,r'$k=(N-1)/N$',r'$N$',r'Branching Ratio Prob $k$')
    x = np.linspace(15,250,100)
    y = (x-1)/x
    plt.plot(x,y,'-m',label=r'$\frac{N-1}{N}$')
    plt.legend(loc='best')

#plot_histograms()
#plot_data_against_N()
#plot_k_bn_fitted()
#plot_N_bn_fitted()
#plot_N_bn_with_c_cmap()
#plot_N_k_fitted()
plt.show()