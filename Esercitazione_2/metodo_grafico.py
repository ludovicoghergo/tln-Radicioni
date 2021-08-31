
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import re
import grafo


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
tot_el = 0
tot_giusti = 0
for i in range(4):
    max_overlap = 0
    local = fn.frame(f[i][0])
    word1 = re.sub(r"[^a-zA-Z0-9 ]", "", local.definition).split()
    word2 = []
    synsets = []
    for fe in local.FE:
        synsets = synsets + wn.synsets(fe)
    synsets = set(synsets)
    grafo.graph_draw(grafo.wn_graph(synsets))
    print("fatto")