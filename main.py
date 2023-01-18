import sys
import re
import os
import Detection
import ReadPockets
import Conversion
import Docking
import ReadParams
import MakeReport
from scoring import scoring as sc


def pipe_main(protein, pockets, ligand, docking_params, path) -> []:
    platform = sys.platform
    if platform.lower() == 'darwin':
        docking_model = 'vina'
        scoring_model = 'Convex-PL'
    else:
        docking_model = 'vina_linux'
        scoring_model = 'Convex-PL_linux'
    scores = []
    pockets_center = []
    ligand_name = re.split('\.', ligand)[0]
    protein_name = re.split('\.', protein)[0]

    try:
        if ligand_name not in os.listdir(path+'/gen_ligand/'):
            os.mkdir(path+'/gen_ligand/'+ligand_name)
    except Exception as e:
        print('Error while creating the gen_ligand directory')
        print(e)

    Conversion.conversion(protein, protein_name + '.pdbqt', options=['-p', '7.4', '-xr'], path=path, protein_flag=1)
    Conversion.conversion(ligand, ligand_name + '.pdbqt', path=path, protein_flag=0)

    for pocket in pockets:
        pockets_center.append([pocket[1], pocket[2], pocket[3]])
        Docking.docking(receptor=protein_name + '.pdbqt', ligand=ligand_name + '.pdbqt', x=pocket[1],
                        y=pocket[2], z=pocket[3], output='ligand_vina_'+pocket[0]+'.pdbqt',
                        docking_params=docking_params, path=path, model=docking_model)
        p_lid = Conversion.conversion('ligand_vina_'+pocket[0]+'.pdbqt', ligand_name, pid=protein_name+'@'+pocket[0],
                                      path=path, gen_ligand=1)
        scores.append(sc.parse_score(model=scoring_model, receptor=protein, ligand=ligand_name, plid=p_lid, path=path))

    try:
        for pocket in pockets:
            ligand_pdbqt = 'ligand_vina_'+pocket[0]+'.pdbqt'
            if ligand_pdbqt in os.listdir(path):
                os.remove(ligand_pdbqt)
        if protein_name + '.pdbqt' in os.listdir(path):
            os.remove(protein_name + '.pdbqt')
        if ligand_name + '.pdbqt' in os.listdir(path):
            os.remove(ligand_name + '.pdbqt')
    except Exception as e:
        print('Error while deleting the files')
        print(e)
    return scores, pockets_center


def pocket_detection(protein, probability=0.5, path=''):
    protein_name = re.split('\.', protein)[0]
    try:
        if protein_name not in os.listdir(path+'/result/pockets/'):
            os.mkdir(path+'/result/pockets/'+protein_name)
    except Exception as e:
        print('Error while creating the pocket directory')
        print(e)
    Detection.detect(protein, protein_name, path=path)
    pockets = ReadPockets.read_pocket(protein_name, probaility=probability, path=path)
    return pockets


if __name__ == '__main__':
    path = "."
    scores = []
    if len(sys.argv) > 1:
        path = sys.argv[1]
    print(f"\nCurrent running path:{path}")
    pdb_id, ligands, pocket_proba, docking_params = ReadParams.read(path)
    pockets = pocket_detection(pdb_id, probability=pocket_proba, path=path)
    print(f'{len(pockets)} pockets are detected...')
    for i, ligand in enumerate(ligands):
        print(f'Docking on {i} / {len(ligands)} ligands...')
        # todo
        # check if ligand is single-model file
        score, centers = pipe_main(pdb_id, pockets, ligand, docking_params, path)
        scores.append(score)
    MakeReport.write_report(scores, centers, path=path)
