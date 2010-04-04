#< it
class IterativeKnaspsackSolver:
    def __init__(self, createMap: "int, int -> IMap<(int, int), Real>"=lambda N, W: dict()):
        self.createMap = createMap

    def profit(self, W: "int", v: "IList<Real>", w: "IList<int>") -> "Real":
        N = len(v)
        B = self.createMap(N, W)
        for c in range(W+1): B[0, c] = 0
        for n in range(1, len(v)+1): 
            for c in range(w[n-1]): B[n,c] = B[n-1,c]
            for c in range(w[n-1], W+1): B[n,c] = max(B[n-1,c], B[n-1,c-w[n-1]]+v[n-1])
        return B[N, W]
#> it
