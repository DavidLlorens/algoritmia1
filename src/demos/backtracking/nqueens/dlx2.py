#coding: latin1

#< full
from algoritmia.problems.puzzles.nqueens.dlx2 import NQueensDLXSolver

solver = NQueensDLXSolver()   
for n in range(1, 9):
    print("Solución con {} reinas: {}.".format(n, solver.solve(n)))
#> full