from algoritmia.problems.shortestpaths.interfaces import IShortestPathsFinder
from algoritmia.utils import infinity, min

class RecursiveDagShortestPathsFinder(IShortestPathsFinder):#[recdag
    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", F: "SizedIterableContainer<T>") -> "R":
        def D(v):
            init = 0 if v in I else infinity
            return min(init, min((D(u)+d(u,v) for u in G.preds(v)), ifempty=infinity))
        return min(D(v) for v in F) #]recdag

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", 
            F: "SizedIterableContainer<T>") -> "Iterable<(T, T or None)>": 
        raise NotImplementedError()
