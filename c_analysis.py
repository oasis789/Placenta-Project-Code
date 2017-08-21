import LoadCode as lc
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import generations as generations
import plotlib as plott
import matplotlib.mlab as mlab
import itertools

def get_data(G):
    out_d = nx.out_degree_centrality(G)
    barren_node_list = [i for i,j in out_d.iteritems() if j==0]
    gens , g = generations.get_generations(G,max(G.nodes()))
    avg_terminating_gen = np.mean([g[i] for i in barren_node_list])
    root_children = G.degree(max(G.nodes()))
    branching_ratio = np.mean(np.mean(G.out_degree().values()))
    gen_density = max(G.nodes())/float(max(gens.keys()))
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

plott.plot_ncs_earli_histogram(na_c,nv_c,ea_c,ev_c,'',r'Number of Children at Root $c$')


def c_analysis(data,label):
    C = na_c + nv_c + ea_c + ev_c
    C_dict = {k+1:[] for k in range(4)}
    for i in range(4):
        indicies = [j for j,x in enumerate(C) if x==(i+1)]
        c_data = [data[index] for index in indicies]
        C_dict[i+1].extend(c_data)
    
    c1 = C_dict[1]
    c2 = C_dict[2]
    c3 = C_dict[3]
    c4 = C_dict[4]

    print label
    print np.mean(c1), np.std(c1)
    print np.mean(c2), np.std(c2)
    print np.mean(c3), np.std(c3)
    print np.mean(c4), np.std(c4)
    
    plt.figure()
    data_list = [c1,c2,c3,c4]
    colors = ['r','b','g','k']
    plt.hist(data_list,bins=10,normed=True,color=colors,label=['$c=1$','$c=2$','$c=3$','$c=4$'])
    for i,data in enumerate(data_list):
            #y = mlab.normpdf(bins,np.mean(data),np.std(data))
            #shape,loc,scale = scipy.stats.lognorm.fit(data,floc=0)
            x_fit = np.linspace(min(data),max(data),100)
            #y_fit = scipy.stats.lognorm.pdf(x_fit,shape,loc=loc,scale=scale)
            y_fit = mlab.normpdf(x_fit,np.mean(data), np.std(data))
            plt.plot(x_fit,y_fit,colors[i]+'--',linewidth=1)
    plt.legend(loc='best')
    plt.xlabel(label)
    plt.ylabel('Frequency Density')
    plt.show()

c_analysis(na_N + nv_N + ea_N + ev_N,'$N$')
c_analysis(na_G + nv_G + ea_G + ev_G,'$G$')
c_analysis(na_k + nv_k + ea_k + ev_k,'$k$')
c_analysis(na_bn + nv_bn + ea_bn + ev_bn,'$b_n$')





'''
G = na_G + nv_G + ea_G + ev_G
C = na_c + nv_c + ea_c + ev_c
G_C_dict = dict(zip(G,C))
c1 = [i for i,j in G_C_dict.iteritems() if j==1]
c2 = [i for i,j in G_C_dict.iteritems() if j==2]
c3 = [i for i,j in G_C_dict.iteritems() if j==3]
c4 = [i for i,j in G_C_dict.iteritems() if j==4]
print 'G'
print np.mean(c1), np.std(c1)
print np.mean(c2), np.std(c2)
print np.mean(c3), np.std(c3)
print np.mean(c4), np.std(c4)

plt.figure()
data_list = [c1,c2,c3,c4]
colors = ['r','b','g','k']
plt.hist(data_list,bins=10,normed=True,color=colors,label=['$c=1$','$c=2$','$c=3$','$c=4$'])
for i,data in enumerate(data_list):
        #y = mlab.normpdf(bins,np.mean(data),np.std(data))
        #shape,loc,scale = scipy.stats.lognorm.fit(data,floc=0)
        x_fit = np.linspace(min(data),max(data),100)
        #y_fit = scipy.stats.lognorm.pdf(x_fit,shape,loc=loc,scale=scale)
        y_fit = mlab.normpdf(x_fit,np.mean(data), np.std(data))
        plt.plot(x_fit,y_fit,colors[i]+'--',linewidth=1)
plt.legend(loc='best')
plt.xlabel('$G$')
plt.ylabel('Frequency Density')
plt.show()


K = na_k + nv_k + ea_k + ev_k
K_C_dict = dict(zip(K,C))
c1 = [i for i,j in K_C_dict.iteritems() if j==1]
c2 = [i for i,j in K_C_dict.iteritems() if j==2]
c3 = [i for i,j in K_C_dict.iteritems() if j==3]
c4 = [i for i,j in K_C_dict.iteritems() if j==4]

plt.figure()
data_list = [c1,c2,c3,c4]
colors = ['r','b','g','k']
plt.hist(data_list,bins=10,normed=True,color=colors,label=['$c=1$','$c=2$','$c=3$','$c=4$'])
for i,data in enumerate(data_list):
        #y = mlab.normpdf(bins,np.mean(data),np.std(data))
        #shape,loc,scale = scipy.stats.lognorm.fit(data,floc=0)
        x_fit = np.linspace(min(data),max(data),100)
        #y_fit = scipy.stats.lognorm.pdf(x_fit,shape,loc=loc,scale=scale)
        y_fit = mlab.normpdf(x_fit,np.mean(data), np.std(data))
        plt.plot(x_fit,y_fit,colors[i]+'--',linewidth=1)
plt.legend(loc='best')
plt.xlabel('$k$')
plt.ylabel('Frequency Density')
plt.show()

B = na_bn + nv_bn + ea_bn + ev_bn
B_C_dict = dict(zip(B,C))
c1 = [i for i,j in B_C_dict.iteritems() if j==1]
c2 = [i for i,j in B_C_dict.iteritems() if j==2]
c3 = [i for i,j in B_C_dict.iteritems() if j==3]
c4 = [i for i,j in B_C_dict.iteritems() if j==4]

plt.figure()
data_list = [c1,c2,c3,c4]
colors = ['r','b','g','k']
plt.hist(data_list,bins=10,normed=True,color=colors,label=['$c=1$','$c=2$','$c=3$','$c=4$'])
for i,data in enumerate(data_list):
        #y = mlab.normpdf(bins,np.mean(data),np.std(data))
        #shape,loc,scale = scipy.stats.lognorm.fit(data,floc=0)
        x_fit = np.linspace(min(data),max(data),100)
        #y_fit = scipy.stats.lognorm.pdf(x_fit,shape,loc=loc,scale=scale)
        y_fit = mlab.normpdf(x_fit,np.mean(data), np.std(data))
        plt.plot(x_fit,y_fit,colors[i]+'--',linewidth=1)
plt.legend(loc='best')
plt.xlabel('$b_n$')
plt.ylabel('Frequency Density')
plt.show()

'''