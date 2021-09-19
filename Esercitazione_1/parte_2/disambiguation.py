import nltk
from nltk.corpus import wordnet as wn
import utils_es2 as ut2
import numpy
import re
##stop words
file3 = open('/home/ludov/Desktop/tln-Radicioni/Esercitazione_1/parte_2/data/stop_words_FULL.txt', 'r')
Lines3 = file3.readlines()
no_words = []
for line in Lines3:
    no_words.append(line[:len(line)-1])
no_words = set(no_words)
## stop words


def lesk(word,sentence):
    if wn.synsets(word):
        best_sense = wn.synsets(word)[0]
        max_overlap = 0
        context = ut2.create_context(set(sentence[0]),no_words)
        for sense in wn.synsets(word):
            signature = []
            for example in sense.examples():
                signature = signature + example.split()
            for glos in sense.definition().split():
                signature = signature + re.sub(r"[^a-zA-Z0-9]","",glos).split()
            signature = set(signature)
            filtered = ut2.create_context(signature,no_words)
            overlap = len(filtered.intersection(context))
            if overlap > max_overlap:
                max_overlap = overlap
                best_sense = sense
    else:
        best_sense = "None"
    return best_sense
