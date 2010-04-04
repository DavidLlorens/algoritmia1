#coding: latin1

from algoritmia.problems.connectedcomponents.interfaces import IConnectedComponentsFinder
from algoritmia.problems.traversals import BreadthFirstTraverser

class GraphTraversalConnectedComponentsFinder(IConnectedComponentsFinder): #[ccbf
    def __init__(self, createDigraphTraverser: "IDigraph<T> -> IDigraphTraverser<T>" #?create?¶create?
                    =lambda G: BreadthFirstTraverser()):#?=?»=?
        self.createDigraphTraverser = createDigraphTraverser
        
    def connected_components(self, 
                             G: "undirected IDigraph<T>") -> "Iterable<Iterable<T>>":
        traverser = self.createDigraphTraverser(G)
        component = []
        first = True
        for (u, v) in traverser.full_traverse(G, visitor=lambda u, v: (u, v)):
            if u == v and not first:
                yield component
                component = []
            component.append(v)
            first = False
        yield component #]ccbf