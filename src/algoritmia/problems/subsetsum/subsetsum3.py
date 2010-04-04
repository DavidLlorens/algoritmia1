from algoritmia.statespace import IForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class SubsetSumStateSpace3(IForwardStateSpace):#[s3
    def __init__(self, w, W):
        self.w, self.W, self.n = w, W, len(w)
        self.tail_sum = [0] * (self.n+1)
        for i in range(self.n-1, -1, -1): 
            self.tail_sum[i] = self.tail_sum[i+1] + w[i]
        
    def initial_states(self):
        yield (0, 0)

    def is_final(self, s):
        (sum, _) = s
        return sum == self.W

    def decisions(self, s):
        (sum, n) = s
        if n < self.n:
            if sum < self.W:
                if sum + self.w[n] + self.tail_sum[n+1] >= self.W:
                    yield 1
                if sum + self.tail_sum[n+1] >= self.W:
                    yield 0

    def decide(self, s, d):
        (sum, n) = s
        return (sum + d * self.w[n], n+1)

class SubsetSumSolver3:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(
            createSolution=lambda space, i, d, f: d + [0]*(space.n-len(d)))
    
    def solve(self, w, W):
        space = SubsetSumStateSpace3(w, W)
        return next(self.enumerator.enumerate(space))