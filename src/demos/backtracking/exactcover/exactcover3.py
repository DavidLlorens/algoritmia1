#coding: latin1

#< full
from algoritmia.problems.exactcover.dlx import DLXSolver

print(DLXSolver().solve([[0,1,5],[3,4],[2,3,5],[0,2,3],[1,4,5],[2,3,4]]))
#> full