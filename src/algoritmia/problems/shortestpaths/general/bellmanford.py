from algoritmia.utils import infinity, argmin, min
from algoritmia.problems.shortestpaths.interfaces import IShortestPathsFinder

class PreBellmanFordShortestPathsFinder(IShortestPathsFinder): #[pre
    def __init__(self, createMap: "Iterable<T> -> IMap<(T, int), R>"=lambda V: dict()):
        self.createMap = createMap

    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", F: "SizedIterableContainer<T>") -> "R": 
        D = self.createMap(G.V)
        for v in G.V: D[v] = infinity
        for s in I: D[s] = 0
        for _ in range(len(G.V)-1):
            for v in G.V:
                D[v] = min(D[v], min((D[u] + d(u,v) for u in G.preds(v)), ifempty=infinity))
        return min(D[t] for t in F) #]bellmanford

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", 
            F: "SizedIterableContainer<T>") -> "Iterable<(T, T or None)>": 
        D = self.createMap(G.V)
        back = self.createMap(G.V)
        for v in G.V: 
            D[v] = infinity
            back[v] = None
        for s in I: 
            D[s] = 0
            back[s] = s
        for _ in range(len(G.V)-1):
            for v in G.V:
                u = argmin(G.preds(v), lambda u: D[u] + d(u,v), ifempty=None)
                if u != None and D[u] + d(u, v) < D[v]:
                    D[v] = D[u] + d(u, v)
                    back[v] = u
        return back.items()#]pre

class BellmanFordShortestPathsFinder(IShortestPathsFinder): #[bellmanford #[]back
    def __init__(self, createMap: "Iterable<T> -> IMap<(T, int), R>"=lambda V: dict()):
        self.createMap = createMap

    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", F: "SizedIterableContainer<T>") -> "R": 
        D = self.createMap(G.V)
        for v in G.V: D[v] = infinity
        for s in I: D[s] = 0
        for _ in range(len(G.V)-1):
            changed = False
            for v in G.V:
                Du = min((D[u] + d(u,v) for u in G.preds(v)), ifempty=infinity)
                if Du < D[v]:
                    D[v]= Du 
                    changed = True
            if not changed: break
        return min(D[t] for t in F) #]bellmanford

    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", #[back 
            I: "SizedIterableContainer<T>", 
            F: "SizedIterableContainer<T>") -> "Iterable<(T, T or None)>": 
        D = self.createMap(G.V)
        back = self.createMap(G.V)
        for v in G.V: 
            D[v] = infinity
            back[v] = None
        for s in I: 
            D[s] = 0
            back[s] = s
        for i in range(len(G.V)-1):
            changed = False
            for v in G.V:
                u = argmin(G.preds(v), lambda u: D[u] + d(u,v), ifempty=None)
                if u != None and D[u] + d(u, v) < D[v]:
                    D[v] = D[u] + d(u, v)
                    back[v] = u
                    changed = True
            if not changed: break                    
        return back.items()#]back
