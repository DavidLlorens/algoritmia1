from algoritmia.statespace import IReversibleForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class SubsetSumStateSpace2(IReversibleForwardStateSpace):#[s2
    def __init__(self, w, W):
        self.w, self.W, self.n = w, W, len(w)

    class State(list):
        def __init__(self, w, N):
            super().__init__([0] * N)
            self.i = 0
            self.n = N
            self.sum = 0
            self.tail_sum = [0] * (N+1)
            for i in range(N-1, -1, -1): 
                self.tail_sum[i] = self.tail_sum[i+1] + w[i]

        def __repr__(self):
            return repr(self[:self.i] + [0] * (self.n-self.i))

    def initial_states(self):
        yield SubsetSumStateSpace2.State(self.w, self.n)

    def is_final(self, s):
        return s.sum == self.W

    def decisions(self, s):
        if s.i < self.n:
            if s.sum < self.W:
                if s.sum + self.w[s.i] + s.tail_sum[s.i+1] >= self.W:
                    yield 1
                if s.sum + s.tail_sum[s.i+1] >= self.W:
                    yield 0

    def decide(self, s, d):
        s[s.i] = d
        s.sum += d * self.w[s.i]
        s.i += 1
        return s

    def undo(self, s, d):
        s.i -= 1
        s.sum -= d * self.w[s.i]
        return s
    
class SubsetSumSolver2:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def solve(self, w, W):
        space = SubsetSumStateSpace2(w, W)
        return next(self.enumerator.enumerate(space))#]s2