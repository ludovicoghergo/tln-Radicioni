import nltk
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import re

def best_sense(context,elements):
    FE_best_senses = []
    for elem in elements:
        max_overlap_FE = 0
        best_sense = "none"
        senses_list = []
        if wn.synsets(elem):
            senses_list = wn.synsets(elem)
        else:
            elem = elem.lower().replace("_", " ")
            elem = elem.split()
            for single in elem:
                senses_list = senses_list + wn.synsets(single)
        for sense in senses_list:
            elem_ctx = []
            for example in sense.examples():
                elem_ctx = elem_ctx + example.split()
            for glos in sense.definition().split():
                elem_ctx = elem_ctx + re.sub(r"[^a-zA-Z0-9]", "", glos).split()
            for hypo in sense.hyponyms():
                for example in hypo.examples():
                    elem_ctx = elem_ctx + example.split()
                for glos in hypo.definition().split():
                    elem_ctx = elem_ctx + re.sub(r"[^a-zA-Z0-9]", "", glos).split()
            for hyper in sense.hypernyms():
                for example in hyper.examples():
                    elem_ctx = elem_ctx + example.split()
                for glos in hyper.definition().split():
                    elem_ctx = elem_ctx + re.sub(r"[^a-zA-Z0-9]", "", glos).split()
            overlap = len(set(elem_ctx).intersection(context))
            if overlap >= max_overlap_FE:
                max_overlap_FE = overlap
                best_sense = sense
        FE_best_senses.append(best_sense)