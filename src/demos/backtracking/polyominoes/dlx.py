#coding: latin1

#< full
from algoritmia.data.tetrominoes import tetrominos
from algoritmia.problems.puzzles.polyominoes.dlx import PolyominoesSolver

solver = PolyominoesSolver()
print(solver.solve('.......\n*......\n.......', tetrominos))
#> full