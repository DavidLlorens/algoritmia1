#coding: latin1

#< full
from algoritmia.utils import infinity

class RandomWalkAsBranchAndBoundProblem:
    class State:
        def __init__(self, i, j):
            self.i, self.j = i, j
            
        def __repr__(self):
            return '(%d, %d)' % (self.i, self.j)

    def __init__(self, walk):
        self.walk = walk
                
    def initial_states(self):
        yield RandomWalkAsBranchAndBoundProblem.State(0, len(self.walk))

    def is_final(self, s):
        return s.j - s.i == 1

    def decisions(self, s):
        k = (s.i + s.j) / 2
        if k > s.i: yield (s.i, k)
        if s.j > k+1: yield (k, s.j)

    def take_decision(self, s, d):
        return RandomWalkAsBranchAndBoundProblem.State(*d)

    def destination_is_promising(self, s, d):
        return True

    def solution(self, s):
        return self.walk[s.i]

    def opt(self, a, b):
        return max(a, b)

    def optimistic(self, s):
        return (self.walk[s.i] + self .walk[s.j-1] + (s.j-s.i)) / 2.0

    def suboptimal_solution(self):
        return None

    def pessimistic(self, s):
        return self.zero
    
    zero = -infinity
    one = infinity
#> full