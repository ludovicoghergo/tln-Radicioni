import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn
import math

def traverse_loop(graph, start):
    done = set([])
    toDo = set([start])
    while toDo:
        actual = toDo.pop()
        if not actual in done:
            len = actual.shortest_path_distance(start)
            if not len > 1:
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
        traverse_loop(G, el)
    print("grafo creato")
    return G

#def graph_draw(graph):
#    nx.draw_shell(graph)
#    matplotlib.pyplot.show()

def best_sense(word, ctx, graph):
    scores = []
    denominatore = 0
    for s in wn.synsets(word):
        score = get_score(s, ctx, graph)
        denominatore+=score
        scores.append([s, score])
    best_sense=0
    best_prob=0
    i=0
    for i in range(0, len(scores)):
        prob = scores[i][1] / denominatore
        if prob>best_prob:
            best_prob=prob
            best_sense=i
    return scores[best_sense][0]

def get_score(poss_sense,ctx,graph):
    sum = 0
    for term in ctx:
        for sense in wn.synsets(term):
            if graph.has_node(sense.name()) and graph.has_node(poss_sense.name()) and nx.has_path(graph,poss_sense.name(),sense.name()):
                p = list(nx.shortest_simple_paths(graph,poss_sense.name(),sense.name()))
                sum = sum + math.exp(-(len(p[0])-1))
    return sum

