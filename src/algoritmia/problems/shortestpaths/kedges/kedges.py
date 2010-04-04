from algoritmia.utils import infinity, min

class KEdgesDistance: #[kedges 
    def __init__(self, createMap: "Iterable<T>, int -> IMap<(T, int), R>"=lambda V, k: dict()):
        self.createMap = createMap
        
    def distance(self, G: "Digraph<T>", d: "T, T -> R", I: "ISet<T>", F: "ISet<T>", k: "int")->"R":
        D = self.createMap(G.V, k)
        for v in G.V: D[v, 0] = infinity
        for s in I: D[s, 0] = 0
        for i in range(1, k+1):
            for v in G.V:
                D[v, i] = min((D[u, i-1] + d(u,v) for u in G.preds(v)), ifempty=infinity)
        return min(D[t, k] for t in F) #]kedges

class SpaceReducedKEdgesDistance: #[kedges2
    def __init__(self, createMap: "Iterable<T> -> IMap<T, R>"=lambda V: dict()):
        self.createMap = createMap
        
    def distance(self, G: "Digraph<T>", d: "T, T -> R", I: "ISet<T>", F: "ISet<T>", k: "int")->"R":
        prev, curr = self.createMap(G.V), self.createMap(G.V)
        for v in G.V: curr[v] = infinity
        for s in I: curr[s] = 0
        for _ in range(1, k+1):
            prev, curr = curr, prev
            for v in G.V:
                curr[v] = min((prev[u] + d(u,v) for u in G.preds(v)), ifempty=infinity)
        return min(curr[t] for t in F) #]kedges2