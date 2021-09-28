import numpy as np
import math
import Esercitazione_1.parte_1.correlation as corr
def cos_simil(v1,v2):
    num = np.dot(v1,v2)
    denom = norm(v1)*norm(v2)
    return num/denom


def norm(v):
    result = 0
    for elem in v:
        result+= elem**2
    return math.sqrt(result)

def calc_max(w1,w2):
    val_max = 0
    w1_elems = terms.get(w1)
    w2_elems = terms.get(w2)
    if w1_elems and w2_elems:
        for elem1 in w1_elems:
            for elem2 in w2_elems:
                val_max = max(cos_simil(data.get(elem1),data.get(elem2)),val_max) if data.get(elem1) and data.get(elem2) else val_max
    return val_max

nasari_file = open('utils/mini_NASARI.tsv', 'r')
gold_file = open('annotation.txt', 'r')
trans_file = open('utils/SemEval17_IT_senses2synsets.txt', 'r')
Lines = nasari_file.readlines()
goldLines = gold_file.readlines()
transLines = trans_file.readlines()
data = {}
gold = []
terms = {}
local = []
key = ""
for line in Lines:
    if(line != '\n'):
        l = line.split("\t")
        data[l[0].split("_")[0]] = list(map(float, l[1:]))

for line in goldLines:
    if(line != '\n'):
        l = line[:len(line)-1].split("\t")
        gold.append(l)

for line in transLines:
    if(line[0] == '#'):
        if len(local) != 0:
            terms[key] = local
        local = []
        key = line[1:len(line)-1]
    else:
        local.append(line[:len(line)-1])

result = []
for elem in gold:
    result.append(calc_max(elem[0],elem[1]))

check_gold = list(map(lambda x: float(x[2]),gold))
pearson = corr.pearson(result,check_gold)
spearman = corr.rank_spear(result,check_gold)
print("Pippo")


