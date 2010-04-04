from algoritmia.utils import chronometer

from algoritmia.problems.puzzles.nqueens.backtracking2 import NQueensEnumerator 
from algoritmia.problems.puzzles.nqueens.backtracking4 import NQueensStateSpace4
from algoritmia.problems.puzzles.nqueens.dlx2 import NQueensDLXSolver

solver = NQueensEnumerator()
dlx = NQueensDLXSolver()
for n in range(1, 31):
    print("{:2d} & ".format(n), end="") 
    print("{:6.2f} & ".format(1000*chronometer(1, lambda: solver.first(NQueensStateSpace4(n)))), end="")
    print("{:6.2f}\\\\".format(1000*chronometer(1, lambda: dlx.solve(n))))