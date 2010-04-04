'''
Created on 08/03/2010

@author: amarzal
'''
#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.statespace import MoneyChangeBackwardsStateSpace
from algoritmia.problems.generalizedcoinchange.weightingfunction import Weight
from algoritmia.semirings.kbest import KMinTropicalSemiRing
from algoritmia.schemes.dynamicprogramming.iterative import IterativeDynamicProgrammingSolver

v, w, Q = [1, 2, 5], [1, 1, 4], 7
space = MoneyChangeBackwardsStateSpace(v, w, Q)
print(IterativeDynamicProgrammingSolver().solve(space, KMinTropicalSemiRing(30), Weight(v, w)))
#> full