#coding: latin1

#< full
from algoritmia.problems.knapsack import KnapsackAsBfoWithOptimisticPruningProblem2
from algoritmia.schemes.branchandbound import BfoWithOptimisticPruningSolver

v, w, W = [10, 2, 3, 4, 2], [12, 5, 6, 2, 6], 10
problem = KnapsackAsBfoWithOptimisticPruningProblem2(v, w, W)
solver = BfoWithOptimisticPruningSolver(problem)
solution, profit = solver.solve()
print('Mejor solución:', solution)
print('Beneficio:', profit)
#> full