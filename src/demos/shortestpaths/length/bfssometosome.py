#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths
from algoritmia.problems.shortestpaths.backtracer import Backtracer

G = Digraph(E=[(0,1), (0,3), (1,2), (1,3), (1,4), (1,5), (2,5), (3,6), (4,6), 
               (4,7), (4,8), (5,8)])
print('Camino más corto de 0 o 2 a...')
backtracer = Backtracer(BreadthFirstShortestPaths().some_to_some_backpointers(G,[0, 2],[7, 8]))
print('7: {} con distancia {}'.format(backtracer.backtrace(7), backtracer.distance(7)))
print('8: {} con distancia {}'.format(backtracer.backtrace(8), backtracer.distance(8)))
#> full