import subprocess


def conversion(input, output, options=[], pid='', path='', protein_flag=1, gen_ligand=0):
    if gen_ligand == 0:
        if protein_flag == 1:
            path = path + '/data/protein/'
        else:
            path = path + '/data/ligand/'
        if len(options) > 0:
            cmd = ['obabel', path + input, '-O', path + '../../' + output, '---errorlevel', '0']
            for op in options:
                cmd.append(op)
        else:
            cmd = ['obabel', path + input, '-O', path + '../../' + output, '---errorlevel', '0']

    else:
        if len(options) > 0:
            cmd = ['obabel', path + '/' + input, '-O', path + '/gen_ligand/' + output + '/' + pid+'@'+output + '.pdb',
                   '---errorlevel', '0']
            for op in options:
                cmd.append(op)
        else:
            cmd = ['obabel', path + '/' + input, '-O', path + '/gen_ligand/' + output + '/' + pid+'@'+output + '.pdb',
                   '---errorlevel', '0']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    proc.wait()
    return f'{pid}@{output}'

