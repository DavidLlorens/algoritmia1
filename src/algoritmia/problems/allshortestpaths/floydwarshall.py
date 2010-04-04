from algoritmia.utils import infinity
from algoritmia.problems.shortestpaths.interfaces import IAllShortestPathsFinder
from algoritmia.datastructures.maps.interfaces import IMap

class AllShortestPathDraft(IAllShortestPathsFinder): #[floydwarshall1
    def __init__(self, createMap: "Iterable<T> -> IMap<T, T>"=lambda V: dict()):
        self.createMap = createMap

    def distances(self, G: "IDigraph<T>", d: "T, T -> R") -> "IMap<(T, T), R>": 
        D = self.createMap(G.V)
        for u in G.V:
            for w in G.V:
                if u == w: D[u, w, None] = 0
                elif w in G.succs(u): D[u, w, None] = d(u,w)
                else: D[u, w, None] = infinity
        vk_1 = None
        for vk in G.V:
            for u in G.V:
                for w in G.V:
                    D[u, w, vk] = min(D[u, w, vk_1], D[u, vk, vk_1] + D[vk, w, vk_1])
            vk_1 = vk
        distance = self.createMap(G.V)
        for u in G.V:
            for w in G.V:
                distance[u, w] = D[u, w, vk]
        return distance #]floydwarshall1

    def backpointers(self, G: "IDigraph<T>", d: "T, T -> R") -> "IMap<T, (T or None)>": #[floydwarshall2
        raise NotImplementedError()
    
class AllShortestPaths: #[floydwarshall #[]back
    def __init__(self, createMap: "Iterable<T> -> IMap<T, T>"=lambda V: dict()): 
        self.createMap = createMap
        
    def distances(self, G: "IDigraph<T>", d: "T, T -> R") -> "IMap<(T, T), R>": 
        D = self.createMap(G.V)
        for u in G.V:
            for w in G.V:
                if u == w: D[u,w] = 0
                elif w in G.succs(u): D[u,w] = d(u,w)
                else: D[u,w] = infinity
        for vk in G.V:
            for u in G.V:
                for w in G.V:
                    D[u,w] = min(D[u,w], D[u,vk] + D[vk,w])
        return D #]floydwarshall

    def backpointers(self, G: "IDigraph<T>", d: "T, T -> R") -> "IMap<T, (T or None)>":  #[back
        D, back = self.createMap(G.V), self.createMap(G.V)
        for u in G.V:
            for w in G.V:
                if u == w: D[u,w] = 0
                elif w in G.succs(u): D[u,w] = d(u,w)
                else: D[u,w] = infinity
                back[u,w] = None
        for vk in G.V:
            for u in G.V:
                for w in G.V:
                    if D[u,vk] + D[vk,w] < D[u,w]:
                        D[u,w] = D[u,vk] + D[vk,w]
                        back[u,w] = vk
        return back #]back

    def shortest_paths(self, G: "IDigraph<T>", back: "IMap<T, (T or None)>"):
        def backtrace(u: "T", w: "T"):
            vk = back[u, w]
            return backtrace(u, vk) + [vk] + backtrace(vk, w) if vk != None else []
        
        for (u,w) in back:
            path = [u] + backtrace(u, w) + [w]
            if all((path[i], path[i+1]) in G.E for i in range(len(path)-1)):
                yield path
