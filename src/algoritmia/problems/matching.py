#coding: latin1

from algoritmia.utils import infinity

#< rest
#< state
class _StateBase:
    def __init__(self, s, d):
        self.parent = s
        self.decision = d
        self.k = 0 if s == None else s.k + 1

    def decision_sequence(self):
        ds = []
        p = self
        while p.parent != None:
            ds.append(p.decision)
            p = p.parent
        return tuple(reversed(ds))
        
    def __getitem__(self, i):
            if i < 0 or i >= self.k: raise IndexError
            if self.k-1 == i: return self.decision
            return self.parent[i]

    def __repr__(self):
        return str(self.decision_sequence())

    def __len__(self):
        return self.k

class MatchingAsBranchAndBoundProblem:
#> rest
    class State(_StateBase):
        def __init__(self, s=None, d=None, c=None):
            super().__init__(s, d)
            self.score = 0 if not s else s.score + c[self.k-1][d] 
#> state
#< rest
    def __init__(self, c):
        self.c = c
        self.M = len(c)
        
    def initial_states(self):
        yield MatchingAsBranchAndBoundProblem.State()

    def is_final(self, s):
        return s.k == self.M

    def decisions(self, s):
        used = set(s.decision_sequence())
        for i in range(self.M):
            if i not in used:
                yield i

    def take_decision(self, s, d):
        return MatchingAsBranchAndBoundProblem.State(s, d, self.c)

    def destination_is_promising(self, s, d):
        return True

    def opt(self, a, b):
        return min(a, b)

    def optimistic(self, s):
        return s.score

    def suboptimal_solution(self):
        return None

    def pessimistic(self, s):
        return self.zero
    
    def solution(self, s):
        return sum(self.c[i][s[i]] for i in range(len(s)))

    zero = infinity
    one = -infinity
#> rest

#< model2

class MatchingAsBranchAndBoundProblem2(MatchingAsBranchAndBoundProblem):
    class State(_StateBase):
        def __init__(self, s=None, d=None, c=None, minc=None):
            super().__init__(s, d)
            self.score = sum(minc) if not s else c[self.k-1][d] - sum(minc[self.k:]) 
            
    def __init__(self, c):
        super().__init__(c)
        self.minc = [min(row) for row in c]

    def initial_states(self):
        yield MatchingAsBranchAndBoundProblem2.State(minc=self.minc)

    def take_decision(self, s, d):
        return MatchingAsBranchAndBoundProblem2.State(s, d, self.c, self.minc)
#> model2

#< model3
class MatchingAsBranchAndBoundProblem3(MatchingAsBranchAndBoundProblem2):
    def __init__(self, c):
        super().__init__(c)

    def suboptimal_solution(self):
        return range(self.M)
#> model3