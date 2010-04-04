from algoritmia.statespace import IForwardStateSpace

class MoneyChangeStateSpace3(IForwardStateSpace): #[statespace
    def __init__(self, Q: "int", v: "IList<int>"):
        self.Q, self.v, self.n = Q, v, len(v)
        
    def initial_states(self) -> "Iterable<(int, int)>":
        yield (0, 0)
    
    def is_final(self, s: "(int, int)") -> "bool":
        (q, n) = s
        return q == self.Q and n == self.n 
    
    def decisions(self, s: "(int, int)") -> "Iterable<int>":
        (q, n) = s
        if n < self.n:
            for i in range((self.Q-q) // self.v[n] + 1):
                yield i
               
    def decide(self, s: "State", d: "int") -> "State":
        (q, n) = s
        return (q + d * self.v[n], n + 1) #]statespace