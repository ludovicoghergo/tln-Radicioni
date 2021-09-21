import re
from nltk.corpus import wordnet as wn

def weigthed_overlap(v1,v2):
    v1_filt = list(map(lambda x: x.split("_")[0], v1))
    v2_filt = list(map(lambda x: x.split("_")[0], v2))
    commons = set(v1_filt).intersection(set(v2_filt))
    i =  1
    nom = 0
    denom = 0
    for elem in commons:
        rank1 = v1_filt.index(elem)+1
        rank2 = v2_filt.index(elem)+1
        nom += pow(rank1+rank2,-1)
        denom += pow(2*i,-1)
        i += 1

    return nom/denom if denom != 0 else 0


def disambiguazione (context, dup):
    best_sense = dup[0][2:]
    max_overlap = 0
    for current in dup:
        for l in Lines4:
            pippo = l.split("\t")[0]
            if current[0] == pippo:
                signature = re.sub(r"[^a-zA-Z0-9 ]", "", l.split("\t")[1]).split()
                signature = set(signature)
                overlap = len(signature.intersection(context))
                if overlap > max_overlap:
                    max_overlap = overlap
                    best_sense = current[1:]
    return best_sense


def unify_vet (vettori):
    vet = []
    for v in vettori:
        for el in v:
            if (el == ""):
                print(2)
            vet.append(el)
    #prendo la seconda parte del termine nasari e ordino in base al suo valore
    vet.sort(key= lambda x: float(x.split("_")[1]),reverse=True)
    return vet

def create_context (frase):
    frase = re.sub(r"[^a-zA-Z0-9 ]", "", frase).lower().split(" ")
    frase = list(set(frase).difference(no_words))
    pippo = dict_vet
    vettori = []
    for w in frase:
        dup_vet = []
        if wn.morphy(w) in dict_vet:
            for elem in dict_vet[wn.morphy(w)]:
                dup_vet.append(elem)
        if (len(dup_vet)>1):
            vettori.append(disambiguazione(frase, dup_vet))
        elif (len(dup_vet)==1):
            vettori.append(dup_vet[0][2:])
    return unify_vet(vettori)

def selectTopic(paragraph):
    topic = ""
    for p in paragraph:
        for sentence in p.split("."):
            if len(set(sentence.lower().split(" ")).intersection(set(cues_words))) > 0:
                topic = topic +" "+sentence
    return topic


#leggo i file
file2 = open('utils/NASARI_vectors/dd-small-nasari-15.txt', encoding="utf8")
Lines2 = file2.readlines()
file3 = open('utils/stop_words_FULL.txt', 'r')
Lines3 = file3.readlines()
file4 = open('utils/babelnet.txt', encoding="utf8")
Lines4 = file4.readlines()
file5 = open('utils/cues_words.txt', encoding="utf8")
cues_words = file5.readlines()
cues_words = list(map(lambda x: x[:len(x)-1].lower(), cues_words))
no_words = []
testi = ['Andy-Warhol.txt','Ebola-virus-disease.txt','Life-indoors.txt','Napoleon-wiki.txt','Trump-wall.txt']
for line in Lines3:
    no_words.append(line[:len(line)-1])
no_words = set(no_words)
dict_vet = {}


for l in Lines2:
    elems = l.split(';')
    elems = list(filter(lambda a: a != '' and a !='\n', elems))
    if(elems[1].lower() in dict_vet):
        dict_vet[elems[1].lower()].append([elems[0]] + elems[2:])
    else:
        dict_vet[elems[1].lower()] = [[elems[0]] +elems[2:]]

for text in testi:
    titolo = []
    i = 0
    file1 = open('utils/docs/'+text, encoding="utf8")
    Lines = file1.readlines()
    while len(titolo)<=0 :
        if (Lines[i][0] != '#' and Lines[i][0]!='\n'):
            titolo = Lines[i]
        i=i+1
    #topic = create_context(titolo)
    val = 0
    paragraph = []
    final = []
    for l in Lines:
        if (l[0] != '#' and l[0]!='\n'):
            paragraph.append(l)
    ##
    topic = create_context(selectTopic(paragraph))
    print(topic)
    ##
    for p in paragraph:
        p_context = create_context(p)
        wo_val = weigthed_overlap(topic,p_context)
        final.append([p, p_context,wo_val])
    final_temp = final
    final_temp.sort(key= lambda x: x[2],reverse=True)
    perc=[10,20,30]
    file = open("utils/riassunti/"+text+"_short", "w")
    for size in perc:
        file.write("Riassunto con"+str(size)+"%:\n")
        calcolo = int(len(final_temp) - len(final_temp) * size / 100)
        filtered = final_temp[:calcolo]
        for elem in final:
            if elem in filtered:
                file.write(elem[0])





