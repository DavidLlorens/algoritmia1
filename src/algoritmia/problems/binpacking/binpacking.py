#coding: latin1

#< bb
from algoritmia.utils import infinity
from math import ceil
#> bb

#< nextfit

#> nextfit

#< firstfit

#> firstfit

#< firstfitdec

#> firstfitdec

#< bb
class BinPackingAsBranchAndBoundProblem:
    class State:
        def __init__(self, s=None, d=None, C=None, w=None):
            self.parent = s
            self.decision = d
            if s == None:
                self.len = 0
                self.maxsi = 0
                self.score = 0
                self.weight = {}
            else:
                self.len = s.len + 1
                self.maxsi = max(s.maxsi, d)
                self.weight = dict(s.weight)
                self.weight[d] = self.weight.get(d, 0) + w[s.len]
                self.score = self.maxsi + \
                    ceil((sum(w[self.len:]) - (C*self.maxsi - sum(w[:self.len])))/C)
        
        def decision_sequence(self):
            ds = []
            p = self
            while p.parent != None:
                ds.append(p.decision)
                p = p.parent
            return tuple(reversed(ds))
        
        def __repr__(self):
            return str(self.decision_sequence())

        def __getitem__(self, i):
            if i < 0 or i >= self.len: raise IndexError
            if self.len-1 == i: return self.decision
            return self.parent[i]

        def __len__(self):
            return self.len

    def __init__(self, C, w):
        self.C = C
        self.w = w
                
    def initial_states(self):
        yield BinPackingAsBranchAndBoundProblem.State()

    def is_final(self, s):
        return s.len == len(self.w)

    def decisions(self, s):
        if s.len < len(self.w):
            for d in range(s.maxsi + 2):
                if s.weight.get(d, 0) + self.w[s.len] <= self.C:
                    yield d

    def take_decision(self, s, d):
        return BinPackingAsBranchAndBoundProblem.State(s, d, self.C, self.w)

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
        return s.maxsi

    zero = infinity
    one = -infinity
#> bb