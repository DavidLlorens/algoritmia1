class GreedyCoinChanger1:#[naif
    def __init__(self, v: "IList<int>"):
        self.v, self.n = v, len(v)

    def change(self, Q: "int") -> "IList<int>":
        x = []
        for vi in self.v:
            x.append(Q//vi)
            Q = Q % vi
            if Q == 0: 
                return x + [0] * (self.n-len(x))
        return None#]naif
