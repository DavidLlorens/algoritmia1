#< full
from fractions import Fraction

class FractionalKnapsackSolver:
    def __init__(self, w: "IList<int>", v: "IList<int>"):
        self.n = len(v)
        self.sorting_permutation = list(reversed(sorted(range(self.n), key =lambda i: v[i]/w[i])))
        self.v, self.w = v, w

    def solve(self, W: "int") -> "IList<int>":
        W = Fraction(W)
        x = [0] * len(self.w)
        for i in self.sorting_permutation:
            x[i] = min(1, W / self.w[i])
            W -= x[i] * self.w[i]
        return x
#> full