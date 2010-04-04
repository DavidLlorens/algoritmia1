from algoritmia.problems.traversals.breadthfirst import BreadthFirstTraverser
from algoritmia.problems.shortestpaths import Backtracer
from algoritmia.utils import argmin

class BreadthFirstShortestPaths: #[bfsl #[]bfsp #[]1all #[]bffromsome #[]some2some
    def __init__(self, createMap: "Iterable<T> -> IMap<T>"=lambda V: dict(),
            createBreadthFirstTraverser: "IDigraph<T> -> IGraphTraverser<T>"
                =lambda G: BreadthFirstTraverser()):
        self.createMap = createMap
        self.createBreadthFirstTraverser = createBreadthFirstTraverser
        
    def distance(self, G: "Digraph<T>", s: "T", t: "T"):
        length = self.createMap(G.V)
        length[s] = 0
        bft = self.createBreadthFirstTraverser(G)
        for (u, v) in bft.traverse(G, s, lambda u, v: (u, v)):
            if u != v: length[v] = length[u] + 1
            if v == t: return length[v]
        return None #]bfsl 

    def shortest_path(self, G: "Digraph<T>", s: "T", t: "T"): #[bfsp
        backpointer = self.createMap(G.V)
        bft = self.createBreadthFirstTraverser(G)
        for (u, v) in bft.traverse(G, s, lambda u, v: (u, v)):
            backpointer[v] = u
            if v == t: break
        return Backtracer(backpointer).backtrace(t) #]bfsp

    def one_to_all_backpointers(self, G: "Digraph<T>", s: "T") -> "Iterable<(T, T)>": #[1all
        bft = self.createBreadthFirstTraverser(G)
        return ((v, u) for (u, v) in bft.traverse(G, s, lambda u, v: (u, v))) #]1all
    
    def some_to_some_backpointers(self, G: "Digraph<T>", #[bffromsome 
            I: "Iterable<T>", F: "Iterable<T>") -> "Iterable<(T, T)>": 
        bft = self.createBreadthFirstTraverser(G)
        left = len(F)
        for (u, v) in bft.traverse_from_some(G, I, lambda u, v: (u, v)):
            yield (v, u)
            if v in F: 
                left -= 1
                if left == 0: break #]bffromsome

    def some_to_some_distance(self, G: "Digraph<T>", I: "Iterable<T>", #[some2some
            F: "Iterable<T>") -> "Iterable<(T, T)>": 
        length, backpointer = self.createMap(G.V), self.createMap(G.V)
        for s in I:
            length[s] = 0
            backpointer[s] = s
        bft = self.createBreadthFirstTraverser(G)
        bft.visitor = lambda u, v: (v, u) 
        for (u, v) in bft.traverse_from_some(G, I, lambda u, v: (u, v)):
            if v != u:
                length[v] = length[u] + 1
                backpointer[v] = u
        return Backtracer(backpointer).backtrace(argmin(F, lambda v: length[v])) #]some2some