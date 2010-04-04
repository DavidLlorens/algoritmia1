#coding: latin1

#< full
class ResourceAllocationSolver:
    def __init__(self, createMap: "-> IMap<int, Real>"=dict):
        self.createMap = createMap
        
    def profit(self, U: "int", m: "IList<int>", v: "Ilist<Real>") -> "Real":
        N = len(m)
        P = self.createMap()
        for u in range(U+1): P[0, u] = 0
        for n in range(1, N+1):
            P[n, 0] = 0
            for u in range(1, U+1):
                P[n, u] = max(P[n-1, u-k] + v[n-1, k] for k in range(min(u, m[n-1])+1))
        return P[N, U]
#> full