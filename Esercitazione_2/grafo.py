import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn
import time
import math

def traverse_loop(graph, start):
    done = set([])
    toDo = set([start])
    while toDo:
        actual = toDo.pop()
        if not actual in done:
            len = actual.shortest_path_distance(start)
            if isinstance(len, int) and not len > 1:
                for child in actual.hyponyms():
                    graph.add_edge(actual.name(), child.name())
                    toDo.add(child)
                for parent in actual.hypernyms():
                    graph.add_edge(actual.name(), parent.name())
                    toDo.add(parent)
        done.add(actual)
    return graph


def wn_graph(starts):
    G = nx.Graph() # [_define-graph]
    G.depth = {}
    print("inizio creazione grafo")
    for el in starts:
        G.add_node(el.name())
        traverse_loop(G, el)
    print("grafo creato")

    return G

#def graph_draw(graph):
#    nx.draw_shell(graph)
#    matplotlib.pyplot.show()

def best_sense(word, ctx, graph):
    scores = []
    denominatore = 0
    #for w in word.replace("_"," ").split():
    for s in wn.synsets(word):
        score = get_score(s, ctx, graph)
        denominatore+=score
        scores.append([s, score])
    best_sense=0
    best_prob=0
    i=0
    if(denominatore == 0):
        print("Zero")
    for i in range(0, len(scores)):
        prob = scores[i][1] / denominatore if denominatore != 0 else 0
        if prob>=best_prob:
            best_prob=prob
            best_sense=i
    if(not scores):
        print("None")
    ris = scores[best_sense][0] if scores else None
    return ris

def get_score(poss_sense,ctx,graph):
    sum = 0
    for sense in ctx:
        if graph.has_node(poss_sense.name())and graph.has_node(sense.name()) and nx.has_path(graph,poss_sense.name(),sense.name()):
            p = nx.shortest_path_length(graph,poss_sense.name(),sense.name())
            sum = sum + math.exp(-(p-1))
    return sum

