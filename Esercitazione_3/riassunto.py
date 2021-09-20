import re
from nltk.corpus import wordnet as wn

def disambiguazione (context, dup):
    best_sense = dup[0][0]
    max_overlap = 0
    for current in dup:
        for l in Lines4:
            if current[0] == l.split("\t")[0]:
                signature = re.sub(r"[^a-zA-Z0-9]", "", l.split("\t")[1]).split()
                signature = set(signature)
                overlap = len(signature.intersection(context))
                if overlap > max_overlap:
                    max_overlap = overlap
                    best_sense = current
    return best_sense


def unify_vet (vettori):
    vet = []
    for v in vettori:
        for el in v:
            if (el == ""):
                print(2)
            vet.append(el)
    #prendo la seconda parte del termine nasari e ordino in base al suo valore
    vet.sort(key= lambda x: float(x.split("_")[1]),reverse=True)
    return vet

def create_context (frase, nasari, no_words):
    frase = re.sub(r"[^a-zA-Z0-9 ]", "", frase).lower().split(" ")
    frase = list(set(frase).difference(no_words))
    vettori = []
    for w in frase:
        dup_vet = []
        for v in nasari:
            if v[1].lower() == wn.morphy(w):
                dup_vet.append(v)
        if (len(dup_vet)>1):
            vettori.append(disambiguazione(frase, dup_vet))
        elif (len(dup_vet)==1):
            vettori.append(dup_vet[0][2:])
    return unify_vet(vettori)

#leggo i file
file1 = open('utils/docs/Andy-Warhol.txt', encoding="utf8")
Lines = file1.readlines()
file2 = open('utils/NASARI_vectors/dd-small-nasari-15.txt', encoding="utf8")
Lines2 = file2.readlines()
file3 = open('utils/stop_words_FULL.txt', 'r')
Lines3 = file3.readlines()
file4 = open('utils/babelnet.txt', encoding="utf8")
Lines4 = file4.readlines()
no_words = []
for line in Lines3:
    no_words.append(line[:len(line)-1])
no_words = set(no_words)
vettori = []
titolo = []
i = 0

for l in Lines2:
    elems = l.split(';')
    elems = list(filter(lambda a: a != '' and a !='\n', elems))
    vettori.append(elems)
while len(titolo)<=0 :
    if (Lines[i][0] != '#' and Lines[i][0]!='\n'):
        titolo = Lines[i]
    i=i+1
topic = create_context(titolo, vettori, no_words)
print(titolo)
print(topic)

paragraph = []
for l in Lines:
    if (l[0] != '#' and l[0]!='\n'):
        paragraph.append(l)
for p in paragraph:
    p = [p, create_context(p, vettori, no_words)]
    print(p)

