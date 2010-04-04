#coding: latin1

#< full
from algoritmia.problems.puzzles.nqueens.backtracking5 import NQueensStateSpace5
from algoritmia.problems.puzzles.nqueens.backtracking5 import SpecialNQueensEnumerator

solver = SpecialNQueensEnumerator()
for n in range(1, 6):
    print("Soluciones con {} reina{}: ".format(n, "s"*(n>1)), end="")#]full
    for sol in solver.enumerate(NQueensStateSpace5(n)): print(sol, end=" ")
    print() 
#> full