from algoritmia.problems.spanningtrees.interfaces import IMinimumSpanningForestFinder,\
    IMinimumSpanningTreeFinder
from algoritmia.utils import argmin
from algoritmia.datastructures.prioritymaps.heapmap import MinHeapMap

class PrimsMinimumSpanningFinder(IMinimumSpanningTreeFinder, IMinimumSpanningForestFinder):#[prim1
    def __init__(self, createSet: "Iterable<T> -> ISet<T>"=lambda V: set(), 
                       createMap: "Iterable<T> -> IMap<T, R>"=lambda V: dict()):
        self.createSet = createSet
        self.createMap = createMap

    def minimum_spanning_tree(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R", u: "T") -> "Iterable<(T, T)>":
        added = self.createSet(G.V)
        return self._mst(G, d, u, added)
    
    def _mst(self, G: "undirected IDigraph<T>", 
             d: "T, T -> R", u: "T", added: "set<T>"=None) -> "Iterable<(T, T)>": #[p1
        added.add(u)
        in_frontier_from = self.createMap(G.V)
        for v in G.succs(u): in_frontier_from[v] = u
        while len(in_frontier_from) > 0:
            (v, u) = argmin(in_frontier_from.items(), d)
            del in_frontier_from[v]
            added.add(v)
            yield (u, v)
            for w in G.succs(v):
                if w not in added and \
                       (w not in in_frontier_from or d(v, w) < d(in_frontier_from[w], w)):
                    in_frontier_from[w] = v #]p1
                    
    def minimum_spanning_forest(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R") -> "Iterable<(T, T)>":
        added = self.createSet(G.V)
        for u in G.V:
            if u not in added:
                for v in self._mst(G, d, u, added):
                    yield v#]prim1

class PrimsWithPriorityQueueMinimumSpanningTreeFinder(PrimsMinimumSpanningFinder): #[prim2
    def __init__(self, createSet: "Iterable<T> -> ISet<T>"=lambda V: set(), 
                    createPriorityMap: "Iterable<T> -> IPriorityDict<T>" \
                        =lambda V: MinHeapMap()):
        self.createSet = createSet
        self.createPriorityMap = createPriorityMap

    def _mst(self, G: "undirected Digraph<T>", d: "T, T -> R", 
             u: "T", added: "set<T>") -> "Iterable<(T, T)>": 
        added.add(u)
        in_frontier_from = self.createPriorityMap(G.V)
        for v in G.succs(u): in_frontier_from[v] = (d(u,v), u) 
        while len(in_frontier_from) > 0:
            (v, (dv, u)) = in_frontier_from.extract_opt_item()
            added.add(v)
            yield (u, v)
            for w in G.succs(v):
                if w not in added and \
                       (w not in in_frontier_from or d(v, w) < d(in_frontier_from[w][1], w)):
                    in_frontier_from[w] = (d(v,w), v) #]prim2

