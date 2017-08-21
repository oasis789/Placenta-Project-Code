import LoadCode as lc
import networkx as nx
import numpy as np
import plotlib as plott
import generations as gens
import operator
import matplotlib.pyplot as plt

def get_data(G,network):
    un_G = G
    G = G.to_undirected()
    vessels = network.getVessels()
    N = max(G.nodes())
    g = gens.get_generation_dict(G,max(G.nodes()))
    for vessel in vessels:
        length = vessel.getArcLength()
        diameter = vessel.getDiameter()
        #print length, diameter
        if diameter == 0:
            diameter = 1.

        if length == 0:
            length = 1.
        diameter = length * (np.pi*diameter**2)/4.
        #diameter = 4.*length / float(np.pi * diameter**2)
        #diameter = 128*0.003*length / float(np.pi * diameter**4)
        (x,y) = vessel.getEdgePair()
        G[x][y]['length'] = length
        G[x][y]['diameter'] = 1/float(diameter)
    #if (length or diameter) == 0:
       # print 'No vessel data'
    try:
        cc_length = nx.current_flow_closeness_centrality(G,weight='length').values()
    except RuntimeError:
        cc_length = 1.
        
    try:
        cc_diameter = nx.current_flow_closeness_centrality(G,weight='diameter').values()
    except RuntimeError:
        cc_diameter = 1.

    cc_l = np.mean(cc_length)
    cc_l_er = np.std(cc_length)/float(np.sqrt(N))
    cc_d = np.mean(cc_diameter)
    cc_d_er = np.std(cc_diameter)/float(np.sqrt(N))
    branching_ratio = np.mean(np.mean(un_G.out_degree().values()))
    return cc_l, cc_l_er, cc_d, cc_d_er, branching_ratio, N
    
na_cc_l = []
na_cc_l_er = []
na_cc_d = []
na_cc_d_er = []
na_k= []
na_N = []

nv_cc_l = []
nv_cc_l_er = []
nv_cc_d = []
nv_cc_d_er = []
nv_k = []
nv_N = []

ea_cc_l = []
ea_cc_l_er = []
ea_cc_d = []
ea_cc_d_er = []
ea_k = []
ea_N = []

ev_cc_l = []
ev_cc_l_er = []
ev_cc_d = []
ev_cc_d_er = []
ev_k = []
ev_N = []

ncs_list, earli_list = lc.getNCSAndEARLIIDList()

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG,p = lc.getPlacentaNetworks(ncs_id)
    cc_l, cc_l_er, cc_d, cc_d_er, k, N = get_data(aG,p.getArteryNetwork())
    na_cc_l.append(cc_l)
    na_cc_l_er.append(cc_l_er)
    na_cc_d.append(cc_d)
    na_cc_d_er.append(cc_d_er)
    na_k.append(k)
    na_N.append(N)
    
    cc_l, cc_l_er, cc_d, cc_d_er, k, N = get_data(vG,p.getVeinNetwork())
    nv_cc_l.append(cc_l)
    nv_cc_l_er.append(cc_l_er)
    nv_cc_d.append(cc_d)
    nv_cc_d_er.append(cc_d_er)
    nv_k.append(k)
    nv_N.append(N)

#Collate EARLI data
for earli_id in earli_list:
    aG, vG,p = lc.getPlacentaNetworks(earli_id)
    cc_l, cc_l_er, cc_d, cc_d_er, k, N = get_data(aG,p.getArteryNetwork())
    ea_cc_l.append(cc_l)
    ea_cc_l_er.append(cc_l_er)
    ea_cc_d.append(cc_d)
    ea_cc_d_er.append(cc_d_er)
    ea_k.append(k)
    ea_N.append(N)
    
    cc_l, cc_l_er, cc_d, cc_d_er, k, N = get_data(vG,p.getVeinNetwork())
    ev_cc_l.append(cc_l)
    ev_cc_l_er.append(cc_l_er)
    ev_cc_d.append(cc_d)
    ev_cc_d_er.append(cc_d_er)
    ev_k.append(k)
    ev_N.append(N)

def log_fit(xdata,ydata,color,label):
    m,c = np.polyfit(np.log(xdata),np.log(ydata),1)
    xp = np.linspace(20,230,100)
    yp = [np.exp(c) * (x**m) for x in xp]
    plt.loglog(xp,yp,color+'-',label=label+'$(m,c)=({:.2f},{:.2f})$'.format(m,c))
    print m,c
    return m,c

def linear_fit(xdata,ydata,color,label):
    coeffs = np.polyfit(xdata,ydata,2)
    xp = np.linspace(0.94,1.0,100)
    f = np.poly1d(coeffs)
    #yp = [(m*x + c) for x in xp]
    plt.plot(xp,f(xp),color+'-',label=label+'$(c_2,c_1,c_0)=({:.1f},{:.1f},{:.1f})$'.format(coeffs[0],coeffs[1],coeffs[2]))
    print coeffs
    #return m,c

def fitting_cc_l_and_N():
    plt.figure()
    plt.loglog(na_N,na_cc_l,'r.',label='NCS A')
    plt.errorbar(na_N,na_cc_l,na_cc_l_er,color='r',linestyle='None')

    plt.loglog(nv_N,nv_cc_l,'b.',label='NCS V')
    plt.errorbar(nv_N,nv_cc_l,nv_cc_l_er,color='b',linestyle='None')

    plt.loglog(ea_N,ea_cc_l,'g.',label='EARLI A')
    plt.errorbar(ea_N,ea_cc_l,ea_cc_l_er,color='g',linestyle='None')

    plt.loglog(ev_N,ev_cc_l,'k.',label='EARLI V')
    plt.errorbar(ev_N,ev_cc_l,ev_cc_l_er,color='k',linestyle='None')

    ncs_x = na_N + nv_N
    ncs_y = na_cc_l + nv_cc_l
    ea_x = ea_N + ev_N
    ea_y = ea_cc_l + ev_cc_l

    m,c = log_fit(ncs_x,ncs_y,'r','NCS')
    m,c = log_fit(ea_x,ea_y,'g','EARLI')
    plt.legend(loc='best')
    plt.xlabel(r'$N$')
    plt.ylabel('Current Flow Closeness')
    plt.title('Weighted by Length')

def fitting_cc_d_and_N():
    plt.figure()
    plt.loglog(na_N,na_cc_d,'r.',label='NCS A')
    plt.errorbar(na_N,na_cc_d,na_cc_d_er,color='r',linestyle='None')

    plt.loglog(nv_N,nv_cc_d,'b.',label='NCS V')
    plt.errorbar(nv_N,nv_cc_d,nv_cc_d_er,color='b',linestyle='None')

    plt.loglog(ea_N,ea_cc_d,'g.',label='EARLI A')
    plt.errorbar(ea_N,ea_cc_d,ea_cc_d_er,color='g',linestyle='None')

    plt.loglog(ev_N,ev_cc_d,'k.',label='EARLI V')
    plt.errorbar(ev_N,ev_cc_d,ev_cc_d_er,color='k',linestyle='None')

    
    ncs_x = na_N + nv_N
    ncs_y = na_cc_d + nv_cc_d
    ea_x = ea_N + ev_N
    ea_y = ea_cc_d + ev_cc_d

    m,c = log_fit(ncs_x,ncs_y,'r','NCS')
    m,c = log_fit(ea_x,ea_y,'g','EARLI')
    plt.legend(loc='best')
    plt.xlabel(r'$N$')
    plt.ylabel('Current Flow Closeness')
    plt.title('Weighted by Diameter')

def fitting_cc_l_and_k():
    plt.figure()
    plt.plot(na_k,na_cc_l,'r.',label='NCS A')
    plt.errorbar(na_k,na_cc_l,na_cc_l_er,color='r',linestyle='None')

    plt.plot(nv_k,nv_cc_l,'b.',label='NCS V')
    plt.errorbar(nv_k,nv_cc_l,nv_cc_l_er,color='b',linestyle='None')

    plt.plot(ea_k,ea_cc_l,'g.',label='EARLI A')
    plt.errorbar(ea_k,ea_cc_l,ea_cc_l_er,color='g',linestyle='None')

    plt.plot(ev_k,ev_cc_l,'k.',label='EARLI V')
    plt.errorbar(ev_k,ev_cc_l,ev_cc_l_er,color='k',linestyle='None')

    ncs_x = na_k + nv_k
    ncs_y = na_cc_l + nv_cc_l
    ea_x = ea_k + ev_k
    ea_y = ea_cc_l + ev_cc_l

    linear_fit(ncs_x,ncs_y,'r','NCS')
    linear_fit(ea_x,ea_y,'g','EARLI')
    plt.legend(loc='best')
    plt.xlabel(r'$k$')
    plt.ylabel('Current Flow Closeness')
    plt.title('Weighted by Length')

def fitting_cc_d_and_k():
    plt.figure()
    plt.plot(na_k,na_cc_d,'r.',label='NCS A')
    plt.errorbar(na_k,na_cc_d,na_cc_d_er,color='r',linestyle='None')

    plt.plot(nv_k,nv_cc_d,'b.',label='NCS V')
    plt.errorbar(nv_k,nv_cc_d,nv_cc_d_er,color='b',linestyle='None')

    plt.plot(ea_k,ea_cc_d,'g.',label='EARLI A')
    plt.errorbar(ea_k,ea_cc_d,ea_cc_d_er,color='g',linestyle='None')

    plt.plot(ev_k,ev_cc_d,'k.',label='EARLI V')
    plt.errorbar(ev_k,ev_cc_d,ev_cc_d_er,color='k',linestyle='None')


    ncs_x = na_k + nv_k
    ncs_y = na_cc_d + nv_cc_d
    ea_x = ea_k + ev_k
    ea_y = ea_cc_d + ev_cc_d

    linear_fit(ncs_x,ncs_y,'r','NCS')
    linear_fit(ea_x,ea_y,'g','EARLI')
    plt.legend(loc='best')
    plt.xlabel(r'$k$')
    plt.ylabel('Current Flow Closeness')
    plt.title('Weighted by Diameter')

def plot_data():
    plott.plot_ncs_earli_xy(na_cc_l,na_N,nv_cc_l,nv_N,ea_cc_l,ea_N,ev_cc_l,ev_N,'Weighted by Length',r'$N$','Current Flow Closeness')
    plott.plot_ncs_earli_xy(na_cc_l,na_k,nv_cc_l,nv_k,ea_cc_l,ea_k,ev_cc_l,ev_k,'Weighted by Length',r'$k$','Current Flow Closeness')
    
    plott.plot_ncs_earli_xy(na_cc_d,na_N,nv_cc_d,nv_N,ea_cc_d,ea_N,ev_cc_d,ev_N,'Weighted by Diameter',r'$N$','Current Flow Closeness')
    plott.plot_ncs_earli_xy(na_cc_d,na_k,nv_cc_d,nv_k,ea_cc_d,ea_k,ev_cc_d,ev_k,'Weighted by Diameter',r'$k$','Current Flow Closeness')
    
#fitting_cc_l_and_N()
fitting_cc_d_and_N()
#fitting_cc_l_and_k()
fitting_cc_d_and_k()
#plot_data()
plott.show()

    
    