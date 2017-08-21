'''Script to save the IDs for the NCS and EARLI placentas
seperately in a pickle file'''
import os
import LoadCode as lc
import pickle

loc = os.path.normpath("C:/Users/Uwais/Google Drive/Uni/MSc Project/My Code/")
ncs_f = os.path.join(loc,'NCS-list')
earli_f = os.path.join(loc,'EARLI-list')

placentas = lc.loadAllPlacentasfromdir()
ncs_list = []
earli_list = []
ID_list = placentas.keys()
for ID in ID_list:
    if ID[0] == 'B':
        ncs_list.append(ID)
    else:
        earli_list.append(ID)

with open(ncs_f, 'wb') as f:
    pickle.dump(ncs_list,f)
    
with open(earli_f, 'wb') as f:
    pickle.dump(earli_list,f)


