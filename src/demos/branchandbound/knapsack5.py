#coding: latin1

#< full
from algoritmia.problems.knapsack import KnapsackAsBestFirstOptimizationProblem
from algoritmia.schemes.branchandbound import BestFirstOptimizationSolver

v, w, W = [10, 2, 3, 4, 2], [12, 5, 6, 2, 6], 10
problem = KnapsackAsBestFirstOptimizationProblem(v, w, W)
solver = BestFirstOptimizationSolver(problem)
solution, profit = solver.solve()
print('Mejor solución:', solution, 'con beneficio', profit)
#> full