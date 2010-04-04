from algoritmia.statespace import IForwardStateSpace, IBackwardsStateSpace

class MoneyChangeForwardStateSpace(IForwardStateSpace):#[forward
    def __init__(self, v, w, Q):
        self.Q, self.v, self.w, self.n = Q, v, w, len(v)
        
    def initial_states(self) -> "Iterable<int>":
        yield 0
    
    def is_final(self, s: "int") -> "bool":
        return s == self.Q
    
    def decisions(self, s: "int") -> "Iterable<int>":
        return (vi for vi in self.v if s + vi <= self.Q)
                
    def decide(self, s: "int", d: "int") -> "int":
        return s + d #]forward
    
class MoneyChangeBackwardsStateSpace(IBackwardsStateSpace):#[backwards
    def __init__(self, v, w, Q):
        self.Q, self.v, self.w, self.n = Q, v, w, len(v)
        
    def final_states(self) -> "Iterable<int>":
        yield self.Q
    
    def is_initial(self, s: "int") -> "bool":
        return s == 0
    
    def incoming_decisions(self, s: "int") -> "Iterable<int>":
        return (vi for vi in self.v if s - vi >= 0)

    def undo(self, s: "int", d: "int") -> "int":
        return s - d #]backwards


    