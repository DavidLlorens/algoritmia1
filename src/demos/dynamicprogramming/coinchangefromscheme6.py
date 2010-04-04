#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.statespace import MoneyChangeForwardStateSpace
from algoritmia.schemes.dynamicprogramming.forward import \
    ForwardDynamicProgrammingSolver
from algoritmia.semirings.tropical import MinTropicalSemiRing
from algoritmia.problems.generalizedcoinchange.weightingfunction import Weight

v, w, Q = [1, 2, 5], [1, 1, 4], 7
space = MoneyChangeForwardStateSpace(v, w, Q)
solver = ForwardDynamicProgrammingSolver()
print(solver.solve(space, MinTropicalSemiRing, Weight(v, w)))
#> full