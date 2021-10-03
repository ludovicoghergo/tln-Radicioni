import numpy as np
import math
import Esercitazione_1.parte_1.correlation as corr
from sklearn.metrics import cohen_kappa_score
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
    max_elem1 = "None"
    max_elem2 = "None"
    w1_elems = terms.get(w1)
    w2_elems = terms.get(w2)
    if w1_elems and w2_elems:
        for elem1 in w1_elems:
            for elem2 in w2_elems:
                if data.get(elem1) and data.get(elem2):
                    temp = cos_simil(data.get(elem1), data.get(elem2))
                    if temp > val_max:
                        max_elem1 = elem1
                        max_elem2 = elem2
                        val_max = temp
    return val_max,max_elem1,max_elem2

nasari_file = open('utils/mini_NASARI.tsv', 'r', encoding="utf8")
gold_file = open('annotation.txt', 'r')
gold_file2 = open('annotation2.txt', 'r')
trans_file = open('utils/SemEval17_IT_senses2synsets.txt', 'r')
terms_file = open('utils/babelnet_termini.txt', 'r')
Lines = nasari_file.readlines()
goldLines = gold_file.readlines()
goldLines2 = gold_file2.readlines()
transLines = trans_file.readlines()
termsLines = terms_file.readlines()
data = {}
gold = []
gold2 = []
terms = {}
local = []
terms_out = {}
key = ""

for line in termsLines:
    if(line != '\n'):
        l = line.split("\t")
        terms_out[l[0]] = l[1].rstrip()

for line in Lines:
    if(line != '\n'):
        l = line.split("\t")
        data[l[0].split("_")[0]] = list(map(float, l[1:]))

for line in goldLines:
    if(line != '\n'):
        l = line[:len(line)-1].split("\t")
        gold.append(l)

for line in goldLines2:
    if(line != '\n'):
        l = line[:len(line)-1].split("\t")
        gold2.append(l)

for line in transLines:
    if(line[0] == '#'):
        if len(local) != 0:
            terms[key] = local
        local = []
        key = line[1:len(line)-1]
    else:
        local.append(line[:len(line)-1])

result = []
output = []
output2 = []
name_list = []
name_list2 = []
for elem in gold:
    num_val,elem_1,elem_2 = calc_max(elem[0],elem[1])
    result.append(num_val)
    name_list.append(elem_1)
    name_list2.append(elem_2)
    if elem_1 == "None" or elem_2 == "None":
        output.append([elem[0], elem[1], elem_1, elem_2, "None", "None"])
    else:
        output.append([elem[0],elem[1],elem_1,elem_2,terms_out[elem_1],terms_out[elem_2]])
    output2.append([elem[0],elem[1],num_val])

name_list = name_list + name_list2
check_gold = list(map(lambda x: float(x[2]),gold))
check_gold2 = list(map(lambda x: float(x[2]),gold2))

# È ordinato i nquesto modo:
# prima i babelnet del primo termine
# poi i babelnet del secondo termine
# x1,x2,x3,x4...y1,y2,y3,y4
syn_gold = list(map(lambda x: x[3],gold))
syn_gold = syn_gold + list(map(lambda x: x[4],gold))
syn_gold2 = list(map(lambda x: x[3],gold2))
syn_gold2 = syn_gold2 + list(map(lambda x: x[4],gold2))

gold_pearson = corr.pearson(check_gold,check_gold2)
gold_spearman = corr.rank_spear(check_gold,check_gold2)
pearson1 = corr.pearson(result,check_gold)
spearman1 = corr.rank_spear(result,check_gold)
pearson2 = corr.pearson(result,check_gold2)
spearman2 = corr.rank_spear(result,check_gold2)
cohen_gold = cohen_kappa_score(syn_gold,syn_gold2)
cohen_nasari1 = cohen_kappa_score(name_list,syn_gold)
cohen_nasari2 = cohen_kappa_score(name_list,syn_gold2)


print(  f"Gold Results: Pearson value: {gold_pearson} Spearman value: {gold_spearman}"
        f"\nNasari (Zito) Results: Pearson value: {pearson1} Spearman value: {spearman1}"
        f"\nNasari (Ghergo) Results: Pearson value: {pearson2} Spearman value: {spearman2}"
        f"\nGold Cohen value: {cohen_gold}"
        f"\nNasari (Zito) Cohen value: {cohen_nasari1}"
        f"\nNasari (Ghergo) Cohen value: {cohen_nasari2}"
      )
print("Inizio Scrittura output")
file = open("output.txt", "w")
file2 = open("output2.txt", "w")
for item in output:
    file.write(item[0]+"\t"+item[1]+"\t"+item[2]+"\t"+item[3]+"\t"+str(item[4])+"\t"+str(item[5])+"\n")
for item in output2:
    file2.write(item[0]+"\t"+item[1]+"\t"+str(item[2])+"\n")
file.close()
file2.close()
print("Fine scrittura Output")
#file = open("perTe.txt", "w")
#for item in name_list:
#    file.write(item+"\n")
#file.close()
#print("Fine scrittura")
