import LoadCode as lc
import networkx as nx
import numpy as np
import plotlib as plott
import generations as gens
import operator
import matplotlib.pyplot as plt

def centre_of_mass(G, mass):
    g = gens.get_generation_dict(G.to_undirected(),max(G.nodes()))
    M = sum(mass.values())
    s=0
    for n in G.nodes():
        s+=mass[n]*(g[n]+1)
    return s/float(M)

def get_data(G):
    N = max(G.nodes())
    close = nx.closeness_centrality(G)
    c = np.mean(close.values())
    c_std = np.std(close.values()) / float(np.sqrt(N))

    close_current = nx.current_flow_closeness_centrality(G.to_undirected())
    cc = np.mean(close_current.values())
    cc_std = np.std(close_current.values()) / float(np.sqrt(N))

    #betw = np.mean(nx.betweenness_centrality(G).values())
    betw = G.degree(max(G.nodes()))
    #betw = centre_of_mass(G,close_current)
    betw_current = np.mean(nx.current_flow_betweenness_centrality(G.to_undirected()).values())
    #betw_current = np.mean(nx.harmonic_centrality(G.to_undirected()).values())
    assort = nx.degree_assortativity_coefficient(G.to_undirected())
    branching_ratio = np.mean(np.mean(G.out_degree().values()))
    return c, c_std, cc, cc_std, betw, betw_current, branching_ratio, assort, N
    
na_c = []
na_c_std = []
na_cc = []
na_cc_std = []

na_b = []
na_bc = []
na_k= []
na_a = []
na_N = []

nv_c = []
nv_c_std = []
nv_cc = []
nv_cc_std = []
nv_b = []
nv_bc = []
nv_k = []
nv_a = []
nv_N = []

ea_c = []
ea_c_std = []
ea_cc = []
ea_cc_std = []
ea_b = []
ea_bc = []
ea_k = []
ea_a = []
ea_N = []

ev_c = []
ev_c_std = []
ev_cc = []
ev_cc_std = []
ev_b = []
ev_bc = []
ev_k = []
ev_a = []
ev_N = []

ncs_list, earli_list = lc.getNCSAndEARLIIDList()

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG,p = lc.getPlacentaNetworks(ncs_id)
    c, c_std, cc, cc_std, b, bc, k, a, N = get_data(aG)
    na_c.append(c)
    na_c_std.append(c_std)
    na_cc.append(cc)
    na_cc_std.append(cc_std)
    na_b.append(b)
    na_bc.append(bc)
    na_k.append(k)
    na_a.append(a)
    na_N.append(N)
    
    c,c_std, cc, cc_std, b, bc, k, a, N = get_data(vG.reverse())
    nv_c.append(c)
    nv_c_std.append(c_std)
    nv_cc.append(cc)
    nv_cc_std.append(cc_std)
    nv_b.append(b)
    nv_bc.append(bc)
    nv_k.append(k)
    nv_a.append(a)
    nv_N.append(N)

#Collate EARLI data
for earli_id in earli_list:
    aG, vG,p = lc.getPlacentaNetworks(earli_id)
    c, c_std, cc, cc_std, b, bc, k, a, N = get_data(aG)
    ea_c.append(c)
    ea_c_std.append(c_std)
    ea_cc.append(cc)
    ea_cc_std.append(cc_std)
    ea_b.append(b)
    ea_bc.append(bc)
    ea_k.append(k)
    ea_a.append(a)
    ea_N.append(N)
    
    c, c_std, cc, cc_std, b, bc, k, a, N = get_data(vG.reverse())
    ev_c.append(c)
    ev_c_std.append(c_std)
    ev_cc.append(cc)
    ev_cc_std.append(cc_std)
    ev_b.append(b)
    ev_bc.append(bc)
    ev_k.append(k)
    ev_a.append(a)
    ev_N.append(N)



def plot_histograms():
    plott.plot_ncs_earli_histogram(na_c,nv_c,ea_c,ev_c,'','Closeness')
    plott.plot_ncs_earli_histogram(na_c,nv_c,ea_c,ev_c,'Scaled','Closeness',scaled=True)
    plott.plot_ncs_earli_histogram(na_cc,nv_cc,ea_cc,ev_cc,'','Current Flow Closeness')
    plott.plot_ncs_earli_histogram(na_cc,nv_cc,ea_cc,ev_cc,'Scaled','Current Flow Closeness',scaled=True)
    plott.plot_ncs_earli_histogram(na_b,nv_b,ea_b,ev_b,'','Betweenness')
    plott.plot_ncs_earli_histogram(na_b,nv_b,ea_b,ev_b,'Scaled','Betweenness',scaled=True)
    plott.plot_ncs_earli_histogram(na_bc,nv_bc,ea_bc,ev_bc,'','Current Flow Betweenness')
    plott.plot_ncs_earli_histogram(na_bc,nv_bc,ea_bc,ev_bc,'Scaled','Current Flow Betweenness',scaled=True)
    plott.plot_ncs_earli_histogram(na_a,nv_a,ea_a,ev_a,'','Degree Assortativity')
    plott.plot_ncs_earli_histogram(na_a,nv_a,ea_a,ev_a,'Scaled','Degree Assortativity',scaled=True)

def plot_data_against_N():
    plott.plot_ncs_earli_xy(na_c,na_N,nv_c,nv_N,ea_c,ea_N,ev_c,ev_N,'',r'$N$','Closeness')
    plott.plot_ncs_earli_xy(na_cc,na_N,nv_cc,nv_N,ea_cc,ea_N,ev_cc,ev_N,'',r'$N$','Current Flow Closeness')
    plott.plot_ncs_earli_xy(na_b,na_N,nv_b,nv_N,ea_b,ea_N,ev_b,ev_N,'',r'$N$','Betweenness')
    plott.plot_ncs_earli_xy(na_bc,na_N,nv_bc,nv_N,ea_bc,ea_N,ev_bc,ev_N,'',r'$N$','Current Flow Betweenness')
    plott.plot_ncs_earli_xy(na_a,na_N,nv_a,nv_N,ea_a,ea_N,ev_a,ev_N,'',r'$N$','Degree Assortativity')

def log_fit(xdata,ydata,color,label):
    m,c = np.polyfit(np.log(xdata),np.log(ydata),1)
    xp = np.linspace(20,230,100)
    yp = [np.exp(c) * (x**m) for x in xp]
    plt.loglog(xp,yp,color+'-',label=label+'$(m,c)=({:.1f},{:.1f})$'.format(m,c))
    return m,c

def linear_fit(xdata,ydata,color,label):
    coeffs = np.polyfit(xdata,ydata,2)
    xp = np.linspace(0.94,1.0,100)
    f = np.poly1d(coeffs)
    #yp = [(m*x + c) for x in xp]
    plt.plot(xp,f(xp),color+'-',label=label+'$(c_2,c_1,c_0)=({:.1f},{:.1f},{:.1f})$'.format(coeffs[0],coeffs[1],coeffs[2]))
    print coeffs
    #return m,c

def fitting_c_and_N():
    plt.figure()
    plt.loglog(na_N,na_c,'r.',label='NCS A')
    plt.errorbar(na_N,na_c,na_c_std,color='r',linestyle='None')

    plt.loglog(nv_N,nv_c,'b.',label='NCS V')
    plt.errorbar(nv_N,nv_c,nv_c_std,color='b',linestyle='None')

    plt.loglog(ea_N,ea_c,'g.',label='EARLI A')
    plt.errorbar(ea_N,ea_c,ea_c_std,color='g',linestyle='None')

    plt.loglog(ev_N,ev_c,'k.',label='EARLI V')
    plt.errorbar(ev_N,ev_c,ev_c_std,color='k',linestyle='None')

    a_data = na_c + ea_c
    v_data = nv_c + ev_c
    xa_data = na_N + ea_N
    xv_data = nv_N + ev_N
    

    m1,c1 = log_fit(xa_data,a_data,'r','A ')
    m2,c2 = log_fit(xv_data,v_data,'b','V ')
    plt.legend(loc='best')
    plt.xlabel(r'$N$')
    plt.ylabel('Directed Closeness')
    print m1,c1
    print m2,c2
    
def fitting_c_and_k():
    
    plt.figure()
    plt.plot(na_k,na_c,'r.',label='NCS A')
    plt.errorbar(na_k,na_c,na_c_std,color='r',linestyle='None')
    
    plt.plot(nv_k,nv_c,'b.',label='NCS V')
    plt.errorbar(nv_k,nv_c,nv_c_std,color='b',linestyle='None')

    plt.plot(ea_k,ea_c,'g.',label='EARLI A')
    plt.errorbar(ea_k,ea_c,ea_c_std,color='g',linestyle='None')

    plt.plot(ev_k,ev_c,'k.',label='EARLI V')
    plt.errorbar(ev_k,ev_c,ev_c_std,color='k',linestyle='None')

    a_data = na_c + ea_c
    v_data = nv_c + ev_c
    xa_data = na_k + ea_k
    xv_data = nv_k + ev_k

    linear_fit(xa_data,a_data,'r','A ')
    linear_fit(xv_data,v_data,'b','V ')
    plt.legend(loc='best')
    plt.xlabel(r'$k$')
    plt.ylabel('Directed Closeness')
    #print m1,c1
    #print m2,c2

def fitting_cc_and_N():
    y_data = na_cc + ea_cc + nv_cc + ev_cc
    x_data = na_N + ea_N + nv_N + ev_N
    plt.figure()
    plt.loglog(na_N,na_cc,'r.',label='NCS A')
    plt.errorbar(na_N,na_cc,na_cc_std,color='r',linestyle='None')

    plt.loglog(nv_N,nv_cc,'b.',label='NCS V')
    plt.errorbar(nv_N,nv_cc,nv_cc_std,color='b',linestyle='None')

    plt.loglog(ea_N,ea_cc,'g.',label='EARLI A')
    plt.errorbar(ea_N,ea_cc,ea_cc_std,color='g',linestyle='None')

    plt.loglog(ev_N,ev_cc,'k.',label='EARLI V')
    plt.errorbar(ev_N,ev_cc,ev_cc_std,color='k',linestyle='None')

    m,c = log_fit(x_data,y_data,'r','')
    plt.legend(loc='best')
    plt.xlabel(r'$N$')
    plt.ylabel('Current Flow Closeness')
    print m,c

def fitting_cc_and_k():
    y_data = na_cc + ea_cc + nv_cc + ev_cc
    x_data = na_k + ea_k + nv_k + ev_k
    plt.figure()
    plt.plot(na_k,na_cc,'r.',label='NCS A')
    plt.errorbar(na_k,na_cc,na_cc_std,color='r',linestyle='None')

    plt.plot(nv_k,nv_cc,'b.',label='NCS V')
    plt.errorbar(nv_k,nv_cc,nv_cc_std,color='b',linestyle='None')

    plt.plot(ea_k,ea_cc,'g.',label='EARLI A')
    plt.errorbar(ea_k,ea_cc,ea_cc_std,color='g',linestyle='None')

    plt.plot(ev_k,ev_cc,'k.',label='EARLI V')   
    plt.errorbar(ev_k,ev_cc,ev_cc_std,color='k',linestyle='None')

    linear_fit(x_data,y_data,'r','')
    plt.legend(loc='best')
    plt.xlabel(r'$k$')
    plt.ylabel('Current Flow Closeness')
    #print m,c

def plot_assort_with_c_cmap():
    plt.figure()
    x_data = na_N + nv_N + ea_N + ev_N
    y_data = na_a + nv_a + ea_a + ev_a
    color_data = na_b + nv_b + ea_b + ev_b
    vmax = max(color_data)
    cmap = plt.get_cmap('jet',4)
    plt.scatter(x_data,y_data,c=color_data,cmap=cmap,vmin=1,vmax=vmax,alpha=0.8)
    plt.colorbar(ticks=[1,2,3,4],label=r'# Children from Root $c$')
    plt.xlabel(r'$N$')
    plt.ylabel(r'Degree Assortativity')

        
    

#fitting_c_and_N()
#fitting_c_and_k()
#plot_histograms()
#plot_data_against_N()
#fitting_cc_and_N()
#fitting_cc_and_k()
plot_assort_with_c_cmap()
plott.show()


    
    