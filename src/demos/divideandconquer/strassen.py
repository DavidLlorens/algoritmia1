#coding: latin1

#< full
from algoritmia.problems.matrix.matrixprod import SqMatrix

A = B = SqMatrix([[(i*4+j) for i in range(4)] for j in range(4)])
C = A * B
for i in range(C.n):
    for j in range(C.n): print("{:6d}".format(C[i,j]), end=" ")
    print()
#> full