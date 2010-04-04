#coding: latin1
from algoritmia.problems.spanningtrees.interfaces import IMinimumSpanningForestFinder
from algoritmia.problems.connectedcomponents.graphtraversal import GraphTraversalConnectedComponentsFinder
from algoritmia.datastructures.digraphs.digraph import UndirectedGraph
from algoritmia.utils import argmin

class BaruvkasMinimumSpanningForestFinder(IMinimumSpanningForestFinder): #[baruvka
    def __init__(self, 
            createConnectedComponentsFinder: 
                "IDigraph<T> -> IConnectedComponentsFinder<T>"
                =lambda G: GraphTraversalConnectedComponentsFinder(),
            createEditableUndirectedGraph: "Iterable<T> _-> IEditableDigraph<T>"
                =lambda V: UndirectedGraph(V, E=[]),
            createMap: "Iterable<T> -> IMap<T, int>"=lambda V: dict()):
        self.createConnectedComponentsFinder = createConnectedComponentsFinder
        self.createEditableUndirectedGraph = createEditableUndirectedGraph
        self.createMap = createMap
        
    def minimum_spanning_forest(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R") -> "Iterable<(T, T)>": 
        G2 = self.createEditableUndirectedGraph(G.V)
        ccf = self.createConnectedComponentsFinder(G)
        while True:
            C = [list(c) for c in ccf.connected_components(G2)]
            lbl = self.createMap(G.V)
            for i in range(len(C)):
                for v in C[i]:
                    lbl[v] = i
            merged = [False]*len(C)
            for i in range(len(C)):
                if not merged[i]:
                    e = argmin(((u,v) for u in C[i] for v in G.succs(u) if lbl[u] != lbl[v]),
                                lambda edge: d(edge))
                    if e!=None:
                        G2.E.add_unchecked(e)
                        yield e
                        merged[lbl[e[1]]] = True
                        for v in C[lbl[e[1]]]:
                            lbl[v] = lbl[e[0]]
            if not any(merged): break #]baruvka