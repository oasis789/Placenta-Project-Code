import LoadCode as lc
import matplotlib.pyplot as plt
import generations as g
import numpy as np

ncs_list, earli_list = lc.getNCSAndEARLIIDList()
#Collate NCS data
ncs_max_gens = 20
a_gens = {k:0 for k in range(ncs_max_gens+1)}
v_gens = {k:0 for k in range(ncs_max_gens+1)}
ncs_a = []
ncs_v = []
for ncs_id in ncs_list:
    aG, vG, p = lc.getPlacentaNetworks(ncs_id)
    gs,x = g.get_generations(aG,max(aG.nodes()))
    #print a_g
    for gen, nodes in gs.iteritems():
        a_gens[gen] += len(nodes)
    ncs_a.append(max(gs.keys()))
    gs,x = g.get_generations(vG,max(vG.nodes()))
    for gen, nodes in gs.iteritems():
            v_gens[gen] += len(nodes)
    ncs_v.append(max(gs.keys()))

ncs_a = [k/float(len(ncs_list)) for k in a_gens.values()]
ncs_v = [k/float(len(ncs_list)) for k in v_gens.values()]

earli_max_gens = 20
a_gens = {k:0 for k in range(ncs_max_gens+1)}
v_gens = {k:0 for k in range(ncs_max_gens+1)}
ea_a = []
ea_v = []
for earli_id in earli_list:
    aG, vG, p = lc.getPlacentaNetworks(earli_id)
    gs,x = g.get_generations(aG,max(aG.nodes()))
    #print a_g
    for gen, nodes in gs.iteritems():
        a_gens[gen] += len(nodes)
    ea_a.append(max(gs.keys()))
    gs,x = g.get_generations(vG,max(vG.nodes()))
    for gen, nodes in gs.iteritems():
            v_gens[gen] += len(nodes)
    ea_v.append(max(gs.keys()))

earli_a = [k/float(len(earli_list)) for k in a_gens.values()]
earli_v = [k/float(len(earli_list)) for k in v_gens.values()]


    
print ncs_a
#print ncs_v
plt.figure()
plt.plot(range(len(ncs_a)),ncs_a,'r.--',label='NCS Artery')
plt.plot(range(len(ncs_v)),ncs_v,'b.--',label='NCS Vein')
plt.plot(range(len(earli_a)),earli_a,'g.--',label='EARLI Artery')
plt.plot(range(len(earli_v)),earli_v,'k.--',label='EARLI Vein')
plt.xlabel('Generation Number')
plt.ylabel('Avg Nodes Per Generation')
plt.legend(loc='best')
plt.show()


    
