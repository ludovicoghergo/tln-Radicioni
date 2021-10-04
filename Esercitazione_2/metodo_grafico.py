
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import re
import grafo
import networkx as nx



def get_context(word):
    word2 = []
    context = []
    no_words = []
    local = fn.frame(word)
    word1 = re.sub(r"[^a-zA-Z0-9 ]", "", local.definition).lower().split()
    for elem in local.FE:
        val = local.FE[elem]
        word2 = word2 + (re.sub(r"[^a-zA-Z0-9 ]", "", val.definition).lower().split())
    context = set(word1 + word2)
    file1 = open('stop_words_FULL.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        no_words.append(line[:len(line)-1])
    no_words = set(no_words)
    context = context.difference(no_words)
    return context


### prova
#CHECK ACCURACY
i=0
title = 0
fileGold = open('annotation2.txt', 'r')
LinesGold = fileGold.readlines()
fileOut = open('output.txt', 'r')
LinesOut = fileGold.readlines()
annotation = [[],[],[],[],[]]
res = []
for line in LinesGold:
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
print("ciao")

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
file = open("output.txt", "w")
count = 0
for i in range(4):
    max_overlap = 0
    local = fn.frame(f[i][0])
    word2 = []
    synsets = []
    word1 = re.sub(r"[^a-zA-Z0-9 ]", "",f[i][1].replace("_"," ")).split()
    for wd in word1:
        synsets = synsets + wn.synsets(wd)
    for fe in local.FE:
        synsets = synsets + wn.synsets(fe)
    for lu in local.lexUnit:
        synsets = synsets + wn.synsets(lu)
    ctx = get_context(f[i][0])
    for term in ctx:
        synsets= synsets + wn.synsets(term)
    synsets = set(synsets).difference("None")
    my_graph = grafo.wn_graph(synsets)
    #grafo.graph_draw(my_graph)
    #short_path_list = nx.shortest_simple_paths(my_graph,'part.n.02','object.n.01')
    #short_path_list = list(short_path_list)

    for elem in annotation[i]:
        tot_el +=1
        out_sense = grafo.best_sense(elem[1],ctx,my_graph)
        count = count + 1 if out_sense is not None and out_sense == wn.synset(elem[3]) else count

    # chiamare best sense per ogni fe e lexical unit
    # for fe in local.FE:
    #     file.write(fe+"\t"+str(grafo.best_sense(fe,ctx,my_graph))+"\n")
    #
    # for lu in local.lexUnit:
    #     file.write(lu+"\t"+str(grafo.best_sense(lu[:len(lu)-2],ctx,my_graph))+"\n")
    #
    file.write("\n")

file.close()
print(float(count/tot_el))


