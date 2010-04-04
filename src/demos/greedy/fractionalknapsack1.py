#coding: latin1

#< full
from algoritmia.problems.fractionalknapsack.suboptimal import SuboptimalFractionalKnapsackSolver

v, w, W = [60, 30, 40, 20, 75], [40, 30, 20, 10, 50], 50
print(', '.join([str(f) for f in SuboptimalFractionalKnapsackSolver().solve(w, v, W)]))
#> full