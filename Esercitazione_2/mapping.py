
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import context as ctx
import pandas as pd
import numpy as np
import re
from nltk.corpus.reader.wordnet import Synset

# FRAME GHERGO
#f = [[1582,"Proper_reference"],[2191,"Turning_out"],[1670,"Posing_as"],[15,"Separating"],[2320,"Cause_bodily_experience"]]
# FRAME ZITO
f = [[1025,"Connecting_architecture"],[2006,"Hunting"],[2612,"Circumscribed_existence"],[251,"Entity"],[62,"Placing"]]

file1 = open('annotation.txt', 'r')
#file1 = open('annotation2.txt', 'r')
Lines = file1.readlines()
i=0
title = 0
annotation = [[],[],[],[],[]]
for line in Lines:
    if(line != '\n'):
        l = line.split("\t")
        if(l[0][0].isupper()):
            if(title == 0):
                annotation[i].append(["Name", l[0], l[1], l[2]])
                title = 1
            else:
                annotation[i].append(["FE",l[0],l[1],l[2]])
        else:
            annotation[i].append(["LU", l[0], l[1], l[2]])
    else:
        i=i+1
        title=0

word = [] * 4
frame_sense = []
FE_sense = []
LU_sense = []
tot_el = 0
tot_giusti = 0
print('Reading frames...')
for i in range(5):
    max_overlap = 0
    local = fn.frame(f[i][0])
    print("reading frame: "+ f[i][1])
    word1 = re.sub(r"[^a-zA-Z0-9 ]", "", local.definition).split()
    word2 = []

    for elem in local.FE:
        val = local.FE[elem]
        word2 = word2 + (re.sub(r"[^a-zA-Z0-9 ]", "", val.definition).split())
    word.append(set(word1 + word2))
    ### SENSO FRAME ELEMENT
    FE_sense.append(ctx.best_sense(word[i],local.FE))
    ### SENSO FRAME
    formatter = []
    formatter.append(f[i][1])
    frame_sense.append(ctx.best_sense(word[i],formatter))
    ### SENSO LEX UNIT
    LU_sense.append(ctx.best_sense_lux(word[i],local.lexUnit))

    for fe in FE_sense[i]:
        tot_el = tot_el + 1
        for el in annotation[i]:
            if (el[0]=='FE' and el[1].lower()==fe[0].lower()):
                el.append(fe[1])
    for fs in frame_sense[i]:
        tot_el = tot_el + 1
        for el in annotation[i]:
            if (el[0]=='Name' and el[1].lower()==fs[0].lower()):
                el.append(fs[1])
    for lu in LU_sense[i]:
        tot_el = tot_el + 1
        for el in annotation[i]:
            if (el[0]=='LU' and el[1].lower().replace("_", " ")==lu[0][:len(lu[0])-2].lower()):
                el.append(lu[1])

for frame in annotation:
    for elem in frame:
        if(elem[3] != "None" and isinstance(elem[4], Synset)):
            if wn.synset(elem[3])==elem[4]:
                tot_giusti=tot_giusti+1
        else:
            tot_giusti
print("totale giusti = "+str(tot_giusti))
print("totale FE e LU = "+str(tot_el))
print("accuracy = "+str(tot_giusti/tot_el))
