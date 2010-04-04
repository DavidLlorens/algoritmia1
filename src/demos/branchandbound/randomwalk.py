#coding: latin1

#< full
from algoritmia.problems.randomwalk import RandomWalkAsBranchAndBoundProblem
from algoritmia.schemes.branchandbound import BranchAndBoundSolver
from algoritmia.datastructures.prioritydicts import MaxHeapMap
from random import seed, randrange
from algoritmia.utils import argmax

seed(0)
walk = [0]
for i in range(999): walk.append(walk[-1] + (1 if randrange(2) else -1))
problem = RandomWalkAsBranchAndBoundProblem(walk)
s, minval = BranchAndBoundSolver(problem, lambda keyvalues: MaxHeapMap(keyvalues)).solve()
print("Por ramificación y acotación. Índice:", s.i, "Valor:", minval)
print("Por fuerza bruta.             Índice:", end= ' ')
print(argmax(range(len(walk)), lambda i: walk[i]), "Valor:", max(walk)) 
#> full