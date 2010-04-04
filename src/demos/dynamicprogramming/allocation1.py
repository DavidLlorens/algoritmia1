#coding: latin1

#< full
from algoritmia.problems.allocation.dynamicprogramming import ResourceAllocationSolver
from random import seed, randrange
seed(0)

U = 12
m = [2, 4, 2, 4, 2]
v = dict( ((i,u), randrange(100)) for i in range(len(m)) for u in range(0, U+1) )
print('   Recursos:', end=' ')
for u in range(0, U+1): print('{:2}'.format(u), end=' ')
print()
for i in range(len(m)):
    print('Actividad {}:'.format(i), end=' ')
    for u in range(0, U+1): print('{:2}'.format(v[i,u]), end=' ')
    print()
print('Beneficio:', ResourceAllocationSolver().profit(U, m, v))
#> full