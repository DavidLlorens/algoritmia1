#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.graphcoloring.greedy import GraphColorer

G = UndirectedGraph(E=[(0,1), (0,2), (0,3), (1,3), (1,4), (2,3), (2,5), (3,4), (3,5),
             (3,6), (4,7), (5,6), (5,8), (6,7), (6,8), (6,9), (7,9), (8,9)])
for i, s in enumerate(GraphColorer().colors(G)): print('Color {}: {}'.format((i+1), s))
#> full