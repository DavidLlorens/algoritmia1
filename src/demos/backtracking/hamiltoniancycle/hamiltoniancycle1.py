#coding: latin1

#< full
from algoritmia.problems.hamiltoniancycle.forward import HamiltonianCycleSolver
from algoritmia.datastructures.digraphs import UndirectedGraph

G = UndirectedGraph(E=[(0,1), (0,2), (0,3), (1,3), (1,4), (2,3), (2,5), (3,4), (3,5), #?(0,1?¶(0,1?
             (3,6), (4,7), (5,6), (5,8), (6,7), (6,8), (6,9), (7,9), (8,9)]) #?(3,6?»(3,6?

print(HamiltonianCycleSolver().solve(G))
#> full