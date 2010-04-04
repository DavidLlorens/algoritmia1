#< it2
class SpaceSavingKnaspsackSolver:
    def __init__(self, createMap=lambda W: dict()):
        self.createMap = createMap

    def profit(self, W, v, w):
        N = len(v)
        curr, prev = [0] * (W+1), [0] * (W+1)
        for n in range(1, N+1): 
            for c in range(w[n]): curr[c] = prev[c]
            for c in range(w[n], W+1): curr[c] = max(prev[c], prev[c-w[n-1]]+v[n-1])
            curr, prev = prev, curr
        return prev[W]
#> it2


#< it3
class SpaceSavingKnaspsackSolver2:
    def __init__(self, createMap=lambda W: dict()):
        self.createMap = createMap

    def profit(self, W, v, w):
        N = len(v)
        B = [0] * (W+1)
        for n in range(1, N+1): 
            for c in range(W, w[n-1]-1, -1): B[c] = max(B[c], B[c-w[n-1]]+v[n-1])
            for c in range(w[n-1]-1, -1, -1): B[c] = B[c]
        return B[W]
#> it3


#< it4
class SpaceSavingKnaspsackSolver3:
    def __init__(self, createMap=lambda W: dict()):
        self.createMap = createMap

    def profit(self, W, v, w):
        N = len(v)
        B = [0] * (W+1)
        for n in range(1, N+1): 
            for c in range(W, w[n-1]-1, -1): B[c] = max(B[c], B[c-w[n-1]]+v[n-1])
        return B[W]
#> it4

