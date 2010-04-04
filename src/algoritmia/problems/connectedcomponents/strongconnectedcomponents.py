from algoritmia.problems.connectedcomponents.interfaces import IStrongConnectedComponentsFinder
from algoritmia.datastructures.queues.lifo import Lifo

class StrongConnectedComponentsFinder(IStrongConnectedComponentsFinder): #[strong
    def __init__(self, createSet: "Iterable<T> -> ISet<T>"=lambda V: set(),
                       createLifo: "ITerable<T> -> ILifo<T>"=lambda V: Lifo(),
                       createMap: "Iterable<T> -> IMap<T>"=lambda V: dict()):
        self.createSet = createSet
        self.createLifo = createLifo
        self.createMap = createMap

    def strong_connected_components(self, G: "IDigraph<T>") -> "Iterable<Iterable<T>>":
        Q = self.createLifo(G.V)
        d, l = self.createMap(G.V), self.createMap(G.V)
        visited, dead = self.createSet(G.V), self.createSet(G.V)
        comps = []
        def _strong_components(u):
            visited.add(u)
            Q.push(u)
            d[u] = len(d)
            l[u] = d[u]
            for v in G.succs(u):
                if v not in dead:
                    if v not in visited:
                        _strong_components(v)
                        l[u] = min(l[u], l[v])
                    else:
                        l[u] = min(l[u], d[v])
            if l[u] == d[u]:
                comp = []
                while True:
                    v = Q.pop()
                    comp.append(v)
                    dead.add(v)
                    if v == u: break
                comps.append(comp)
        _strong_components(list(G.V)[0])
        return (tuple(comp) for comp in comps) #]strong
