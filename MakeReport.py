import numpy as np


def write_report(scores, centers, path=''):
    filename = path + '/result/report.csv'
    max1 = 0
    max2 = 0
    rep = {}
    res = []
    for ligand in scores:
        for index, score_dict in enumerate(ligand):
            center = centers[index]
            keys = list(score_dict.keys())
            for key in keys:
                sc = score_dict[key]
                rep[key] = [round(float(sc),3), round(float(center[0]),3), round(float(center[1]),3), round(float(center[2]),3)]

    keys = list(rep.keys())
    for key in keys:
        abc = key.strip().split('@')
        protein = abc[0]
        max1 = max(len(protein), max1)
        proba = abc[1]
        ligand = abc[2]
        max2 = max(len(ligand), max2)
        aaa = [protein, ligand, round(float(proba),3)]
        aaa.extend(rep[key])
        res.append(aaa)

    res = np.array(res)
    order = np.argsort(res[:, 3].astype(float))[::-1]
    res = res[order]

    with open(filename, 'w') as f:
        input_string = ''
        for r in res:
            input_string += f'{r[0] : <{max1+2}}\t{r[1] : <{max2+2}}\t{r[2] : <8}\t' \
                            f'{r[3] : <8}\t{r[4] : <8}\t{r[5] : <8}\t{r[6] : <8}\n'
        f.write(input_string)
        f.close()
