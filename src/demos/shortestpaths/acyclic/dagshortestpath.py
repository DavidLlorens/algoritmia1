#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.problems.shortestpaths.acyclic import DagShortestPathsFinder
from algoritmia.problems.shortestpaths.backtracer import Backtracer
from algoritmia.utils import argmin

d = WeightingFunction({(0,1):3, (0,3):-1, (1,2):5, (1,4):2, (1,5):4, 
                       (2,4): 3, (2,5):1, (3,1):1, (4,5):1})
G, I, F = Digraph(E=d.keys()), [0], [2, 5]
backtracer = Backtracer(DagShortestPathsFinder().some_to_some_backpointers(G, d, I, F))
t = argmin(F, lambda v: backtracer.distance(v))
print('El camino más corto entre {} y {} es {} y mide {}'.format(
      I, F, backtracer.backtrace(t), backtracer.distance(t)))
#> full