import subprocess


def docking(receptor, ligand, x, y, z, output, docking_params=['20', '20', '20', None, '8', '9', '3'], path='', model='vina'):
    print(f'Docking {ligand} with {receptor}...\n')
    model = './' + model
    model_path = path + '/docking/'
    path = path + '/'
    size_x = str(docking_params[0])
    size_y = str(docking_params[1])
    size_z = str(docking_params[2])
    flex = docking_params[3]
    exhaut = str(docking_params[4])
    num_mode = str(docking_params[5])
    energy_range = str(docking_params[6])

    if flex is not None:
        cmd = [model_path + model, '--receptor', path + receptor, '--ligand', path + ligand, '--out', path+'/' + output,
               '--center_x', x, '--center_y', y, '--center_z', z, '--size_x', size_x, '--size_y', size_y, '--size_z', size_z,
               '--flex', path + flex, '--exhaustiveness', exhaut, '--num_modes', num_mode, '--energy_range', energy_range]
    else:
        cmd = [model_path + model, '--receptor', path + receptor, '--ligand', path + ligand, '--out', path+'/' + output,
               '--center_x', x, '--center_y', y, '--center_z', z, '--size_x', size_x, '--size_y', size_y, '--size_z',
               size_z, '--exhaustiveness', exhaut, '--num_modes', num_mode, '--energy_range', energy_range]

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    proc.wait()
