from algoritmia.statespace import IReversibleForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class ExactCoverStateSpace(IReversibleForwardStateSpace): #[full
    def __init__(self, matrix):
        self.M, self.n, self.m = matrix, len(matrix), len(matrix[0])

    class State(list):
        def __init__(self, m, n):
            super().__init__([False] * n)
            self.i = 0
            self.covered = [False] * m

    def initial_states(self):
        yield ExactCoverStateSpace.State(self.m, self.n)

    def is_final(self, s):
        return s.i == self.n and all(s.covered)

    def decide(self, s, value):
        if value:
            for j in range(self.m):
                if self.M[s.i][j]: s.covered[j] = True
        s[s.i] = value
        s.i += 1
        return s

    def undo(self, s, value):
        s.i -= 1
        if value:
            for j in range(self.m):
                if self.M[s.i][j]: s.covered[j] = False
        return s

    def decisions(self, s):
        if s.i < self.n:
            if not any(self.M[s.i][j] and s.covered[j] for j in range(self.m)):
                yield True
            yield False 

class ExactCoverSolver:
    def __init__(self):
        self.solver = BacktrackingEnumerator(createSolution=lambda space, i, d, f: d)
        
    def solve(self, matrix):
        space = ExactCoverStateSpace(matrix)
        return(next(self.solver.enumerate(space)))
#]full
