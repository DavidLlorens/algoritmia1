from algoritmia.problems.topsort.reversedpostorder import Topsorter
from algoritmia.utils import infinity, argmin, min
from algoritmia.problems.shortestpaths.interfaces import IShortestPathsFinder

class DagShortestPathsFinder(IShortestPathsFinder): #[iter #[]back
    def __init__(self, createTopsorter: "acyclic IDigraph<T> -> ITopsorter<T>"
                    =lambda G: Topsorter(),
                 createMap: "acyclic IDigraph<T> -> IMap<T, ?>"=lambda V: dict()):
        self.createTopsorter = createTopsorter
        self.createMap = createMap
    
    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", F: "SizedIterableContainer<T>") -> "R": 
        mindist = infinity
        mem = self.createMap(G.V)
        left = len(F)
        for v in self.createTopsorter(G).topsorted(G):
            if left == 0: break
            mem[v] = min(0 if v in I else infinity, 
                         min((mem[u] + d(u,v) for u in G.preds(v)), ifempty=infinity))
            if v in F:
                if mem[v] < mindist: mindist = mem[v]
                left -= 1
        return mindist #]iter

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", #[back
            I: "SizedIterableContainer<T>", 
            F: "SizedIterableContainer<T>") -> "Iterable<(T, T or None)>": 
        mem= self.createMap(G.V)
        left = len(F)
        for v in self.createTopsorter(G).topsorted(G):
            if left == 0: break
            u = argmin(G.preds(v), lambda u: mem[u] + d(u, v), ifempty=None)
            mem[v] = mem[u] + d(u,v) if u != None else infinity
            if v in I and 0 < mem[v]: mem[v], u = 0, v
            yield v, u
            if v in F: left -= 1 #]back
