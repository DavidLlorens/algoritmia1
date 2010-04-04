#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.connectedcomponents import GraphTraversalConnectedComponentsFinder

G=UndirectedGraph(E=[(0,1), (0,2), (1,2), (3,4), #?[(?[¶(? 
                     (5,6), (5,7), (5,8), (6,7), (6,8), (7,8)]) #?(5,6?»(5,6?
print([c for c in GraphTraversalConnectedComponentsFinder().connected_components(G)])
#> full