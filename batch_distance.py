import LoadCode as lc
import networkx as nx
import numpy as np
import generations as gens
import plotlib as plott
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def log_fit(xdata,ydata,color,label):
    m,c = np.polyfit(np.log(xdata),np.log(ydata),1)
    xp = np.linspace(min(xdata),max(xdata),100)
    yp = [np.exp(c) * (x**m) for x in xp]
    plt.loglog(xp,yp,color+'-',label=label)
    return m,c

def get_data(G):    
    ecc = np.mean(nx.eccentricity(G.to_undirected()).values())
    radius =  nx.radius(G.to_undirected())
    diameter = nx.diameter(G.to_undirected())
    density = nx.density(G)
    branching_ratio =  np.mean(np.mean(G.out_degree().values()))
    out_d = nx.out_degree_centrality(G)
    barren_node_list = [i for i,j in out_d.iteritems() if j==0]
    return ecc, radius, diameter, density, branching_ratio, max(G.nodes()), len(barren_node_list)/float(max(G.nodes()))
    

#Distance Measures Analysis
na_ecc = []
na_r = []
na_d = []
na_den = []
na_k= []
na_N = []
na_bn = []

nv_ecc = []
nv_r = []
nv_d = []
nv_den = []
nv_k= []
nv_N = []
nv_bn = []

ea_ecc = []
ea_r = []
ea_d = []
ea_den = []
ea_k= []
ea_N = []
ea_bn = []

ev_ecc = []
ev_r = []
ev_d = []
ev_den = []
ev_k= []
ev_N = []
ev_bn = []

ncs_list, earli_list = lc.getNCSAndEARLIIDList()

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG, p = lc.getPlacentaNetworks(ncs_id)
    ecc,r,d,den,k,N,bn = get_data(aG)
    na_ecc.append(ecc)
    na_r.append(r)
    na_d.append(d)
    na_den.append(den)
    na_k.append(k)
    na_N.append(N)
    na_bn.append(bn)

    
    ecc,r,d,den,k,N,bn = get_data(vG)
    nv_ecc.append(ecc)
    nv_r.append(r)
    nv_d.append(d)
    nv_den.append(den)
    nv_k.append(k)
    nv_N.append(N)
    nv_bn.append(bn)

#Collate EARLI data
for earli_id in earli_list:
    aG, vG, p = lc.getPlacentaNetworks(earli_id)
    ecc,r,d,den,k,N,bn = get_data(aG)
    ea_ecc.append(ecc)
    ea_r.append(r)
    ea_d.append(d)
    ea_den.append(den)
    ea_k.append(k)
    ea_N.append(N)
    ea_bn.append(bn)
    
    ecc,r,d,den,k,N,bn = get_data(vG)
    ev_ecc.append(ecc)
    ev_r.append(r)
    ev_d.append(d)
    ev_den.append(den)
    ev_k.append(k)
    ev_N.append(N)
    ev_bn.append(bn)

def plot_data_against_N():
    plott.plot_ncs_earli_xy(na_ecc,na_N,nv_ecc,nv_N,ea_ecc,ea_N,ev_ecc,ev_N,'',r'$N$','Average Eccentricity')
    plott.plot_ncs_earli_xy(na_r,na_N,nv_r,nv_N,ea_r,ea_N,ev_r,ev_N,'',r'$N$','Radius')
    plott.plot_ncs_earli_xy(na_d,na_N,nv_d,nv_N,ea_d,ea_N,ev_d,ev_N,'',r'$N$','Diameter')
    plott.plot_ncs_earli_xy(na_den,na_N,nv_den,nv_N,ea_den,ea_N,ev_den,ev_N,'',r'$N$','Density')

def plot_data_against_k():
    plott.plot_ncs_earli_xy(na_ecc,na_k,nv_ecc,nv_k,ea_ecc,ea_k,ev_ecc,ev_k,'',r'$k$','Average Eccentricity')
    plott.plot_ncs_earli_xy(na_r,na_k,nv_r,nv_k,ea_r,ea_k,ev_r,ev_k,'',r'$k$','Radius')
    plott.plot_ncs_earli_xy(na_d,na_k,nv_d,nv_k,ea_d,ea_k,ev_d,ev_k,'',r'$k$','Diameter')
    plott.plot_ncs_earli_xy(na_den,na_k,nv_den,nv_k,ea_den,ea_k,ev_den,ev_k,'',r'$k$','Density')

def plot_data_against_bn():
    plott.plot_ncs_earli_xy(na_ecc,na_bn,nv_ecc,nv_bn,ea_ecc,ea_bn,ev_ecc,ev_bn,'',r'$b_n$','Average Eccentricity')
    plott.plot_ncs_earli_xy(na_r,na_bn,nv_r,nv_bn,ea_r,ea_bn,ev_r,ev_bn,'',r'$b_n$','Radius')
    plott.plot_ncs_earli_xy(na_d,na_bn,nv_d,nv_bn,ea_d,ea_bn,ev_d,ev_bn,'',r'$b_n$','Diameter')
    plott.plot_ncs_earli_xy(na_den,na_bn,nv_den,nv_bn,ea_den,ea_bn,ev_den,ev_bn,'',r'$b_n$','Density')

def plot_histograms():
    plott.plot_ncs_earli_histogram(na_ecc,nv_ecc,ea_ecc,ev_ecc,'',r'$Eccentricity$')
    plott.plot_ncs_earli_histogram(na_r,nv_r,ea_r,ev_r,'',r'$Radius$')
    plott.plot_ncs_earli_histogram(na_d,nv_d,ea_d,ev_d,'',r'$Diameter$')
    plott.plot_ncs_earli_histogram(na_den,nv_den,ea_den,ev_den,'',r'$Density$')



    

#plot_data_against_N()
plot_data_against_k()
plot_data_against_bn()
plot_histograms
plt.show()

    
    