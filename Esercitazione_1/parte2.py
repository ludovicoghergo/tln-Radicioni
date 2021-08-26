import nltk
from nltk.corpus import semcor
import disambiguation as dis
from nltk.corpus.reader.wordnet import Lemma
import random

def filt(x):
    return x.label() == 'NN'
test_data = []
correct = []
sents = semcor.sents()
index = random.randrange(0,len(sents)-51)

for s in semcor.tagged_sents(tag='both')[index:index+50]:
    for c in s:
        if isinstance(c.label(), Lemma):
            if c[0].label() == 'NN':
                test_data.append([c[0][0], c.label().synset()])
                break

i = 0
ris = 0
for s in sents[index:index+50]:
    sol = dis.lesk(test_data[i][0], s)
    if not isinstance(sol,str):
        ris = ris + 1 if test_data[i][1] == sol else ris
    test_data[i].append(sol)
    i = i + 1
perc = ris / 50
#print(dis.lesk(word, semcor.sents()[:1]).definition())

print("ciao")