#< full
from fractions import Fraction

class SuboptimalFractionalKnapsackSolver:
    def solve(self, w: "IList<int>", v: "IList<int>", W: "int") -> "IList<int>":
        W = Fraction(W)
        x = [0] * len(w)
        for i in range(len(w)):
            x[i] = min(1, W / w[i])
            W -= x[i] * w[i]
        return x
#> full