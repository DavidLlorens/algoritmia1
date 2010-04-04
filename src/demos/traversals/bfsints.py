from algoritmia.datastructures.digraphs import AdjacencyDigraph #[full
from algoritmia.datastructures.sets import IntSet
from algoritmia.datastructures.maps import IntKeyMap
from algoritmia.problems.traversals.breadthfirst import BreadthFirstTraverser

G = AdjacencyDigraph(E=[(0,1), (0,3), (1,4), (2,5), (3,1), (4,3)],
                     createMap=lambda V: IntKeyMap(capacity=max(V)+1),
                     createSet=lambda V: IntSet(capacity=max(V)+1))
bft = BreadthFirstTraverser(createSet=lambda V: IntSet(capacity=max(V)+1))
print(list(bft.traverse(G, 0)))#]full
