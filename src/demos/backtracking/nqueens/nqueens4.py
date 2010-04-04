#coding: latin1

#< full
from algoritmia.problems.puzzles.nqueens.backtracking4 import NQueensStateSpace4
from algoritmia.problems.puzzles.nqueens.backtracking4 import NQueensEnumerator

solver = NQueensEnumerator()
for n in range(1, 8): 
    sol = solver.first(NQueensStateSpace4(n)) 
    print("Una solución con {} reina{}: {}".format(n, "s"*(n>1), sol))#]full
#> full