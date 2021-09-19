from nltk.corpus.reader.wordnet import Synset
import math
def max_depth(node):
    hyps = node.hypernyms()
    if hyps:
        depth = 1 + max(current.max_depth() for current in hyps)
    else:
        depth = 0
    return depth



def find_lch(n1,n2):
    h1 = all_hyp(n1)
    h2 = all_hyp(n2)
    commons = list(h1.intersection(h2))
    if commons:
        m_depth = max(max_depth(s) for s in commons)
        unsorted_lch = [s for s in commons if max_depth(s) == m_depth]
    else:
        unsorted_lch = []
    return unsorted_lch

def all_hyp(node):
    output = []
    todo = [node]
    while todo:
        current = todo.pop()
        todo = todo + current.hypernyms()
        output= output + current.hypernyms()
    return set(output)

def get_paths(node):
    if node.name() == "*ROOT*":
        return {self: 0}
    todo = [(node,0)]
    lista_path = {}
    while todo:
        nd,depth = todo.pop()
        if nd not in lista_path:
            lista_path[nd] = depth
            depth += 1
            todo.extend((hyp, depth) for hyp in nd.hypernyms())
            todo.extend((hyp, depth) for hyp in nd._instance_hypernyms())
    return lista_path

def short_path_dist(node1,node2):
    if node1 == node2:
        return 0
    path1 = get_paths(node1)
    path_real1= node1._shortest_hypernym_paths(False)
    path_real2= node2._shortest_hypernym_paths(False)
    path2 = get_paths(node2)
    min_dist = float("inf")
    for synset, d1 in path1.items():
        d2 = path2.get(synset, float("inf"))
        min_dist = min(min_dist, d1 + d2)
    pippo = node1.shortest_path_distance(node2)
    return None if math.isinf(min_dist) else min_dist
