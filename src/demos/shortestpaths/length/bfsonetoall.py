#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths
from algoritmia.problems.shortestpaths import Backtracer

G = UndirectedGraph(E=[(0,1), (0,3), (1,2), (1,3), (1,4), (1,5), (2,5), (3,6), (4,6), #?(0,1?¶(0,1?
             (4,7), (4,8), (5,8)]) #?(4,7?»(4,7?
tree = dict(BreadthFirstShortestPaths().one_to_all_backpointers(G, 0))
print('Camino más corto de 0')
for v in range(9): print('  a {}: {}'.format(v, Backtracer(tree).backtrace(v)))
#> full
