import nltk
from nltk.corpus import wordnet as wn
import numpy
import re

def lesk(word,sentence):
    if wn.synsets(word):
        best_sense = wn.synsets(word)[0]
        max_overlap = 0
        context = set(sentence[0])
        for sense in wn.synsets(word):
            signature = []
            for example in sense.examples():
                signature = signature + example.split()
            for glos in sense.definition().split():
                signature = signature + re.sub(r"[^a-zA-Z0-9]","",glos).split()
            signature = set(signature)
            overlap = len(signature.intersection(context))
            if overlap > max_overlap:
                max_overlap = overlap
                best_sense = sense
    else:
        best_sense = "None"
    return best_sense
