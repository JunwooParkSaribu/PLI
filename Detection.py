import subprocess
import os


def detect(pdb_id, pdb_name, path=''):
    print(f'\nDetecting pockets in {pdb_id}...')
    path = path + '/detection/distro'
    os.chdir(path)
    cmd = ['./prank', 'predict', '-f', '../../data/protein/'+pdb_id, '-o', '../../result/pockets/'+pdb_name]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    proc.wait()
    os.chdir('../..')
