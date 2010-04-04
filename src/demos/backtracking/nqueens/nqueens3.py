#coding: latin1

#< full
from algoritmia.problems.puzzles.nqueens.backtracking3 import NQueensStateSpace3
from algoritmia.problems.puzzles.nqueens.backtracking3 import NQueensEnumerator

solver = NQueensEnumerator()
for n in range(1, 9): 
    sol = solver.first(NQueensStateSpace3(n)) 
    print("Una solución con {} reina{}: {}".format(n, "s"*(n>1), sol))#]full
#> full