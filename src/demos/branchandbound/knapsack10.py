#coding: latin1

#< full
from algoritmia.problems.knapsack import KnapsackAsBranchAndBoundProblem
from algoritmia.schemes.branchandbound import BranchAndBoundSolver

v, w, W = [10, 2, 3, 4, 2], [12, 5, 6, 2, 6], 10
problem = KnapsackAsBranchAndBoundProblem(v, w, W)
solver = BranchAndBoundSolver(problem)
solution, profit = solver.solve()
print('Mejor solución:', solution, 'con beneficio', profit)
#> full