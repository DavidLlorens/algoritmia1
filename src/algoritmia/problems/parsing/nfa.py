#coding: latin1

#< full
class NFA:
    def __init__(self, Q: "ISet<T>", q0: "T", preds: "IMap<T, Iterable<(T, str)>>", F: "ISet<T>", 
                 createMap: "ISet<T> -> IMap<T, bool>"=lambda Q: dict()):
        self.Q, self.q0, self.preds, self.F = Q, q0, preds, F
        self.createMap = createMap
         
    def accepts(self, x: "str") -> "bool":
        P = [self.createMap(self.Q) for _ in range(1+len(x))]
        for q in self.Q: P[0][q] = False
        P[0][self.q0] = True
        for i in range(1, len(x)+1):
            for q in self.Q:
                P[i][q] = any(P[i-1][q1] and c == x[i-1] for (q1, c) in self.preds[q])
        return any(P[len(x)][q] for q in self.F)
#> full