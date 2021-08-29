
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
    frame_sense.append(ctx.best_sense(word[i],f[i][1]))
    ### SENSO LEX UNIT
    LU_sense.append(ctx.best_sense_lux(word[i],local.lexUnit))


data = pd.read_csv ("/home/ludov/Desktop/tln-Radicioni/Esercitazione_2/annotation.txt", sep = '\t',header=0,names=["frame_word","frame_id","wn_syn"])
for d_row in data.itertuples():
    d_row[0]
print("ci")