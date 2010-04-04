#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.spanningtrees import GraphTraversalSpanningTreeFinder

G = UndirectedGraph(E=[(0,1), (0,3), (1,4), (2,5), (3,1), (4,3)])
print(list(GraphTraversalSpanningTreeFinder().spanning_tree(G, 0)))
#> full