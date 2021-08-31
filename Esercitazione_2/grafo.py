import networkx as nx
import matplotlib
from nltk.corpus import wordnet as wn


def traverse(graph, start, node):
    graph.depth[node.name] = node.shortest_path_distance(start)
    if (node.shortest_path_distance(start)<=0):
        for child in node.hyponyms():
                graph.add_edge(node.name, child.name)
                print("aggiunto nodo" + str(child.name))
                traverse(graph, start, child)
        for child in node.hypernyms():
                 graph.add_edge(node.name, child.name)
                 print("aggiunto nodo" + str(child.name))
                 traverse(graph, start, child)

def hyponym_graph(start, start2):
    G = nx.Graph() # [_define-graph]
    G.depth = {}
    traverse(G, start, start)
    traverse(G, start2, start2)
    return G

def graph_draw(graph):
    nx.draw_shell(graph)
    matplotlib.pyplot.show()


graph_draw(hyponym_graph(wn.synset('dog.n.01'), wn.synset('canine.n.02')))
