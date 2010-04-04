#coding: latin1
from algoritmia.problems.traversals.interfaces import IDigraphBreadthFirstTraverser
from algoritmia.datastructures.queues.fifo import Fifo


class BreadthFirstTraverser(IDigraphBreadthFirstTraverser): #[bfs #[]fromsome #[]bff 
    def __init__(self, createFifo: "IDigraph<T> -> IFifo<T>"=lambda G: Fifo(), #?createFifo?¶createFifo?
                       createSet: "IDigraph<T> -> ISet<T>"=lambda G: set()): #?createSet?»createSet?
        self.createFifo = createFifo
        self.createSet = createSet

    def traverse(self, G: "IDigraph<T>", s: "T", #?G:?¶G:? 
                       visitor: "T, T-> S"=lambda u, v: v)->"Iterable<S>": #?vis?»vis?
        visited = self.createSet(G.V)
        queue = self.createFifo(G.V)
        return self._traverse(G, s, visitor, visited, queue)
    
    def _traverse(self, G: "IDigraph<T>", s: "T", visitor: "T, T -> S", 
                  visited: "ISet<T>", queue: "IFifo<T>") -> "Iterable<S>":
        visited.add(s)
        queue.push(s)
        yield visitor(s, s)
        while len(queue) > 0:
            u = queue.pop()
            for v in G.succs(u):
                if v not in visited:
                    queue.push(v)
                    visited.add(v)
                    yield visitor(u, v) #]bfs

    def full_traverse(self, G: "IDigraph<T>", #[bff #?self?¶self? 
                      visitor: "T, T -> S"=lambda u, v: v) -> "Iterable<S>": #?vis?»vis?  
        visited = self.createSet(G.V)
        queue = self.createFifo(G.V)
        for u in G.V:
            if u not in visited:
                for v in self._traverse(G, u, visitor, visited, queue): yield v #]bff

    def traverse_from_some(self, G: "IDigraph<T>", I: "Iterable<T>", #[fromsome
            visitor: "T, T -> S"=lambda u, v: v) -> "Iterable<S>": 
        Q = self.createFifo(G.V)
        for v in I: Q.push(v)
        visited = self.createSet(G.V)
        for s in I:
            visited.add(s)
            yield visitor(s, s)
        while len(Q) > 0:
            u = Q.pop()
            for v in G.succs(u):
                if v not in visited:
                    Q.push(v)
                    visited.add(v)
                    yield visitor(u, v) #]fromsome