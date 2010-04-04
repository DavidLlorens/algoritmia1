from algoritmia.utils import infinity, argmin
from algoritmia.datastructures.prioritymaps.heapmap import MinHeapMap
from algoritmia.problems.shortestpaths.interfaces import IShortestPathsFinder

class DijkstraShortestPathsFinder(IShortestPathsFinder): #[dijkstra #[]dijkstrasp
    def __init__(self, createSet: "Iterable<T> -> ISet<T>"=lambda V: set(),
                       createMap: "Iterable<T> -> IMap<T, R>"=lambda V: dict()):
        self.createSet = createSet
        self.createMap = createMap
    
    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "IterableContainer<T>", F: "IterableContainer<T>") -> "R": 
        D = self.createMap(G.V)
        for v in G.V: D[v] = infinity
        for s in I: D[s] = 0
        in_fringe_from = self.createMap(G.V)
        for s in I: in_fringe_from[s] = s
        added = self.createSet(G.V)
        left = len(F)
        while len(in_fringe_from) > 0 and left > 0:
            (v, u) = argmin(in_fringe_from.items(), lambda e: D[e[0]])
            del in_fringe_from[v]
            added.add(v)
            yield (v, u)
            if v in F: left -= 1
            if left > 0:
                for w in G.succs(v):
                    if w not in added and D[v] + d(v,w) < D[w]:
                        D[w] = D[v] + d(v,w)
                        in_fringe_from[w] = v #]dijkstra
    
    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "IterableContainer<T>", F: "IterableContainer<T>") -> "R": 
        mindist = infinity
        D = self.createMap(G.V)
        for v in G.V: D[v] = infinity
        for s in I: D[s] = 0
        added = self.createSet(G.V)
        left = len(F)
        while len(D) > 0 and left > 0:
            (v, Dv) = argmin(D.items(), lambda v_Dv: v_Dv[1])
            del D[v]
            added.add(v)
            if v in F: 
                left -= 1
                if Dv < mindist: mindist = Dv
            if left > 0:
                for w in G.succs(v):
                    if w not in added and Dv + d(v,w) < D[w]:
                        D[w] = Dv + d(v,w)
        return mindist
    

class DijkstraWithPriorityDictShortestPathsFinder(IShortestPathsFinder): #[dijkstra2
    def __init__(self, createSet: "Iterable<T> -> ISet<T>"=lambda V: set(),
                       createMap: "Iterable<T> -> IMap<T, T>"=lambda V: dict(),
                       createPriorityMap: "Iterable<T> -> IPriorityMap<T, R>"
                            =lambda V: MinHeapMap(capacity=len(V))):
        self.createSet = createSet
        self.createMap = createMap
        self.createPriorityMap = createPriorityMap

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "IterableContainer<T>", F: "IterableContainer<T>") -> "R": 
        D = self.createPriorityMap(G.V)
        for v in G.V: D[v] = infinity
        for s in I: D[s] = 0
        back = self.createMap(G.V)
        for s in I: back[s] = s
        added = self.createSet(G.V)
        left = len(F)
        while len(D) > 0 and left > 0:
            (v, Dv) = D.extract_opt_item()
            added.add(v)
            yield (v, back[v] if v in back else None)
            if v in F: left -= 1
            if left > 0:
                for w in G.succs(v):
                    if w not in added and Dv + d(v,w) < D[w]:
                        D[w] = Dv + d(v,w)
                        back[w] = v #]dijkstra2
 
    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "IterableContainer<T>", F: "IterableContainer<T>") -> "R": 
        mindist = infinity
        D = self.createPriorityMap(G.V)
        for v in G.V: D[v] = infinity
        for s in I: D[s] = 0
        added = self.createSet(G.V)
        left = len(F)
        while len(D) > 0 and left > 0:
            (v, Dv) = D.extract_opt_item()
            added.add(v)
            if v in F: 
                left -= 1
                if Dv < mindist: mindist = Dv
            if left > 0:
                for w in G.succs(v):
                    if w not in added and Dv + d(v,w) < D[w]:
                        D[w] = Dv + d(v,w) 
        return mindist
    
    