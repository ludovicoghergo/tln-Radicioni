
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import context as ctx
import pandas as pd
import numpy as np
import re

# FRAME GHERGO
#f = [[1582,"reference"],[2191,"turn_out"],[1670,"posing"],[15,"separating"],[2320,"experience"]]
# FRAME ZITO
f = [[1025,"Connecting_architecture"],[2006,"Hunting"],[2612,"Circumscribed_existence"],[251,"Entity"]]

file1 = open('annotation.txt', 'r')
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
for i in range(4):
    max_overlap = 0
    local = fn.frame(f[i][0])
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
        for el in annotation[i]:
            if (el[0]=='FE' and el[1].lower()==fe[0].lower()):
                el.append(fe[1])
    for fs in frame_sense[i]:
        for el in annotation[i]:
            if (el[0]=='Name' and el[1].lower()==fs[0].lower()):
                el.append(fs[1])
    for lu in LU_sense[i]:
        for el in annotation[i]:
            if (el[0]=='LU' and el[1]==lu[0][:len(lu[0])-2].lower()):
                el.append(lu[1])
print("a")