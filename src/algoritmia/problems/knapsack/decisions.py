
#< back
class KnaspsackSolver:
    def __init__(self, createMap: "int, int -> IMap<(int, int), Real>"=lambda N, W: dict()):
        self.createMap = createMap

    def decisions(self, W: "int", v: "IList<Real>", w: "IList<int>") -> "Real":
        N = len(v)
        B, back = self.createMap(N, W), self.createMap(N, W)
        for c in range(W+1): B[0,c], back[0,c] = 0, None
        for n in range(1, N+1): 
            for c in range(w[n-1]): B[n,c], back[n,c] = B[n-1,c], (n-1, c)
            for c in range(w[n-1], W+1):
                if B[n-1,c] > B[n-1,c-w[n-1]] + v[n-1]: B[n,c], back[n,c] = B[n-1,c], (n-1, c)
                else: B[n,c], back[n,c] = B[n-1,c-w[n-1]]+v[n-1], (n-1, c-w[n-1])
        path = []
        (n, c) = (len(v), W)
        while back[n,c] != None:
            path.append(1 if back[n,c] != (n-1, c) else 0)
            (n, c) = back[n,c]
        path.reverse()
        return path
#> back