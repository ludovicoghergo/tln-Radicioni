import nltk
from nltk.corpus import wordnet as wn
import numpy

def wup_correlation_word(w1, w2):
    max = 0.0
    for ss1 in wn.synsets(w1):
        for ss2 in wn.synsets(w2):
            wup = wup_correlation_sense(ss1, ss2)
            if (wup > max):
                max = wup
    return max

def wup_correlation_sense(ss1,ss2):
    max_depth_lch = -1
    lch = ss1.lowest_common_hypernyms(ss2)
    dp1 = ss1.max_depth() + 1
    dp2 = ss2.max_depth() + 1
    for wup in lch:
        dp_lch = wup.min_depth() + 1
        if (max_depth_lch < dp_lch):
            max_depth_lch = dp_lch
    if (max_depth_lch != -1):
        return (2.0 * max_depth_lch) / (dp1 + dp2)
    return 0.0

def shortest_path_word(w1, w2):
    max = 0.0
    for ss1 in wn.synsets(w1):
        for ss2 in wn.synsets(w2):
            sp = shortest_path_sense(ss1, ss2)
            if (sp > max):
                max = sp
    return max

def shortest_path_sense(ss1, ss2):
    if(ss1.shortest_path_distance(ss2)!=None):
        sp = float(float(2*16) - float(ss1.shortest_path_distance(ss2)))
        return sp
    return 0.0

def lc_word (w1, w2):
    max = 0.0
    for ss1 in wn.synsets(w1):
        for ss2 in wn.synsets(w2):
            sp = lc_sense(ss1, ss2)
            if (sp > max):
                max = sp
    return max

def lc_sense (ss1, ss2):
    if (ss1.shortest_path_distance(ss2) != None):
        lc = float(-(numpy.log((ss1.shortest_path_distance(ss2)+1)/(2*16+1))))
        #print(str(lc) + " - " + str(ss1.lch_similarity(ss2)))
        return lc
    return 0.0