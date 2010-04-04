#coding: latin1

#< full
from algoritmia.problems.knapsack import KnapsackBfoWithOptimisticAndEarlyPruningProblem
from algoritmia.schemes.branchandbound import BfoWithOptimisticImplicitAndEarlyPruningSolver

v, w, W = [10, 2, 3, 4, 2], [12, 5, 6, 2, 6], 10
problem = KnapsackBfoWithOptimisticAndEarlyPruningProblem(v, w, W)
solver = BfoWithOptimisticImplicitAndEarlyPruningSolver(problem)
solution, profit = solver.solve()
print('Mejor solución:', solution, 'con beneficio', profit)
#> full