from algoritmia.statespace import IReversibleForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class SubsetSumStateSpace(IReversibleForwardStateSpace):#[s1
    def __init__(self, w, W):
        self.w, self.W, self.n = w, W, len(w)
        
    def initial_states(self):
        yield []

    def is_final(self, s):
        return len(s) == self.n and sum(s[i]*self.w[i] for i in range(self.n)) == self.W

    def decisions(self, s):
        if len(s) < self.n:
            yield 0
            weight = sum(s[i]*self.w[i] for i in range(len(s)))
            if weight + self.w[len(s)] <= self.W:
                yield 1

    def decide(self, s, d):
        s.append(d)
        return s

    def undo(self, s, d):
        s.pop()
        return s

class SubsetSumSolver1:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def solve(self, w, W):
        space = SubsetSumStateSpace(w, W)
        return next(self.enumerator.enumerate(space))#]s1