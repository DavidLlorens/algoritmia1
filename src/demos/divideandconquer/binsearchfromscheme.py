#coding: latin1

#< full
from algoritmia.schemes.decreaseandconquer import DecreaseAndConquerSolver
from algoritmia.problems.searching import BinarySearchProblem

a = [2, 3, 3, 4, 11, 11, 12, 18, 21, 29, 30, 37, 43, 75, 82, 98]
for v in 1, 10, 30, 100:
    print('Valor {} en {}.'.format(
        v, DecreaseAndConquerSolver().solve(BinarySearchProblem(a, v))))
#> full