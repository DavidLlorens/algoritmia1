from algoritmia.datastructures.prioritymaps import MinHeapMap
from algoritmia.utils import infinity
from algoritmia.problems.shortestpaths import Backtracer

class MetricDigraphShortestPaths: #[euclidean
    def __init__(self, d_prime: "T, T -> R",
                 createMap: "Iterable<T> -> IMap<T, R>"=lambda V: dict(),
                 createSet: "Iterable<T> -> ISet<T>"=lambda V: set(),
                 createPriorityMap: "Iterable<T> -> IPriorityMap<T, R>"
                    =lambda D, V: MinHeapMap(D, capacity=len(V))):
        self.d_prime = d_prime
        self.createMap = createMap
        self.createSet = createSet
        self.createPriorityMap = createPriorityMap
    
    def shortest_path(self, G: "metric IDigraph<T>", d: "T, T -> R", 
                      s: "T", t: "T") -> "Iterable<T>":
        D = self.createMap(G.V)
        for v in G.V: D[v] = infinity
        D[s] = 0
        back =  self.createMap(G.V)
        back[s] = s
        fringe = self.createPriorityMap(D.items(), G.V)
        fringe[s] = self.d_prime(s, t)
        added = self.createSet(G.V)
        while len(fringe) > 0:
            v = fringe.extract_opt()
            added.add(v)
            if v == t: break
            for w in G.succs(v):
                if w not in added and D[v] + d(v, w) < D[w]:
                    D[w] = D[v] + d(v,w)
                    fringe[w] =  D[w] + self.d_prime(w, t)
                    back[w] = v
        return Backtracer(back).backtrace(t) #]euclidean
