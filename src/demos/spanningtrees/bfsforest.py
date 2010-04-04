from algoritmia.datastructures.digraphs import UndirectedGraph #[full
from algoritmia.problems.spanningtrees.graphtraversal import GraphTraversalSpanningForestFinder

G = UndirectedGraph(E=[(0,1), (0,3), (1,4), (2,5), (3,1), (4,3)])
print([list(comp) for comp in GraphTraversalSpanningForestFinder().spanning_forest(G)]) #]full
