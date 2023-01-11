from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem.Draw import SimilarityMaps
from rdkit.Chem import Descriptors
from rdkit.Chem import rdmolops
from matplotlib import pyplot as plt
import sys
import csv


def prepare_ligand(n_confs, ligands, path=''):
    eosList = list(ligands.keys())

    for i, eos in enumerate(eosList):
        print(f'{i} / {len(eosList)} are generated...')
        mol = Chem.MolFromSmiles(ligands[eos])
        mol = rdmolops.AddHs(mol)
        cids = AllChem.EmbedMultipleConfs(mol, numConfs=n_confs)
        for x in cids:
            try:
                rmslist = []
                AllChem.AlignMolConformers(mol, RMSlist=rmslist)
                res = AllChem.MMFFOptimizeMoleculeConfs(mol)
                with Chem.SDWriter(f'{path}/data/ligand/{eos}_conf{x}.sdf') as w:
                    w.write(mol, confId=x)
            except Exception as e:
                print(e)
                print("f'Err while writing {path}/data/ligand/{eos}_conf{x}.sdf'")



    """ 
    with Chem.SDWriter('molecules/before_optimization.sdf') as w:
        for x in cids: w.write(m1, confId=x)
    """



    # force_field = Chem.rdForceFieldHelpers.UFFGetMoleculeForceField(m2)

    # Draw.MolToFile(m1, '../img/after.png')

"""    with Chem.SDMolSupplier('molecules/after_optimization.sdf') as suppl:
        ms = [x for x in suppl if x is not None]

    img = Draw.MolsToGridImage(ms, molsPerRow=4, subImgSize=(200, 200),
                               legends=[x.GetProp("_Name") for x in ms])
    img.save('img/3D_conformers.png')

    for m in ms:
        print(Chem.MolToMolBlock(m))

    p = Chem.MolFromSmiles('[nH]1cnc2cncnc21')
    subms = [x for x in ms if x.HasSubstructMatch(p)]

    AllChem.Compute2DCoords(p)"""

"""    
    for m in subms: AllChem.GenerateDepictionMatching2DStructure(m, p)
    img = Draw.MolsToGridImage(subms, molsPerRow=4, subImgSize=(200, 200), legends=[x.GetProp("_Name")for x in subms])
    img.save('img/aligned_2D_conformers.png')
    """


"""    AllChem.ComputeGasteigerCharges(ms[0])
    contribs = rdMolDescriptors._CalcCrippenContribs(ms[0])
    fig = (SimilarityMaps.GetSimilarityMapFromWeights(ms[0], [x for x,y in contribs], colorMap='jet', contourLines=10,
                                                       size=(750,750), coordScale=1))
    plt.savefig("img/Gasteiger_partial_charges.png", bbox_inches='tight', dpi=100)"""


def read_ligand_list(path):
    fileName = path + '/pilot_library2.csv'
    ligands = {}
    with open(fileName, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ligands[row['eos']] = row['smiles']
    return ligands


if __name__ == '__main__':
    path = '.'
    if len(sys.argv) > 1:
        n_confs = sys.argv[1]
    else:
        n_confs = 1

    ligands = read_ligand_list('data/5000ligand_list')
    prepare_ligand(n_confs, ligands, path)
