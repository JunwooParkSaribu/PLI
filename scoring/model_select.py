import re


def read_pdb(pdb):
    file_content = ''
    index = 0
    models = []

    with open(pdb) as input_file:
        input = input_file.read()
    lines = input.strip().split('\n')

    for file_line_n in range(len(lines)):
        file_content += lines[file_line_n]
        file_content += '\n'

        if re.split('\ ',lines[file_line_n])[0] == 'ENDMDL':
            models.append(write_seperated_models(file_content, pdb, index))
            file_content = ''
            index += 1

    return models, index


def write_seperated_models(content, pdb, index):
    filename = re.split('\.', pdb)[0] + '.' + re.split('\.', pdb)[1]
    filename = filename + '_'+str(index)+'.pdb'
    with open(filename, 'w') as file:
        file.write(content)
    return filename
