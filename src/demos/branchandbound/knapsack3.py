#coding: latin1

#< full
from algoritmia.problems.knapsack import branch_and_bound_knapsack3

v, w, W =  [11, 16, 13, 1, 11], [3, 5, 6, 3, 6], 6
x, score = branch_and_bound_knapsack3(v, w, W)
print(x, score)
#> full