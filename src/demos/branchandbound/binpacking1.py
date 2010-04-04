#coding: latin1

#< full
from algoritmia.problems.binpacking import BinPackingAsBranchAndBoundProblem
from algoritmia.problems.binpacking import first_fit_decreasing_bin_packing, show_solution
from algoritmia.schemes.branchandbound import BranchAndBoundSolver
from algoritmia.datastructures.prioritydicts import MinHeapMap
from algoritmia.datastructures.graphs import UndirectedGraph, WeightingFunction

C, w = 100, [52, 18, 36, 21, 88, 15, 26, 29, 86, 7]
print('Solución voraz:')
show_solution(first_fit_decreasing_bin_packing(w, C), w)
problem = BinPackingAsBranchAndBoundProblem(C, w)
x, containers = BranchAndBoundSolver(problem, lambda keyvalues: MinHeapMap(keyvalues)).solve()
print('Solución óptima:') 
show_solution(x, w)
#> full