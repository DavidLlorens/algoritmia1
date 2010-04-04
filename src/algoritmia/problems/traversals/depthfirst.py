#coding: latin1
from algoritmia.problems.traversals.interfaces import IDigraphDepthFirstTraverser
from algoritmia.datastructures.queues.fifo import Fifo
from algoritmia.datastructures.queues.lifo import Lifo
from itertools import dropwhile
         
class RecursiveDepthFirstTraverser(IDigraphDepthFirstTraverser): #[recursive
    def __init__(self, createFifo: "IDigraph<T> -> IFifo<T>"=lambda G: Fifo(), #?createFifo?¶createFifo?
                       createSet: "IDigraph<T> -> ISet<T>"=lambda G: set()): #?createSet?»createSet?
        self.createFifo = createFifo
        self.createSet = createSet

    def traverse(self, G: "IDigraph<T>", u: "T", preorder_visitor: "T, T -> S"=None, 
                 postorder_visitor: "T, T -> S"=None) -> "Iterable<S>":
        if preorder_visitor == postorder_visitor == None:
            preorder_visitor = lambda u, v: v
        visited = self.createSet(G.V)
        fifo = self.createFifo(G.V)
        self._traverse(G, u, u, preorder_visitor, postorder_visitor, visited, fifo)
        return fifo

    def _traverse(self, G: "IDigraph<T>", u: "T", v: "T", 
                 preorder_visitor: "T, T -> S", postorder_visitor: "T, T -> S",
                 visited: "ISet<T>", fifo: "IFifo<T>") -> "Iterable<S>":
        visited.add(v)
        if preorder_visitor != None:
            fifo.push(preorder_visitor(u, v))
        for w in G.succs(v):
            if w not in visited: 
                self._traverse(G, v, w, preorder_visitor, postorder_visitor, visited, fifo)
        if postorder_visitor != None:
            fifo.push(postorder_visitor(u, v))
    
    def full_traverse(self, G: "IDigraph<T>", 
                 preorder_visitor: "T, T -> S"=None, 
                 postorder_visitor: "T, T -> S"=None) -> "Iterable<S>":
        if preorder_visitor == postorder_visitor == None:
            preorder_visitor = lambda u, v: v
        visited = self.createSet(G.V)
        fifo = self.createFifo(G.V)
        for u in G.V:
            if u not in visited:
                self._traverse(G, u, u, preorder_visitor, postorder_visitor, visited, fifo)
            while len(fifo) > 0:
                yield fifo.pop()#]recursive 
    
class DepthFirstTraverser(IDigraphDepthFirstTraverser): #[iterative
    def __init__(self, createLifo=lambda V: Lifo(),
                       createSet=lambda V: set()):
        self.createLifo = createLifo
        self.createSet = createSet
        
    def traverse(self, G: "IDigraph<T>", u: "T", preorder_visitor: "T, T -> S"=None,
                 postorder_visitor: "T, T -> S"=None):
        if preorder_visitor == postorder_visitor == None:
            preorder_visitor = lambda u, v: v
        visited = self.createSet(G.V)
        stack = self.createLifo(G.V)
        return self._traverse(G, u, preorder_visitor, postorder_visitor, visited, stack)
    
    def _traverse(self, G: "IDigraph<T>", u: "T", preorder_visitor: "T, T -> S", 
                  postorder_visitor: "T, T -> S",
                  visited: "ISet<T>", stack: "ILifo<T>"):
        visited.add(u)
        stack.push(((u, u), (v for v in G.succs(u))))
        if preorder_visitor != None:
            yield preorder_visitor(u, u)
        while len(stack) > 0:
            ((u, v), succs) = stack.pop()
            succs = dropwhile(lambda w: w in visited, succs)
            w = next(succs, None)
            if w != None:
                stack.push(((u, v), succs))
                stack.push(((v, w), (x for x in G.succs(w))))
                visited.add(w)
                if preorder_visitor != None:
                    yield preorder_visitor(v, w)
            else:
                if postorder_visitor != None:
                    yield postorder_visitor(u, v)

    def full_traverse(self, G: "IDigraph<T>", 
                  preorder_visitor: "T, T -> S"=None, 
                  postorder_visitor: "T, T -> S"=None):
        if preorder_visitor == postorder_visitor == None:
            preorder_visitor = lambda u, v: v
        visited = self.createSet(G.V)
        stack = self.createLifo(G.V)
        for v in G.V:
            if v not in visited:
                for w in self._traverse(G, v, preorder_visitor, postorder_visitor, visited, stack): 
                    yield w  #]iterative