#coding: latin1
from algoritmia.problems.puzzles.nqueens.backtracking1 import NQueensEnumerator#[full
from algoritmia.problems.puzzles.nqueens.backtracking1 import NQueensStateSpace1

solver = NQueensEnumerator()
for n in range(1, 9): 
    space = NQueensStateSpace1(n)
    print("Soluciones con {} reina{}:".format(n, 's'*(n>1)), end=" ")
    for queens in solver.enumerate(space): 
        print(queens, end=" ")
    print() #]full
