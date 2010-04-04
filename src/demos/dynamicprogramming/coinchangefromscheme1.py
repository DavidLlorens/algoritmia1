#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.statespace import MoneyChangeBackwardsStateSpace
from algoritmia.problems.generalizedcoinchange.weightingfunction import Weight
from algoritmia.semirings.tropical import MinTropicalSemiRing
from algoritmia.schemes.dynamicprogramming.recursive import \
    RecursiveDynamicProgrammingSolver

v, w, Q = [1, 2, 5], [1, 1, 4], 7
space = MoneyChangeBackwardsStateSpace(v, w, Q)
print(RecursiveDynamicProgrammingSolver().solve(space, MinTropicalSemiRing, Weight(v, w)))
#> full