from algoritmia.statespace import IForwardStateSpace

class MoneyChangeStateSpace2(IForwardStateSpace):#[statespace
    def __init__(self, Q, v):
        self.Q, self.v, self.n = Q, v, len(v)
        
    def initial_states(self) -> "Iterable<(int, int)>":
        yield (0, 0)
    
    def is_final(self, s: "(int, int)") -> "bool":
        (q, _) = s
        return q == self.Q
    
    def decisions(self, s: "int") -> "Iterable<(int, int)>":
        (q, i) = s
        return (self.v[j] for j in range(i, self.n) if q + self.v[j] <= self.Q)
                
    def decide(self, s: "(int, int)", d: "int") -> "int":
        (q, _) = s
        j = self.v.index(d)
        return (q + d, j) #]statespace