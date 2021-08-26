import nltk
from nltk.corpus import semcor
import disambiguation as dis
from nltk.corpus.reader.wordnet import Lemma

def filt(x):
    return x.label() == 'NN'
sem = ""
word = ""
for s in semcor.tagged_sents(tag='both')[:1]:
    for c in s:
        if isinstance(c.label(), Lemma):
            if c[0].label() == 'NN':
                sem = c.label().synset()
                word = c[0][0]



print(dis.lesk(word, semcor.sents()[:1]).definition())
print(sem.definition())