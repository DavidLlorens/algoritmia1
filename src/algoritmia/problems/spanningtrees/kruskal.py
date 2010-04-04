from algoritmia.problems.spanningtrees.interfaces import IMinimumSpanningForestFinder
from algoritmia.datastructures.mergefindsets.mergefindset import MergeFindSet

class KruskalsMinimumSpanningForestFinder(IMinimumSpanningForestFinder): #[kruskal
    def __init__(self, createMergeFindSet: "Iterable<T> -> IMFSet<T>"
                 =lambda V: MergeFindSet((v,) for v in V)):
        self.createMergeFindSet = createMergeFindSet 
        
    def minimum_spanning_forest(self, G: "undirected Digraph<T>", 
            d: "T, T -> R") -> "Iterable<(T, T)> ":
        forest = self.createMergeFindSet(G.V)
        n = 0
        for (_, (u,v)) in sorted(((d(u,v), (u,v)) for (u,v) in G.E)):
            if forest.find(u) != forest.find(v): 
                forest.merge(u, v)
                yield (u, v)
                n += 1
                if n == len(G.V)-1: break #]kruskal
