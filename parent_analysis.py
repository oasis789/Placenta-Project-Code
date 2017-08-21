import LoadCode as lc
import numpy as np
import matplotlib.pyplot as plt
import generations as generations
import plotlib as plott

ncs_a_max_gens = 18
ncs_v_max_gens = 20
ncs_a_data = [[] for i in range(ncs_a_max_gens+1)]
ncs_v_data = [[] for i in range (ncs_v_max_gens+1)]
ncs_list, earli_list = lc.getNCSAndEARLIIDList()
ncs_a_data2 = [[] for i in range(ncs_a_max_gens)]
ncs_v_data2 = [[] for i in range (ncs_v_max_gens)]

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG, placenta = lc.getPlacentaNetworks(ncs_id)
    #NCS A Collate
    gens , g = generations.get_generations(aG,max(aG.nodes()))
    parents = generations.get_parent_per_gen(aG,max(aG.nodes()),ncs_a_max_gens+1)
    parents = [p/float(len(n)) for p,n in zip(parents,gens.values())]
    parent_diff = [parents[i] - parents[i+1] for i in range(len(parents) - 1)]
    for i,parent in enumerate(parents):
        ncs_a_data[i].append(parent)
    for i,s in enumerate(parent_diff):
        ncs_a_data2[i].append(s)
    
    #NCS V Collate
    gens , g = generations.get_generations(vG,max(vG.nodes()))
    parents = generations.get_parent_per_gen(vG,max(vG.nodes()),ncs_v_max_gens+1)
    parents = [p/float(len(n)) for p,n in zip(parents,gens.values())]
    parent_diff = [parents[i] - parents[i+1] for i in range(len(parents) - 1)]
    for i,parent in enumerate(parents):
        ncs_v_data[i].append(parent)
    for i,s in enumerate(parent_diff):
        ncs_v_data2[i].append(s)

earli_a_max_gens = 14
earli_v_max_gens = 16
earli_a_data = [[] for i in range(earli_a_max_gens+1)]
earli_v_data = [[] for i in range(earli_v_max_gens+1)]
earli_a_data2 = [[] for i in range(earli_a_max_gens)]
earli_v_data2 = [[] for i in range(earli_v_max_gens)]

#Collate EARLI data
for earli_id in earli_list:
    aG, vG, placenta = lc.getPlacentaNetworks(earli_id)
    #EARLI A Collate
    gens , g = generations.get_generations(aG,max(aG.nodes()))
    parents = generations.get_parent_per_gen(aG,max(aG.nodes()),earli_a_max_gens)
    parents = [p/float(len(n)) for p,n in zip(parents,gens.values())]
    parent_diff = [parents[i] - parents[i+1] for i in range(len(parents) - 1)]
    for i,parent in enumerate(parents):
        earli_a_data[i].append(parent)
    for i,s in enumerate(parent_diff):
        earli_a_data2[i].append(s)
        
    #EARLI V Collate
    gens , g = generations.get_generations(vG,max(vG.nodes()))
    parents = generations.get_parent_per_gen(vG,max(vG.nodes()),earli_v_max_gens)
    parents = [p/float(len(n)) for p,n in zip(parents,gens.values())]
    parent_diff = [parents[i] - parents[i+1] for i in range(len(parents) - 1)]
    for i,parent in enumerate(parents):
        earli_v_data[i].append(parent)
    for i,s in enumerate(parent_diff):
        earli_v_data2[i].append(s)

plt.figure()
plt.plot(range(ncs_a_max_gens+1),[np.mean(data) for data in ncs_a_data],'r.',label='NCS Artery')
plt.plot(range(ncs_v_max_gens+1),[np.mean(data) for data in ncs_v_data],'b.',label='NCS Vein')
plt.plot(range(earli_a_max_gens+1),[np.mean(data) for data in earli_a_data],'g.',label='EARLI Artery')
plt.plot(range(earli_v_max_gens+1),[np.mean(data) for data in earli_v_data],'k.',label='EARLI Vein')
plt.xlabel('Generation Number')
plt.ylabel('Average Parent Probability')
plt.legend(loc='best')

plt.figure()
plt.plot(range(ncs_a_max_gens+1),[np.std(data) for data in ncs_a_data],'r.',label='NCS Artery')
plt.plot(range(ncs_v_max_gens+1),[np.std(data) for data in ncs_v_data],'b.',label='NCS Vein')
plt.plot(range(earli_a_max_gens+1),[np.std(data) for data in earli_a_data],'g.',label='EARLI Artery')
plt.plot(range(earli_v_max_gens+1),[np.std(data) for data in earli_v_data],'k.',label='EARLI Vein')
plt.xlabel('Generation Number')
plt.ylabel('Std Dev Parent Probability')
plt.legend(loc='best')

plt.figure()
plt.plot(range(1,ncs_a_max_gens+1),[np.mean(data) for data in ncs_a_data2],'r.',label='NCS Artery')
plt.plot(range(1,ncs_v_max_gens+1),[np.mean(data) for data in ncs_v_data2],'b.',label='NCS Vein')
plt.plot(range(1,earli_a_max_gens+1),[np.mean(data) for data in earli_a_data2],'g.',label='EARLI Artery')
plt.plot(range(1,earli_v_max_gens+1),[np.mean(data) for data in earli_v_data2],'k.',label='EARLI Vein')
plt.xlabel('Generation Number')
plt.ylabel('Delta Parent Probability')
plt.legend(loc='best')


plt.show()


    
    