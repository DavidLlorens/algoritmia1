#coding: latin1

#< full
from algoritmia.problems.knapsack import branch_and_bound_knapsack0

v, w, W = [10,2,3,4,2], [12,5,6,2,6], 10
x, score = branch_and_bound_knapsack0(v, w, W)
print(x, score)
#> full