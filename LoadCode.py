import glob, os
import pickle
import gzip
import networkx as nx
import placenta 

def loadAllPlacentasfromdir(loc = 'C:\Users\Uwais\Google Drive\Uni\MSc Project\My Code\data\*.pic.gz'):
    '''Loads and recovers all pickled placentas into a dictionary'''
    pyplacentas = {}
    files = glob.glob(loc)
    for x in files:
        print "Loading file:", x
        ID = os.path.basename(x).split(".")[0]
        pyplacentas[ID] = pickle.load(gzip.open(x, 'rb'))
    return pyplacentas

def loadSinglePlacentafromdir(ID, loc = 'C:\Users\Uwais\Google Drive\Uni\MSc Project\My Code\data'):
    '''Loads and recovers a single specified pickled placenta'''
    filename = os.path.join(loc,ID +'.pic.gz')
    print "Loading file:", filename
    placenta = pickle.load(gzip.open(filename, 'rb')) 
    return placenta

def getNCSAndEARLIIDList():
    loc = os.path.normpath("C:/Users/Uwais/Google Drive/Uni/MSc Project/My Code/")
    ncs_f = os.path.join(loc,'NCS-list')
    earli_f = os.path.join(loc,'EARLI-list')
    with open(ncs_f,'rb') as f:
        ncs_list = pickle.load(f)
    with open(earli_f,'rb') as f:
        earli_list = pickle.load(f)
    return ncs_list, earli_list

def getPlacentaNetworks(ID):
    '''Loads specified placenta with given ID and returns the artery and vein network as a nx graph object'''
    placenta = loadSinglePlacentafromdir(ID)
    artery_network = placenta.getArteryNetwork()
    vein_network = placenta.getVeinNetwork()
    artery_G = nx.DiGraph(artery_network.getChildren())
    #artery_G = nx.from_dict_of_lists(artery_network.getChildren())
    #vein_G = nx.from_dict_of_lists(vein_network.getChildren())
    vein_G = nx.DiGraph(vein_network.getChildren())
    return artery_G, vein_G, placenta
    
'''def getPlacentaNetworks(placenta):
    ''''''Loads specified placenta and returns the artery and vein network as a nx graph object''''''
    artery_network = placenta.getArteryNetwork()
    vein_network = placenta.getVeinNetwork()
    artery_G = nx.from_dict_of_lists(artery_network.getChildren())
    vein_G = nx.from_dict_of_lists(vein_network.getChildren())
    return artery_G, vein_G'''
