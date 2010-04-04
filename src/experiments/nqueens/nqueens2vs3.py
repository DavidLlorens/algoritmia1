from algoritmia.utils import chronometer

from algoritmia.problems.puzzles.nqueens.backtracking2 import NQueensStateSpace2, NQueensEnumerator
from algoritmia.problems.puzzles.nqueens.backtracking3 import NQueensStateSpace3

solver = NQueensEnumerator()
for n in range(1, 25):
    print("{:2d} & ".format(n), end="") 
    print("{:6.2f} & ".format(1000*chronometer(1, lambda: solver.first(NQueensStateSpace2(n)))), end="")
    print("{:6.2f}\\\\".format(1000*chronometer(1, lambda: next(solver.enumerate(NQueensStateSpace3(n)), None))))