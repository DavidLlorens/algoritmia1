from algoritmia.datastructures.digraphs.interfaces import IEditableDigraph, IEditableVertexSet, IEditableEdgeSet
from collections import Sequence
from algoritmia.datastructures.maps import IMap, IntKeyMap
from algoritmia.datastructures.sets import IntSet, ListSet, LinkedListSet
from itertools import chain

class AdjacencyDigraph(IEditableDigraph): #[adjacencyctor #[]props #[]props2 #[]vertexedgeset #[]rest
    def __init__(self, V: "Iterable<T>"=[], 
                 E: "Iterable<(T, T)> or IMap<T, Iterable<T>>"=[], 
                 directed: "bool"=True,
                 createMap: "Iterable<T> -> IMap<T, ISet<T>>"=lambda V: dict(), 
                 createSet: "Iterable<T> -> ISet<T>"=lambda V: set(),  
                 redimMap:"IMap<T,ISet<T>>,T -> IMap<T,ISet<T>>"
                    =lambda anIMap, maxkey: anIMap,
                 redimSet:"ISet<T>, T -> ISet<T>"=lambda aSet, maxkey: aSet):
        self.createMap = createMap
        self.createSet = createSet
        self.redimMap = redimMap
        self.redimSet = redimSet

        if isinstance(E, IMap): E = tuple((u, v) for u in E for v in E[u])
        elif not isinstance(E, Sequence): E = tuple(E)
        if not isinstance(V, Sequence): V = tuple(V)
        if not V: V = set(chain((u for (u,v) in E), (v for (u, v) in E)))

        self._directed = directed

        self._succs = self.createMap(V)
        for v in V: self._succs[v] = self.createSet(V)
        for (u,v) in E: self._succs[u].add(v)
        if not directed:
            for (u,v) in E: self._succs[v].add(u)

        self._vertexSet = AdjacencyDigraph.VertexSet(self)
        self._edgeSet = AdjacencyDigraph.EdgeSet(self) #]adjacencyctor


    V = property(lambda self: self._vertexSet) #[props
    E = property(lambda self: self._edgeSet) #]props
    
    is_directed = property(lambda self: self._directed) #[]props2
    
    class VertexSet(IEditableVertexSet): #[vertexedgeset
        def __init__(self, G: "AdjacencyDigraph<T>"):
            self.G = G

        def __contains__(self, v: "T") -> "bool":
            return v in self.G._succs

        def __iter__(self) -> "Iterable<T>":
            return (v for v in self.G._succs.keys())

        def __len__(self) -> "int":
            return len(self.G._succs)

        def add(self, v: "T"):
            self.G._add_vertex(v)

        def remove(self, v: "T"):
            self.G._remove_vertex(v)

        def __repr__(self) -> "str":
            return repr(list(self))

    class EdgeSet(IEditableEdgeSet):
        def __init__(self, G: "AdjacencyDigraph<T>"):
            self.G = G

        def __contains__(self, e: "(T, T)") -> "bool":
            return e[0] in self.G._succs and e[1] in self.G._succs[e[0]]

        def __iter__(self) -> "Iterable<(T, T)>":
            if self.G.is_directed:
                for u in self.G._succs:
                    for v in self.G._succs[u]: yield (u, v)
            else:
                prev = self.G.createSet(self.G.V)
                for u in self.G._succs:
                    prev.add(u)
                    for v in self.G._succs[u]:
                        if v not in prev: yield(u, v)

        def __len__(self) -> "int":
            return sum(len(self.G._succs[u]) for u in self.G._succs)

        def add(self, u: "T or (T, T)", v: "T or None"=None):
            if v == None: (u,v) = u
            self.G._add_edge((u, v))

        def add_unchecked(self, u: "T or (T, T)", v: "T or None"=None):
            if v == None: (u,v) = u
            self.G._add_edge_unchecked((u, v))

        def remove(self, u: "T or (T, T)", v: "T or None"=None):
            if v == None: (u,v) = u
            self.G._remove_edge((u, v))
            
        def __repr__(self) -> "str":
            return repr(list(self)) #]vertexedgeset

    def succs(self, u: "T") -> "Iterable<T>": #[rest
        return self._succs[u]

    def preds(self, v: "T") -> "Iterable<T>":
        return (u for u in self._succs if v in self._succs[u])

    def out_degree(self, u: "T") -> "int":
        return len(self._succs[u])

    def in_degree(self, v: "T") -> "int":
        return sum(1 for u in self.preds(v))

    def _add_vertex(self, v: "T"):
        if v not in self._succs:
            self.redimMap(self._succs, v)
            self._succs[v] = self.createSet(self.V)
            for u in self._succs:
                self.redimSet(self._succs[u], v)

    def _remove_vertex(self, v: "T"):
        if v in self._succs:
            del self._succs[v]
            for u in self._succs:
                if v in self._succs[u]: self._succs[u].remove(v)

    def _add_edge(self, edge: "(T, T)"):
        if edge[0] not in self._succs: self._add_vertex(edge[0])
        if edge[1] not in self._succs: self._add_vertex(edge[1])
        self._succs[edge[0]].add(edge[1])
        if not self.is_directed: self._succs[edge[1]].add(edge[0])

    def _add_edge_unchecked(self, edge: "(T, T)"):
        if hasattr(self._succs[edge[0]], 'add_unckecked'):
            self._succs[edge[0]].add_unchecked(edge[1])
            if not self.directed: self._succs[edge[1]].add_unchecked(edge[0])
        else:
            self._add_edge(edge)

    def _remove_edge(self, edge: "(T, T)"):
        self._succs[edge[0]].remove(edge[1])
        if not self.is_directed: self._succs[edge[1]].remove(edge[0])

    def __repr__(self) -> "str":
        return '{}(V={!r}, E={!r}, directed={!r})'.format(self.__class__.__name__, \
           list(self.V), list(self.E), self.is_directed) #]rest

class LinkedListSetAdjacencyDigraph(AdjacencyDigraph): #[linkedlist
    def __init__(self, V=[], E=[], directed=True, **kw):
        super().__init__(V, E, directed, createSet=lambda V: LinkedListSet(), **kw) #]linkedlist 

class ListSetAdjacencyDigraph(AdjacencyDigraph): #[listset
    def __init__(self, V=[], E=[], directed=True, **kw):
        super().__init__(V, E, directed, createSet=lambda V: ListSet(), **kw) #]listset 

class SetAdjacencyDigraph(AdjacencyDigraph): #[set
    def __init__(self, V=[], E=[], directed=True, **kw):
        super().__init__(V, E, directed, createSet=lambda V: set(), **kw) #]set 

class AdjacencyMatrixDigraph(AdjacencyDigraph): #[matrix
    def __init__(self, V: "Iterable<T>"=[], E: "Iterable<(T,T)>"=[], directed: "bool"=True):
        capacity = max(V)+1
        super().__init__(V, E, directed,
              createMap=lambda V: IntKeyMap(capacity=capacity),
              createSet=lambda V: IntSet(capacity=capacity),
              redimMap=lambda map, v: map.set_capacity(v+1),
              redimSet=lambda set, v: set.set_capacity(v+1))

    def _add_vertex(self, v: "T"):
        if v not in self._succs:
            if self._succs.capacity <= v: self._succs.capacity = v + 1
            self._succs[v] = self.createSet(self.V)
            if self._succs[0].capacity <= v: #posible bug
                for u in self._succs:
                    self._succs[u].capacity = v + 1 #]matrix

class InvAdjacencyDigraph(AdjacencyDigraph): #[inv
    def __init__(self, V, E, directed=True, **kw):
        super().__init__(V, E, directed, **kw)
        if directed:
            self._preds = self.createMap(self.V)
            for v in self._succs: self._preds[v] = self.createSet(self.V)
            for (u, v) in self.E: self._preds[v].add(u)
        else:
            self._preds = self._succs
        
    def preds(self, v: "T") -> "Iterable<T>":
        return self._preds[v]

    def in_degree(self, v: "T") -> "int":
        return len(self._preds[v])

    def _add_vertex(self, v: "T"):
        if v not in self._succs:
            self._succs[v] = self.createSet(self.V)
            if self._directed: self._preds[v] = self.createSet(self.V)

    def _remove_vertex(self, v: "T"):
        if v in self._succs:
            for u in self._succs[v]:
                self._preds[u].discard(v)
            if self._directed:
                for u in self._preds[v]:
                    self._succs[u].discard(v)
                del self._preds[v]
            del self._succs[v]

    def _add_edge(self, edge: "(T, T)"):
        self._succs[edge[0]].add(edge[1])
        if self._directed: self._preds[edge[1]].add(edge[0])
        else: self._succs[edge[1]].add(edge[0])

    def _add_edge_unchecked(self, edge: "(T, T)"):
        if 'add_unckecked' in self._succs.__class__.__dict__:
            self._succs[edge[0]].add_unchecked(edge[1])
            if not self._directed: self._succs[1].add_unchecked(edge[0])
            else: self._succs[edge[1]].add_unchecked(edge[0])
        else:
            self._add_edge(edge)

    def _remove_edge(self, edge: "(T, T)"):
        self._succs[edge[0]].discard(edge[1])
        if not self._directed: self._preds[edge[1]].discard(edge[0]) #]inv