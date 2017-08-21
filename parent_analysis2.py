import LoadCode as lc
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import generations as generations
import plotlib as plott

def get_no_descendants(G,root=None,nodes=None,gen=0):
    if (root == None):    
        root = max(G.nodes())
    if (nodes == None):
        nodes = []
    nodes.append(root)
    children = G.successors(root)
    #nodes.extend(s)
    for child in children:
        gen += 1
        nodes = get_no_descendants(G,root=child,nodes=nodes,gen=gen)
        gen -= 1
    return nodes
    
ncs_list, earli_list = lc.getNCSAndEARLIIDList()
ncs_a = []
ncs_a2 = []
ncs_v = []
ncs_v2 = []
ncs_ax = []
ncs_vx = []
ncs_ax2 = []
ncs_vx2 = []

#Collate NCS data
for ncs_id in ncs_list:
    aG, vG, placenta = lc.getPlacentaNetworks(ncs_id)
    #NCS A Collate
    ncs_a.append(np.mean(aG.out_degree().values()))
    first_gen_nodes = aG.successors(max(aG.nodes()))
    gens , g = generations.get_generations(aG,max(aG.nodes()))
    ncs_ax.append(max(aG.nodes()))
    ncs_ax2.append(max(gens.keys()))
    '''if len(first_gen_nodes) == 2:
        #for node in first_gen_nodes:
        no_of_descendants = get_no_descendants(aG,root=first_gen_nodes[0])
        ratio_of_descendants = len(no_of_descendants)/float(max(aG.nodes()) -1)
        print abs(0.5 - ratio_of_descendants)
        ncs_a2.append(abs(0.5-ratio_of_descendants))
        '''

    #NCS V Collate
    ncs_v.append(np.mean(vG.out_degree().values()))
    gens , g = generations.get_generations(vG,max(vG.nodes()))
    ncs_vx.append(max(vG.nodes()))
    ncs_vx2.append(max(gens.keys()))

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
    earli_a.append(np.mean(np.mean(aG.out_degree().values())))
    earli_ax.append(max(aG.nodes()))
    earli_ax2.append(max(gens.keys()))
    
    #EARLI V Collate
    gens , g = generations.get_generations(vG,max(vG.nodes()))
    earli_v.append(np.mean(np.mean(vG.out_degree().values())))
    earli_vx.append(max(vG.nodes()))
    earli_vx2.append(max(gens.keys()))

scaled = lambda x : [s/float(np.mean(x)) for s in x]
label = r'$\overline{k_{out}}$'
plott.plot_ncs_earli_xy(ncs_a,ncs_ax,ncs_v,ncs_vx,earli_a,earli_ax,earli_v,earli_vx,label,r'$N$',label,scaled=False)
#Try and fit data to get relationship between k_out and N
x = np.linspace(20,250,100)
y = (x-1)/x
plt.plot(x,y,'--m',label=r'$\frac{N-1}{N}$')

#plott.plot_ncs_earli_histogram(ncs_a,ncs_v,earli_a,earli_v,label,label,scaled=False)

#label = r'$^{\overline{k_{out}}} / _{\langle \overline{k_{out}} \rangle}$'
#plott.plot_ncs_earli_xy(ncs_a,ncs_ax,ncs_v,ncs_vx,earli_a,earli_ax,earli_v,earli_vx,label,r'$^N/ _{\langle N \rangle}$',label,scaled=True)
#plott.plot_ncs_earli_histogram(ncs_a,ncs_v,earli_a,earli_v,label,label,scaled=True)
#plott.show()
'''
ncs_a_list = []
ncs_v_list = []
ea_a_list = []
ev_v_list = []

plt.figure()

for i in range(min(ncs_ax2),max(ncs_ax2)+1):
    indices = [s for s,x in enumerate(ncs_ax2) if s == i]
    ncs_a_list.append(np.mean([ncs_a[index] for index in indices]))

y = range(min(ncs_ax2),max(ncs_ax2)+1)
y = [x/float(np.mean(ncs_ax2)) for x in y]
plt.plot(y,ncs_a_list,'r.',label='NCS A')

for i in range(min(ncs_vx2),max(ncs_vx2)+1):
    indices = [s for s,x in enumerate(ncs_vx2) if s == i]
    ncs_v_list.append(np.mean([ncs_v[index] for index in indices]))
y = range(min(ncs_vx2),max(ncs_vx2)+1)
y = [x/float(np.mean(ncs_vx2)) for x in y]
plt.plot(y,ncs_v_list,'b.',label='NCS V')



for i in range(min(earli_ax2),max(earli_ax2)+1):
    indices = [s for s,x in enumerate(earli_ax2) if s == i]
    ea_a_list.append(np.mean([earli_a[index] for index in indices]))
y = range(min(earli_ax2),max(earli_ax2)+1)
y = [x/float(np.mean(earli_ax2)) for x in y]
plt.plot(y,ea_a_list,'g.',label='EARLI A')


for i in range(min(earli_vx2),max(earli_vx2)+1):
    indices = [s for s,x in enumerate(earli_vx2) if s == i]
    ev_v_list.append(np.mean([earli_v[index] for index in indices]))
y = range(min(earli_vx2),max(earli_vx2)+1)
y = [x/float(np.mean(earli_vx2)) for x in y]
plt.plot(y,ev_v_list,'k.',label='EARLI V')

plt.xlabel('Total Gens')
plt.ylabel('Average Branching Ratio Per Gen')
plt.legend(loc='best')
plt.show()

#plt.figure()
#label = 'Avg Branching Prob Per Gen'
#plott.plot_ncs_earli_xy(ncs_a_list,ncs_ax2,ncs_v_list,ncs_vx2,ea_a_list,earli_ax2,ev_v_list,earli_vx2,label,'Total Gens',label)






label = 'Avg Branching Prob'
plott.plot_ncs_earli_histogram(ncs_a,ncs_v,earli_a,earli_v,label,label)

a = [x/float(np.mean(ncs_ax)) for x in ncs_ax]
b = [x/float(np.mean(ncs_vx)) for x in ncs_vx]
c = [x/float(np.mean(earli_ax)) for x in earli_ax]
d = [x/float(np.mean(earli_vx)) for x in earli_vx]

plott.plot_ncs_earli_xy(ncs_a,ncs_ax,ncs_v,ncs_vx,earli_a,earli_ax,earli_v,earli_vx,label,'Total Nodes',label)
plott.plot_ncs_earli_xy(ncs_a,a,ncs_v,b,earli_a,c,earli_v,d,label,'Total Nodes/Mean Nodes',label)

a = [x/float(np.mean(ncs_ax2)) for x in ncs_ax2]
b = [x/float(np.mean(ncs_vx2)) for x in ncs_vx2]
c = [x/float(np.mean(earli_ax2)) for x in earli_ax2]
d = [x/float(np.mean(earli_vx2)) for x in earli_vx2]

plott.plot_ncs_earli_xy(ncs_a,ncs_ax2,ncs_v,ncs_vx2,earli_a,earli_ax2,earli_v,earli_vx2,label,'Total Gens',label)
plott.plot_ncs_earli_xy(ncs_a,a,ncs_v,b,earli_a,c,earli_v,d,label,'Total Gens/Mean Gens',label)
'''

'''
plt.figure()
plt.plot(ncs_ax,ncs_a,'r.',label='NCS Artery')
plt.plot(ncs_vx,ncs_v,'b.',label='NCS Vein')
plt.plot(earli_ax,earli_a,'g.',label='EARLI Artery')
plt.plot(earli_vx,earli_v,'k.',label='EARLI Vein')
plt.xlabel('Max Number of Generations')
plt.ylabel('Average Branching Probability')
plt.legend(loc='best')
plt.show()
'''
    