
import nltk
import similarity as sim
import pandas as pd
import numpy as np
import correlation as corr
from nltk.corpus import wordnet as wn
import matplotlib.pyplot as plt
import scipy
data = pd.read_csv("/home/ludov/Desktop/tln-Radicioni/Esercitazione_1/parte_1/data/WordSim353.csv", sep =',')

wp_arr = []
spw_arr = []
lch_arr = []
human_arr = []
diff_arr = []
result = []
result1 = []
for d_row in data.itertuples():
    wp_arr.append(sim.wup_correlation_word(d_row[1],d_row[2]))
    spw_arr.append(sim.shortest_path_word(d_row[1],d_row[2]))
    lch_arr.append(sim.lc_word(d_row[1],d_row[2]))
    human_arr.append(d_row[3])
    #diff_arr.append(abs(WP(d_row[1],d_row[2])-d_row[3]))
result1.append(corr.rank_spear(human_arr,wp_arr))
result1.append(corr.rank_spear(human_arr,spw_arr))
result1.append(corr.rank_spear(human_arr,lch_arr))
result.append(corr.pearson(human_arr,wp_arr))
result.append(corr.pearson(human_arr,spw_arr))
result.append(corr.pearson(human_arr,lch_arr))
print(result1)
