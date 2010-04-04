#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.statespace import MoneyChangeBackwardsStateSpace
from algoritmia.schemes.dynamicprogramming.iterative import \
    IterativeIdempotentDynamicProgrammingSolver
from algoritmia.semirings.backpointer import MinTropicalBackPointerSemiRing
from algoritmia.problems.generalizedcoinchange.weightingfunction import WeightAndDecision

v, w, Q = [1, 2, 5], [1, 1, 4], 7
space = MoneyChangeBackwardsStateSpace(v, w, Q)
solver = IterativeIdempotentDynamicProgrammingSolver()
print(solver.solve(space, MinTropicalBackPointerSemiRing, WeightAndDecision(v, w)))
#> full