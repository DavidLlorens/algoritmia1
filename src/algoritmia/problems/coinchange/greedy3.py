from algoritmia.schemes.greedy import GreedySolver#[full
from algoritmia.problems.coinchange.backtracking3 import MoneyChangeStateSpace3

class ChangeSolver:
    def __init__(self, v: "IList<int>"):
        self.v = list(reversed(sorted(v)))
        self.greedy_solver = GreedySolver(
            createSolution=lambda space, d, s: d,
            decisionSelector=lambda space, s: max(space.decisions(s)))
        
    def solve(self, Q: "int") -> "IList<int>":
        space = MoneyChangeStateSpace3(Q, self.v)
        return self.greedy_solver.solve(space)#]full