from algoritmia.problems.closures.interfaces import IDigraphTransitiveClosureFinder
from algoritmia.problems.closures.matrixclosure import WarshallMatrixTransitiveClosureFinder
from algoritmia.datastructures.digraphs.digraph import Digraph

class DigraphTransitiveClosureFinder(IDigraphTransitiveClosureFinder): #[w
    def __init__(self,
            createMatrixTransitiveClosureFinder: "-> IMatrixTransitiveClosureFinder"
                =lambda G: WarshallMatrixTransitiveClosureFinder(),
            createDigraph: "Iterable<T>, Iterable<(T, T)> -> IDigraph<T>"
                =lambda V, E: Digraph(V, E)):
        self.createMatrixTransitiveClosureFinder = createMatrixTransitiveClosureFinder
        self.createDigraph = createDigraph
        
    def transitive_closure(self, G: "Digraph<T>") -> "Digraph<T>":
        V = tuple(G.V)
        n = len(V)
        R = self.createMatrixTransitiveClosureFinder(G).transitive_closure(
            (((V[i], V[j]) in G.E) for j in range(n)) for i in range(n))
        C = self.createDigraph(G.V, 
            [(V[i], V[j]) for i in range(n) for j in range(n) if R[i][j]])
        return C #]w
