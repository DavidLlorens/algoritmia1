#coding: latin1

#< gcolor
class GraphColorer:
    def __init__(self, createSet: "ISet<V> -> ISet<V>"=lambda V: set()):
        self.createSet = createSet
        
    def colors(self, G: "Undirected Digraph<V>") -> "IList<ISet<V>>":
        V = self.createSet(G.V)
        for v in G.V: V.add(v)
        partition = []
        while len(V) > 0:
            last_color = self.createSet(G.V)
            for v in V:
                if all(v not in G.succs(u) for u in last_color):
                    last_color.add(v)
            V = V.difference(last_color)
            partition.append(last_color)
        return partition
#> gcolor