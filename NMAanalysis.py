from prody import *
from pylab import *

save_path = './NMA'
protein_name = '7nn0_chainA.pdb'
protein_path = 'data/protein/'+protein_name
protein = parsePDB(protein_path)

# 'protein and name CA'
selected_atoms = protein.select('all')

anm = ANM(protein_name+' ANM analysis')
anm.buildHessian(selected_atoms)
anm.calcModes()
writeNMD(save_path + '/' + protein_name + '_anm_modes.nmd', anm[:5], selected_atoms)
