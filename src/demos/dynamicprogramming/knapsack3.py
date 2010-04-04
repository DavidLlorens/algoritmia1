#coding: latin1

#< full
from algoritmia.problems.knapsack.decisions import KnaspsackSolver

W, v, w = 6,[90, 75, 60, 20, 10], [ 4,  3,  3,  2,  2]
print("Selección de objetos de valores {} y pesos {} para máximo".format(v, w), end= ' ')
print("beneficio con mochila de capacidad {}: {}.".format(W, KnaspsackSolver().decisions(W,v,w)))
#> full