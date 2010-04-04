#coding: latin1

#< full
from algoritmia.problems.knapsack import KnapsackAsBestFirstSearchProblem
from algoritmia.schemes.branchandbound import BestFirstSearchSolver
from algoritmia.utils import infinity

v, w, W = [10, 2, 3, 4, 2], [12, 5, 6, 2, 6], 10
problem = KnapsackAsBestFirstSearchProblem(v, w, W)
solver = BestFirstSearchSolver(problem)
opt_final, opt_result = None, -infinity
for final, result in solver.solve_all():
    print(final, result)
    if result > opt_result: 
        opt_final, opt_result = final, result
print('Mejor solución:', opt_final)
print('Beneficio:', opt_result)
#> full