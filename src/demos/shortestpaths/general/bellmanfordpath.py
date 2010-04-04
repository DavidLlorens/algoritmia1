#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.problems.shortestpaths.general import BellmanFordShortestPathsFinder

d = WeightingFunction({(0,1):3, (0,3):1, (1,0):-2, (1,1):2, (1,2): 2, (1,4):-2,  
                       (1,5):3, (2,5):1, (3,1):1, (4,3):2, (4,5):2})
G = Digraph(E=d.keys())
path = BellmanFordShortestPathsFinder().shortest_path(G, d, 0, 5)
print('Distancia de 0 a 5:', sum(d(path[i],path[i+1]) for i in range(len(path)-1)))
print('Camino:', path)
#> full