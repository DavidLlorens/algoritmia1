#coding: latin1
#< full
from algoritmia.datastructures.digraphs import AdjacencyDigraph
from algoritmia.datastructures.sets import IntSet
from algoritmia.datastructures.maps import IntKeyMap
from algoritmia.problems.traversals import BreadthFirstTraverser

G = AdjacencyDigraph(E=[(0,1), (0,3), (1,4), (2,5), (3,1), (4,3)], #?E=?¶E=?
                     createMap=lambda V: IntKeyMap(capacity=max(V)+1), #?mapF?»mapF?
                     createSet=lambda V: IntSet(capacity=max(V)+1)) #?setF?»setF?
bft = BreadthFirstTraverser(createSet=lambda V: IntSet(capacity=max(V)+1))
print(list(bft.traverse(G, 0)))
#> full