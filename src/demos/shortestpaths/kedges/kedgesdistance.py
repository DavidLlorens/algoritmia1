#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.problems.shortestpaths.kedges import KEdgesDistance

d = WeightingFunction({(0,1):3, (0,3):1, (1,0):-2, (1,1):2, (1,2): 2, (1,4):-2, 
                        (1,5):3, (2,5):1, (3,1):1, (4,3):2, (4,5):2})
G = Digraph(E=d.keys())
print('Distancia de {0} a {5}')
for i in range(6):
    print('  con {} aristas: {}'.format(i, KEdgesDistance().distance(G, d, [0], [5], i)))
#> full