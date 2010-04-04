#coding: latin1

#< full
from algoritmia.problems.puzzles.polyominoes.backtracking import PolyominoesSolver
from algoritmia.data.tetrominoes import tetrominos

print(PolyominoesSolver().solve('.......\n ......\n.......', tetrominos))
#> full