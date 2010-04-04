#< rec
class RecursiveKnapsackSolver:
    def profit(self, W: "int", v: "IList<Real>", w: "IList<int>") -> "Real":
        N = len(v)
        def B(n, c):
            if n==0: return 0
            if w[n-1] <= c: return max(B(n-1, c), B(n-1, c-w[n-1]) + v[n-1])
            return B(n-1, c)
        return B(N, W)
#> rec