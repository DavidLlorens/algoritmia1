#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.problems.shortestpaths.general import BellmanFordShortestPathsFinder

d = WeightingFunction({(0,1):3, (0,3):1, (1,0):1, (1,1):2, (1,2): 2, (1,4):-2, #?(0,1?¶(0,1?
                       (1,5):3, (2,5):1, (3,1):1, (4,3):2, (4,5):2}) #?(1,5?»(1,5?
bfsp = BellmanFordShortestPathsFinder()
print('Distancia de 0 a 5:', bfsp.distance(Digraph(E=d.keys()), d, 0, 5)) 
#> full