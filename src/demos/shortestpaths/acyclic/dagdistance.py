#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.problems.shortestpaths.acyclic import DagShortestPathsFinder

d = WeightingFunction({(0,1): 3, (0,3): -1, (1,2): 5, (1,4): 2, (1,5): 4, #?(0,1?¶(0,1? 
                       (2,4): 3, (2,5): 1, (3,1): 1, (4,5): 1}) #?(2,4?»(2,4?
G, I, F = Digraph(E=d.keys()), [0], [2, 5]
print('Distancia entre {} y {}: {}'.format(
    I, F, DagShortestPathsFinder().some_to_some_distance(G, d, I, F)))
#> full