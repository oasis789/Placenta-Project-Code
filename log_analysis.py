import LoadCode as lc
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def log_fit(xdata,ydata,color,label):
    m,c = np.polyfit(np.log(xdata),np.log(ydata),1)
    xp = np.linspace(min(xdata),max(xdata),100)
    yp = [np.exp(c) * (x**m) for x in xp]
    plt.loglog(xp,yp,color+'-',label=label)
    return m,c

    
def run(f,title):
    ncs_a = []
    ncs_ax = []
    ncs_v = []
    ncs_vx = []
    
    ncs_list, earli_list = lc.getNCSAndEARLIIDList()
    
    #Collate NCS data
    for ncs_id in ncs_list:
        aG, vG, p = lc.getPlacentaNetworks(ncs_id)
        ncs_a.append(f(aG))
        ncs_ax.append(max(aG.nodes()))
        ncs_v.append(f(vG))
        ncs_vx.append(max(vG.nodes()))
    
    ea_a = []
    ea_ax = []
    ea_v = []
    ea_vx = []
    
    #Collate EARLI data
    for earli_id in earli_list:
        aG, vG, p = lc.getPlacentaNetworks(earli_id)
        ea_a.append(f(aG))
        ea_ax.append(max(aG.nodes()))
        ea_v.append(f(vG))
        ea_vx.append(max(vG.nodes()))
    
    b_a = []
    b_ax = []
    #Collate Perfect Tree Data
    for i in range(3,9):
        aG = nx.balanced_tree(2,i)
        b_a.append(f(aG))
        b_ax.append(max(aG.nodes()))


    plt.figure()
    plt.loglog(ncs_ax,ncs_a,'r.',label='NCS A')
    log_fit(ncs_ax,ncs_a,'r','NCS A-Fit')
    plt.loglog(ncs_vx,ncs_v,'b.',label='NCS V')
    log_fit(ncs_vx,ncs_v,'b','NCS V-Fit')
    
    plt.loglog(ea_ax,ea_a,'g.',label='EARLI A')
    log_fit(ea_ax,ea_a,'g','EARLI A-Fit')
    plt.loglog(ea_vx,ea_v,'k.',label='EARLI V')
    log_fit(ea_vx,ea_v,'k','EARLI V-Fit')

    plt.loglog(b_ax,b_a,'m.',label='Tree')
    log_fit(b_ax,b_a,'m','Tree Fit')
    
    plt.title(title)
    plt.xlabel('Maximum Number of Nodes')
    plt.ylabel('Average ' + title)
    plt.legend(loc='best')


run(lambda x : np.mean(nx.closeness_centrality(x).values()),'Closeness')
#run(lambda x : np.mean(nx.katz_centrality(x).values()),'Katz Centrality','Node','Value')
run(lambda x : np.mean(nx.current_flow_closeness_centrality(x).values()),'Current Flow Closeness')
run(lambda x : np.mean(nx.betweenness_centrality(x).values()),'Betweenness')
run(lambda x : np.mean(nx.current_flow_betweenness_centrality(x).values()),'Current Flow Betweenness')
run(lambda x : np.mean(nx.load_centrality(x).values()),'Load')
run(lambda x : np.mean(nx.communicability_centrality(x).values()),'Communicability')
plt.show()


    
    