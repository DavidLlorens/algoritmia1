from algoritmia.problems.topsort.reversedpostorder import Topsorter
from algoritmia.utils import infinity, min
from algoritmia.problems.shortestpaths.interfaces import IShortestPathsFinder

class ForwardDagShortestPathsFinder(IShortestPathsFinder): #[forward
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
            memv = mem[v] if v in mem else infinity
            if v in I: 
                memv = min(0, mem[v])
            if v in F:
                if memv < mindist: mindist = memv
                left -= 1
            if left > 0:
                del mem[v]
                for w in G.succs(v):
                    if w not in mem: mem[w] = infinity
                    mem[w] = min(mem[w], memv + d(v, w))
        return mindist #]iter

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", 
            F: "SizedIterableContainer<T>") -> "Iterable<(T, T or None)>": 
        mem= self.createMap(G.V)
        back = self.createMap(G.V)
        left = len(F)
        for v in self.createTopsorter(G).topsorted(G):
            if left == 0: break
            mem[v] = mem[v] if v in mem else infinity
            if v in I:
                if 0 < mem[v]:
                    mem[v] = 0
                    back[v] = v
            if v in F:
                left -= 1
            yield (v, back[v])
            if left > 0:
                del back[v]
                for w in G.succs(v):
                    if w not in mem: mem[w] = infinity
                    if mem[v] + d(v, w) < mem[w]:
                        back[w] = v
                        mem[w] = mem[v] + d(v, w) #]forward
                del mem[v]
