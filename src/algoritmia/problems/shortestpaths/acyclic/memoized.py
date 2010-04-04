from algoritmia.problems.shortestpaths.interfaces import IShortestPathsFinder
from algoritmia.utils import infinity, min
from algoritmia.problems.topsort.reversedpostorder import Topsorter

class MemoizedDagShortestPathsFinder(IShortestPathsFinder): #[memo
    def __init__(self, 
                 createTopsorter: "acyclic IDigraph<T> -> ITopsorter<T>"=lambda G: Topsorter(),
                 createMap: "acyclic IDigraph<T> -> IMap<T, ?>"=lambda V: dict()):
        self.createTopsorter = createTopsorter
        self.createMap = createMap

    def some_to_some_distance(self, G: "acyclic IDigraph<T>",
            d: "T, T -> R", I: "ICollection<T>", F: "ICollection<T>") -> "R": 
        mem = self.createMap(G.V)
        def D(v):
            init = 0 if v in I else infinity
            for u in G.preds(v):
                if u not in mem: mem[u] = D(u)
            return min(init, min((mem[u] + d(u,v) for u in G.preds(v)), ifempty=infinity))
        for t in F:
            if t not in mem: mem[t] = D(t)
        return min(mem[t] for t in F) #]memo

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "IterableContainer<T>", F: "IterableContainer<T>") -> "Iterable<(T, T or None)>": 
        raise NotImplementedError()
