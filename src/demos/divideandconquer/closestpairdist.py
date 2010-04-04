#coding: latin1

#< full
from algoritmia.problems.geometry.closestpair import *

z = [(0.5,3.5), (1,2), (3,2), (3.5,1.5), (4,3.5), (5,0.5), (5,3), (5.5,1.5)]
cpf = ClosestPointsFinder1()
bfcpf = BruteForceClosestPointsFinder()
print('Distancia entre puntos más próximos:', cpf.distance_between_closest_points(z))
print('Ídem por fuerza bruta:', bfcpf.distance_between_closest_points(z))
#> full