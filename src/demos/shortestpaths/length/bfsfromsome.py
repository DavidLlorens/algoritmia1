#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths
from algoritmia.problems.shortestpaths import Backtracer

G = UndirectedGraph(E={0: [1,3], 1:[2,3,4,5], 2:[5], 3:[6], 4:[6,7,8], 5:[8]})
tree = dict(BreadthFirstShortestPaths().some_to_some_backpointers(G, [0, 2], list(G.V)))
print('Camino más corto de 0 o 2')
for v in G.V: print('  a {}: {}'.format(v, Backtracer(tree).backtrace(v)))
#> full