#coding: latin1

#< full
from algoritmia.problems.sorting import MergesortProblem
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver

problem = MergesortProblem([11, 21, 3, 1, 98, 0, 12, 82, 29, 30, 11, 18, 43, 4, 75, 37])
print(DivideAndConquerSolver().solve(problem))
#> full