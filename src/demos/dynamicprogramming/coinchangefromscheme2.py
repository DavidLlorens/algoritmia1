#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.statespace import MoneyChangeBackwardsStateSpace
from algoritmia.problems.generalizedcoinchange.weightingfunction import Weight
from algoritmia.schemes.dynamicprogramming.memoized import \
    MemoizedRecursiveDynamicProgrammingSolver
from algoritmia.semirings.tropical import MinTropicalSemiRing

v, w, Q = [1, 2, 5], [1, 1, 4], 7
space = MoneyChangeBackwardsStateSpace(v, w, Q)
solver = MemoizedRecursiveDynamicProgrammingSolver()
print(solver.solve(space, MinTropicalSemiRing, Weight(v, w)))
#> full