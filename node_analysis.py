import LoadCode as lc
import networkx as nx
import numpy as np
import generations as gens
import plotlib as plt

ncs_a = []
ncs_a2 = []
ncs_a3 = []
ncs_ax = []
ncs_v = []
ncs_v2 = []
ncs_v3 = []
ncs_vx = []

ncs_list, earli_list = lc.getNCSAndEARLIIDList()

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG,p = lc.getPlacentaNetworks(ncs_id)
    gs,x = gens.get_generations(aG,max(aG.nodes()))
    ncs_a.append(max(gs.keys()))
    ncs_ax.append(max(aG.nodes()))
    ncs_a2.append(max(aG.nodes())/float(max(gs.keys())))
    ncs_a3.append(aG.degree(max(aG.nodes())))
    gs,x = gens.get_generations(vG,max(vG.nodes()))
    ncs_v.append(max(gs.keys()))
    ncs_vx.append(max(vG.nodes()))
    ncs_v2.append(max(vG.nodes())/float(max(gs.keys())))
    ncs_v3.append(vG.degree(max(vG.nodes())))


ea_a = []
ea_a2 = []
ea_a3 = []
ea_ax = []
ea_v = []
ea_v2 = []
ea_v3 = []
ea_vx = []

#Collate EARLI data
for earli_id in earli_list:
    aG, vG, p = lc.getPlacentaNetworks(earli_id)
    gs,x = gens.get_generations(aG,max(aG.nodes()))
    ea_a.append(max(gs.keys()))
    ea_ax.append(max(aG.nodes()))
    ea_a2.append(max(aG.nodes())/float(max(gs.keys())))
    ea_a3.append(aG.degree(max(aG.nodes())))
    gs,x = gens.get_generations(vG,max(vG.nodes()))
    ea_v.append(max(gs.keys()))
    ea_vx.append(max(vG.nodes()))
    ea_v2.append(max(vG.nodes())/float(max(gs.keys())))
    ea_v3.append(vG.degree(max(vG.nodes())))


'''
plt.plot(ncs_ax,ncs_a,'r.',label='NCS A')
plt.plot(ncs_vx,ncs_v,'b.',label='NCS V')
plt.plot(ea_ax,ea_a,'g.',label='EARLI A')
plt.plot(ea_vx,ea_v,'k.',label='EARLI V')
plt.xlabel('Total Nodes')
plt.ylabel(label)
plt.title(label)
plt.legend(loc='best')   
'''

plt.plot_ncs_earli_histogram(ncs_ax,ncs_vx,ea_ax,ea_vx,'',r'$N$')
plt.plot_ncs_earli_histogram(ncs_ax,ncs_vx,ea_ax,ea_vx,'Scaled',r'$^N / _{\langle N \rangle}$',scaled=True)
plt.plot_ncs_earli_histogram(ncs_a,ncs_v,ea_a,ea_v,'',r'$G$')
plt.plot_ncs_earli_histogram(ncs_a,ncs_v,ea_a,ea_v,'Scaled',r'$^G / _{\langle G \rangle} $',scaled=True)

plt.plot_ncs_earli_histogram(ncs_a2,ncs_v2,ea_a2,ea_v2,'',r'$d_{g} = ^N/_G$')
plt.plot_ncs_earli_histogram(ncs_a2,ncs_v2,ea_a2,ea_v2,'Scaled',r'$^{d_{g}} / _{\langle d_{g} \rangle}$',scaled=True)

plt.plot_ncs_earli_xy(ncs_a3,ncs_ax,ncs_v3,ncs_vx,ea_a3,ea_ax,ea_v3,ea_vx,'','Total Nodes','Root Children',scaled=False)
plt.plot_ncs_earli_histogram(ncs_a3,ncs_v3,ea_a3,ea_v3,'Root Children','Root Children')

'''
plt.plot_ncs_earli_xy(ncs_a2,ncs_ax,ncs_v2,ncs_vx,ea_a2,ea_ax,ea_v2,ea_vx,'','Total Nodes','Generation Density',scaled=False)

plt.plot_ncs_earli_xy(ncs_a2,ncs_ax,ncs_v2,ncs_vx,ea_a2,ea_ax,ea_v2,ea_vx,'','Total Nodes Scaled','Generation Density',scaled=True)


'''

'''

a = [x/float(y) for x,y in zip(ncs_ax,ncs_a)]
b = [x/float(y) for x,y in zip(ncs_vx,ncs_v)]
c = [x/float(y) for x,y in zip(ea_ax,ea_a)]
d = [x/float(y) for x,y in zip(ea_vx,ea_v)]

plt.plot_ncs_earli_histogram(a,b,c,d,'Generation Density','Generation Density')

a = [x/float(np.mean(ncs_ax)) for x in ncs_ax]
b = [x/float(np.mean(ncs_vx)) for x in ncs_vx]
c = [x/float(np.mean(ea_ax)) for x in ea_ax]
d = [x/float(np.mean(ea_vx)) for x in ea_vx]

plt.plot_ncs_earli_histogram(a,b,c,d,'Scaled Generations','Total Nodes/Mean Nodes')


'''
plt.show()


    