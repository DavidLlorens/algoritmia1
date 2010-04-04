class GreedyCoinChanger2:#[full
    def __init__(self, v: "IList<int>"):
        self.n = len(v)
        self.sorting_permutation = list(reversed(sorted(range(len(v)), key = v.__getitem__)))
        self.v = [v[i] for i in self.sorting_permutation]

    def change(self, Q: "int") -> "IList<int>":
        x = []
        for vi in sorted(self.v, reverse=True):
            x.append(Q//vi)
            Q = Q % vi
            if Q == 0: return self.sorted(x + [0] * (self.n-len(x)))
        return None

    def sorted(self, x: "IList<int>") -> "IList<int>":
        return [x[p] for p in self.sorting_permutation]#]full
