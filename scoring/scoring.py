import subprocess
import re
import scoring.model_select as m


def parse_score(model, receptor, ligand, plid='', path=''):
    scores = {}
    #print('scoring path : ', os.getcwd())  # /Users/junwoopark/Desktop/Junwoo/Faculty/Master/M2/MEETU/2022--2023-SU-Team3
    model = path + '/scoring/./' + model
    receptor = path + '/data/protein/' + receptor
    ligand = path + '/gen_ligand/' + ligand + '/' + plid + '.pdb'
    ligands, nb_ligands = m.read_pdb(ligand)
    for ligand_model in ligands:
        ligand_name = re.split('/', ligand_model)[-1]

        cmd = [model, "--receptor", receptor, "--ligand", ligand_model]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        proc.wait()

        for line in proc.stdout:
            model_score = str(line)

        vals = re.split("\ ", model_score[1:-1])
        score = re.split('\\\\', vals[4])[0]
        scores[ligand_name] = score
    return scores
