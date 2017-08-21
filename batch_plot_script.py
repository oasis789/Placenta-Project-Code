import networkx as nx
import LoadCode as lc
import matplotlib.pyplot as plt
import plot_tree_graph as plt_tree
import os

loc = os.path.normpath("C:/Users/Uwais/Google Drive/Uni/MSc Project/My Code/figs/")
placentas = lc.loadAllPlacentasfromdir()
for ID,placenta in placentas.iteritems():
    #ID = placenta.ID
    print 'Plotting:', ID
    anetwork = placenta.getArteryNetwork()
    vnetwork = placenta.getVeinNetwork()
    aG = nx.from_dict_of_lists(anetwork.getChildren())
    vG = nx.from_dict_of_lists(vnetwork.getChildren())
    apos = plt_tree.linear_equidistant_plot(aG,anetwork.getChildren().keys()[-1])
    vpos = plt_tree.linear_equidistant_plot(vG,vnetwork.getChildren().keys()[-1])
    
    plt.figure()
    nx.draw(aG,pos=apos,alpha=0.6,node_size=20)
    plt.savefig(os.path.join(loc,ID+'-A'+'.png'))
    plt.close()
    
    plt.figure()
    nx.draw(vG,pos=vpos,alpha=0.6,node_size=20)
    plt.savefig(os.path.join(loc,ID+'-V'+'.png'))
    plt.close()

 
    
    
    
    
    