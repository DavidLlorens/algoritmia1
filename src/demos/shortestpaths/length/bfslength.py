#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths

G = Digraph(E=[(0,1), (0,3), (1,4), (2,4), (2,5), (3,0), (3,1), (4,3), (5,5)])
bfsp = BreadthFirstShortestPaths()
for (s,t) in (0,3), (0,4), (2,0):
    print('Aristas entre {} y {}: {}'.format(s, t, bfsp.distance(G, s, t)))
#> full