#coding: latin1

#< full
from algoritmia.problems.subsetsum.subsetsum3 import SubsetSumSolver3

w, W = [4,5,3,6], 8
print('Selección con pesos %s y capacidad %d:' % (w, W), end=' ')
print(SubsetSumSolver3().solve(w, W))
#> full