import pandas as pd


def read_pocket(pdb_name, probaility=0.5, path=''):
    path = path + '/result/pockets/'
    file_name = path + pdb_name + '/' + pdb_name + '.pdb_predictions.csv'

    with open(file_name, 'r') as f:
        predictions = pd.read_csv(f, header=None)

    proba = predictions[3]
    center_x = predictions[6]
    center_y = predictions[7]
    center_z = predictions[8]
    pockets = []

    for i in range(1, len(proba)):
        if float(proba[i]) > probaility:
            pockets.append([proba[i].strip(), center_x[i].strip(), center_y[i].strip(), center_z[i].strip()])
    return pockets

