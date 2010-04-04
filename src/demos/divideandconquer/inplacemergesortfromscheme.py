#coding: latin1

#< full
from algoritmia.problems.sorting import InPlaceMergesortProblem
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver

v = [11, 21, 3, 1, 98, 0, 12, 82, 29, 30, 11, 18, 43, 4, 75, 37]
DivideAndConquerSolver().solve(InPlaceMergesortProblem(v))
print(v)
#> full