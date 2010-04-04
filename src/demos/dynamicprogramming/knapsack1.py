#coding: latin1

#< full
from algoritmia.problems.knapsack.recursive import RecursiveKnapsackSolver

W, v, w = 6, [90, 75, 60, 20, 10], [ 4,  3,  3,  2,  2]
print("Beneficio máximo con objetos de valores {} y pesos {}".format(v, w), end=' ')
print("con mochila de capacidad {}: {}.".format(W, RecursiveKnapsackSolver().profit(W,v,w)))
#> full