from nltk.corpus import wordnet as wn

def create_context (frase, no_words):
    frase = list(set(frase).difference(no_words))
    ctx_lemmas = []
    for w in frase:
        ctx_lemmas.append(wn.morphy(w.lower()))
    ctx_lemmas2 = list(filter(lambda x: x != None, ctx_lemmas))
    return set(ctx_lemmas2)
