import LoadCode as lc
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def log_fit(xdata,ydata,color,label):
    m,c = np.polyfit(np.log(xdata),np.log(ydata),1)
    xp = np.linspace(min(xdata),max(xdata),100)
    yp = [np.exp(c) * (x**m) for x in xp]
    plt.loglog(xp,yp,color+'-',label=label)

    
#def run(f,title):
ncs_a = []
ncs_x = []
ncs_v = []

ncs_list, earli_list = lc.getNCSAndEARLIIDList()

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG, placenta = lc.getPlacentaNetworks(ncs_id)
    ncs_a.append(max(aG.nodes()))
    ncs_x.append(placenta.Area)
    ncs_v.append(max(vG.nodes()))

ea_a = []
ea_x = []
ea_v = []

#Collate EARLI data
for earli_id in earli_list:
    aG, vG, placenta = lc.getPlacentaNetworks(earli_id)
    ea_a.append(max(aG.nodes()))
    ea_x.append(placenta.Area)
    ea_v.append(max(vG.nodes()))

#plt.plot_ncs_earli_xy(ncs_a,ncs_ax,ncs_v,ncs_vx,ea_a,ea_ax,ea_v,ea_vx,title,xlabel,ylabel)
#plt.plot_ncs_earli_histogram(ncs_a,ncs_v,ea_a,ea_v,title,xlabel)


    
plt.figure()
plt.loglog(ncs_x,ncs_a,'r.',label='NCS A')
#log_fit(ncs_ax,ncs_a,'r','NCS A-Fit')
plt.loglog(ncs_x,ncs_v,'b.',label='NCS V')
#log_fit(ncs_vx,ncs_v,'b','NCS V-Fit')

plt.loglog(ea_x,ea_a,'g.',label='EARLI A')
#log_fit(ea_ax,ea_a,'g','EARLI A-Fit')
plt.loglog(ea_x,ea_v,'k.',label='EARLI V')
#log_fit(ea_vx,ea_v,'k','EARLI V-Fit')

#plt.title(title)
plt.xlabel('Placenta Area')
plt.ylabel('Max Nodes')
plt.legend(loc='best')



'''
plt.figure()
plt.plot(a_gens,a_close,'r.',label='NCS Artery Networks')
plt.plot(v_gens,v_close,'b.',label='NCS Vein Networks')
plt.plot(ea_gens,ea_close,'g.',label='EARLI Artery Networks')
plt.plot(ev_gens,ev_close,'k.',label='EARLI Vein Networks')
plt.xlabel('Maximum Generation Number')
plt.ylabel('Average '+label)
plt.title(label)   
plt.legend(loc='best')

plt.figure()
plt.plot(a_max_node,a_gens,'r.',label='NCS Artery Networks')
plt.plot(v_max_node,v_gens,'b.',label='NCS Vein Networks')
plt.plot(ea_max_node,ea_gens,'g.',label='EARLI Artery Networks')
plt.plot(ev_max_node,ev_gens,'k.',label='EARLI Vein Networks')
plt.legend(loc='best')'''


#run(lambda x : np.mean(nx.closeness_centrality(x).values()),'Closeness')
#run(lambda x : np.mean(nx.katz_centrality(x).values()),'Katz Centrality','Node','Value')
#run(lambda x : np.mean(nx.current_flow_closeness_centrality(x).values()),'Current Flow Closeness')
#run(lambda x : np.mean(nx.betweenness_centrality(x).values()),'Betweenness')
#run(lambda x : np.mean(nx.current_flow_betweenness_centrality(x).values()),'Current Flow Betweenness')
#run(lambda x : np.mean(nx.load_centrality(x).values()),'Load')
plt.show()


    
    