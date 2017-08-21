import LoadCode as lc
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import generations as generations
import plotlib as plott

ncs_list, earli_list = lc.getNCSAndEARLIIDList()
ncs_a = []
ncs_v = []
ncs_ax = []
ncs_vx = []
ncs_ax2 = []
ncs_vx2 = []

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG, placenta = lc.getPlacentaNetworks(ncs_id)
    #NCS A Collate
    gens , g = generations.get_generations(aG,max(aG.nodes()))
    ncs_a.append(sum(g.values())/float(max(aG.nodes())))
    ncs_ax.append(max(aG.nodes()))
    ncs_ax2.append(max(g.values()))
    
    #NCS V Collate
    gens , g = generations.get_generations(vG,max(vG.nodes()))
    ncs_v.append(sum(g.values())/float(max(vG.nodes())))
    ncs_vx.append(max(vG.nodes()))
    ncs_vx2.append(max(g.values()))

earli_a = []
earli_v = []
earli_ax = []
earli_vx = []
earli_ax2 = []
earli_vx2 = []

#Collate EARLI data
for earli_id in earli_list:
    aG, vG, placenta = lc.getPlacentaNetworks(earli_id)
    #EARLI A Collate
    gens , g = generations.get_generations(aG,max(aG.nodes()))
    earli_a.append(sum(g.values())/float(max(aG.nodes())))
    earli_ax.append(max(aG.nodes()))
    earli_ax2.append(max(gens.keys()))
    
    #EARLI V Collate
    gens , g = generations.get_generations(vG,max(vG.nodes()))
    earli_v.append(sum((g.values()))/float(max(vG.nodes())))
    earli_vx.append(max(vG.nodes()))
    earli_vx2.append(max(gens.keys()))

label='Sum G'
plott.plot_ncs_earli_xy(ncs_a,[x/float(np.mean(ncs_ax)) for x in ncs_ax],ncs_v,[x/float(np.mean(ncs_vx)) for x in ncs_vx],earli_a,[x/float(np.mean(earli_ax)) for x in earli_ax],earli_v,[x/float(np.mean(earli_vx)) for x in earli_vx],label,'Total Nodes',label)
plott.plot_ncs_earli_histogram(ncs_a,ncs_v,earli_a,earli_v,'Sum G','Sum G')
plott.show()

    