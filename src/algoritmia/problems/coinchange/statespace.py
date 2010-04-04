from algoritmia.statespace import IForwardStateSpace

class MoneyChangeForwardStateSpace(IForwardStateSpace):#[forward
    def __init__(self, Q, v):
        self.Q, self.v = Q, v
        
    def initial_states(self) -> "Iterable<int>":
        yield 0
    
    def is_final(self, s: "int") -> "bool":
        return s == self.Q
    
    def decisions(self, s: "int") -> "Iterable<int>":
        return (vi for vi in self.v if s + vi <= self.Q)
                
    def decide(self, s: "int", d: "int") -> "int":
        return s + d #]forward
    