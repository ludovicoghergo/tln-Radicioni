import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn
import math


def traverse(graph, start, node):
    len = node.shortest_path_distance(start)
    graph.depth[node.name()] = len
    if (len<=3):
        # for child in node.hyponyms():
        #     graph.add_edge(node.name, child.name)
        #     traverse(graph, start, child)
        for child in node.hypernyms():
             graph.add_edge(node.name(), child.name())
             traverse(graph, start, child)

def wn_graph(starts):
    G = nx.Graph() # [_define-graph]
    G.depth = {}
    for el in starts:
        traverse(G, el, el)
    return G

#def graph_draw(graph):
#    nx.draw_shell(graph)
#    matplotlib.pyplot.show()

def get_score(word,poss_sense,ctx,graph):
    sum = 0
    for term in ctx:
        for sense in wn.synsets(term):
            if graph.has_node(sense.name()) and nx.has_path(graph,poss_sense,sense.name()):
                p = list(nx.shortest_simple_paths(graph,poss_sense,sense.name()))
                sum = sum + math.exp(-(len(p[0])-1))
    return sum

