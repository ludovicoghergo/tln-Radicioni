from nltk.corpus import semcor
import disambiguation as dis
from nltk.corpus.reader.wordnet import Lemma
import random

test_data = ["Unknown"] * 50

def calc_lesk():
    correct = []
    sents = semcor.sents()
    index = random.randrange(0,300)
    j = 0
    for s in semcor.tagged_sents(tag='both')[index:index+50]:
        for c in s:
            if isinstance(c.label(), Lemma):
                if c[0].label() == 'NN':
                    test_data[j] = [c[0][0], c.label().synset()]
                    break
        j = j +1

    i = 0
    ris = 0
    for s in sents[index:index+50]:
        if not isinstance(test_data[i],str):
            sol = dis.lesk(test_data[i][0], s)
            if not isinstance(sol,str):
                ris = ris + 1 if test_data[i][1] == sol else ris
            test_data[i].append(sol)
        i = i + 1
    print(ris/50)
    return ris / 50

sum = 0
n_try = 10
for k in range(n_try):
    sum = sum + calc_lesk()
print("tot = "+ str(sum/n_try))