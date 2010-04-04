from algoritmia.datastructures.digraphs import UndirectedGraph #[full
from algoritmia.problems.traversals.breadthfirst import BreadthFirstTraverser

G = UndirectedGraph(E=[(0,1), (0,3), (1,4), (2,5), (3,1), (4,3)])
print(list(BreadthFirstTraverser().traverse(G, 0))) #]full
