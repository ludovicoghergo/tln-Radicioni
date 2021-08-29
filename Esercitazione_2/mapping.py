
import nltk
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn
import re


f = [[1582,"reference"],[2191,"turn_out"],[1670,"posing"],[15,"separating"],[2320,"experience"]]

word = [] * 5
word_sense = []
FE_sense = []
for i in range(5):
    max_overlap = 0
    local = fn.frame(f[i][0])
    word1 = re.sub(r"[^a-zA-Z0-9 ]", "", local.definition).split()
    word2 = []
    FE_best_senses = []
    for elem in local.FE:
        val = local.FE[elem]
        word2 = word2 + (re.sub(r"[^a-zA-Z0-9 ]", "", val.definition).split())
    word.append(set(word1 + word2))
    if i == 4:
        print("ciao")
    for elem in local.FE:
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
            overlap = len(set(elem_ctx).intersection(word[i]))
            if overlap >= max_overlap_FE:
                max_overlap_FE = overlap
                best_sense = sense
        FE_best_senses.append(best_sense)
    FE_sense.append(FE_best_senses)

    best_sense = "None"
    for sense in wn.synsets(f[i][1]):
        signature = []
        for example in sense.examples():
            signature = signature + example.split()
        for glos in sense.definition().split():
            signature = signature + re.sub(r"[^a-zA-Z0-9]", "", glos).split()
        for hypo in sense.hyponyms():
            for example in hypo.examples():
                signature = signature + example.split()
            for glos in hypo.definition().split():
                signature = signature + re.sub(r"[^a-zA-Z0-9]", "", glos).split()
        for hyper in sense.hypernyms():
            for example in hyper.examples():
                signature = signature + example.split()
            for glos in hyper.definition().split():
                signature = signature + re.sub(r"[^a-zA-Z0-9]", "", glos).split()

        overlap = len(set(signature).intersection(word[i]))
        if overlap >= max_overlap:
            max_overlap = overlap
            best_sense = sense
    word_sense.append(best_sense)
    pippo = 1

print(ris)