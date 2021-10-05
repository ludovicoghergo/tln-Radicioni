

import similarity as sim
import pandas as pd
import correlation as corr
data = pd.read_csv("D:\Games\IntellijProject\\tln-Radicioni\Esercitazione_1\parte_1\data\WordSim353.csv", sep =',')

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
result1.append("wup_spearman = "+str(corr.rank_spear(human_arr,wp_arr)))
result1.append("sp_spearman = "+str(corr.rank_spear(human_arr,spw_arr)))
result1.append("lch_spearman = "+str(corr.rank_spear(human_arr,lch_arr)))
result.append("wup_pearson = "+str(corr.pearson(human_arr,wp_arr)))
result.append("sp_pearson = "+str(corr.pearson(human_arr,spw_arr)))
result.append("lch_pearson = "+str(corr.pearson(human_arr,lch_arr)))
print(result1)
print(result)
