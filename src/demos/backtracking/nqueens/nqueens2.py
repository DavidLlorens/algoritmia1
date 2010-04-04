#coding: latin1
from algoritmia.problems.puzzles.nqueens.backtracking2 import NQueensStateSpace2#[full
from algoritmia.problems.puzzles.nqueens.backtracking2 import NQueensEnumerator

solver = NQueensEnumerator()
for n in range(1, 9):
    sol = solver.first(NQueensStateSpace2(n)) 
    print("Una solución con {} reina{}: {}".format(n, "s"*(n>1), sol))#]full