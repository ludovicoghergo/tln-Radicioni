from nltk.corpus import wordnet as wn
##stop words
file3 = open('/home/ludov/Desktop/tln-Radicioni/Esercitazione_1/parte_2/data/stop_words_FULL.txt', 'r')
Lines3 = file3.readlines()
no_words = []
for line in Lines3:
    no_words.append(line[:len(line)-1])
print("Reading stop words...")
no_words = set(no_words)
## stop words

def create_context (frase):
    frase = list(set(frase).difference(no_words))
    ctx_lemmas = []
    for w in frase:
        ctx_lemmas.append(wn.morphy(w.lower()))
    ctx_lemmas2 = list(filter(lambda x: x != None, ctx_lemmas))
    return set(ctx_lemmas2)
