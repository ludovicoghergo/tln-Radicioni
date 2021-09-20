import nltk
from nltk.corpus import wordnet as wn
import utils_es1 as ut
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
    lch = ut.find_lch(ss1,ss2)
    dp1 = ut.max_depth(ss1) + 1
    dp2 = ut.max_depth(ss2) + 1
    for wup in lch:
        dp_lch = ut.min_depth(wup) + 1
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
    if(ut.short_path_dist(ss1,ss2)!=None):
        sp = float(float(2*16) - float(ut.short_path_dist(ss1,ss2)))
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
    if (ut.short_path_dist(ss1,ss2) != None):
        lc = float(-(numpy.log((ut.short_path_dist(ss1,ss2)+1)/(2*16+1))))
        #print(str(lc) + " - " + str(ss1.lch_similarity(ss2)))
        return lc
    return 0.0