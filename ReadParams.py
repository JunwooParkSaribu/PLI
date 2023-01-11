import os


def read(path):
    pdb_id=''
    ligand_path=''
    pocket_probability=0
    size_x=''
    size_y=''
    size_z=''
    flex=''
    exhaut=''
    num_modes=''
    energy_range=''

    try:
        readpath = path+'/params.txt'
        with open(readpath, 'r') as f:
            input = f.readlines()
            for i in range(len(input)):
                input[i] = input[i].strip().split('\n')[0]
    except Exception as e:
        print(e)
        print("Err on reading parameters")

    for line in input:
        line = line.strip().split('=')
        param_name = line[0]
        if param_name == 'protein':
            pdb_id = line[-1].strip().split('/')[-1]
            pdb_path = line[-1].strip()
            pdb_path = path + '/' + pdb_path

        if param_name == 'ligand':
            ligand_path = line[-1].strip()
            ligand_path = path + '/' + ligand_path

        if param_name == 'pocket_probability':
            pocket_probability = float(line[-1].strip())

        if param_name == 'size_x':
            size_x = line[-1].split('#')[0].strip()
        if param_name == 'size_y':
            size_y = line[-1].split('#')[0].strip()
        if param_name == 'size_z':
            size_z = line[-1].split('#')[0].strip()
        if param_name == 'flex':
            flex = line[-1].split('#')[0].strip()
            if flex == 'None':
                flex = None
        if param_name == 'exhaustiveness':
            exhaut = line[-1].split('#')[0].strip()
        if param_name == 'num_modes':
            num_modes = line[-1].split('#')[0].strip()
        if param_name == 'energy_range':
            energy_range = line[-1].split('#')[0].strip()

    ligands = []
    try:
        for ligand in os.listdir(ligand_path):
            if ligand.strip().split('.')[-1] == 'sdf':
                ligands.append(ligand)
    except Exception as e:
        print(e)
        print("Err on reading ligands")
    return pdb_id, ligands, pocket_probability, [size_x, size_y, size_z, flex, exhaut, num_modes, energy_range]
