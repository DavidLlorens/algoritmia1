from algoritmia.statespace import IForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class HamiltonianCycleStateSpace(IForwardStateSpace):#[space
    def __init__(self, G):
        self.G = G
        
    def initial_states(self):
        yield (next(iter(self.G.V)),)
        
    def is_final(self, s):
        return len(s) == len(self.G.V) and (s[-1], s[0]) in self.G.E

    def decide(self, s, v):
        return s + (v,)
    
    def decisions(self, s):
        if len(s) < len(self.G.V):
            for v in self.G.succs(s[-1]):
                if v not in s:
                    yield v #]space

class HamiltonianCycleSolver:#[solver
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution
                                                 =lambda space, i, d, f: f + (f[0],))
    
    def solve(self, G):
        space = HamiltonianCycleStateSpace(G)
        return next(self.enumerator.enumerate(space)) #]solver
