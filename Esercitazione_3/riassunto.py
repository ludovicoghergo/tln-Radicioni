import re
from nltk.corpus import wordnet as wn

def unify_vet (vettori):
    vet = []
    for v in vettori:
        for el in v:
            vet.append(el)
    #prendo la seconda parte del termine nasari e ordino in base al suo valore
    vet.sort(key= lambda x: float(x.split("_")[1]),reverse=True)
    return vet

def create_context (frase, nasari, no_words):
    frase = re.sub(r"[^a-zA-Z0-9 ]", "", frase).lower().split(" ")
    frase = list(set(frase).difference(no_words))
    vettori = []
    for w in frase:
        for v in nasari:
            if v[1].lower() == wn.morphy(w):
                vettori.append(v[2:])
    return unify_vet(vettori)

#leggo i file
file1 = open('utils/docs/Andy-Warhol.txt', encoding="utf8")
Lines = file1.readlines()
file2 = open('utils/NASARI_vectors/dd-small-nasari-15.txt', encoding="utf8")
Lines2 = file2.readlines()
file3 = open('utils/stop_words_FULL.txt', 'r')
Lines3 = file3.readlines()
no_words = []
for line in Lines3:
    no_words.append(line[:len(line)-1])
no_words = set(no_words)
vettori = []
titolo = []
i = 0

for l in Lines2:
    vettori.append(l.split(';'))
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

