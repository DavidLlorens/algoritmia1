from algoritmia.datastructures.digraphs.adjacencydigraph import InvAdjacencyDigraph,\
    AdjacencyDigraph

class Digraph(InvAdjacencyDigraph): #[digraph
    def __init__(self, V=[], E=[]):
        super().__init__(V, E, directed=True)

    def __repr__(self) -> "str":
        return self.__class__.__name__ + '(V={!r}, E={!r})'.format(list(self.V), list(self.E))

class UndirectedGraph(AdjacencyDigraph):
    def __init__(self, V=[], E=[]):
        super().__init__(V, E, directed=False)

    def __repr__(self) -> "str":
        return self.__class__.__name__ + '(V={!r}, E={!r})'.format(list(self.V), list(self.E)) #]digraph

