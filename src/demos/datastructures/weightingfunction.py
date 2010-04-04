#coding: latin1

#< full
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction

d = WeightingFunction({(0,1):4, (0,3):4, (1,4):1, (2,4):0, (2,5):2, (3,0):1, 
                                (3,1):4, (4,3):1, (5,5):2})
G = Digraph(E=d.keys())
for (u, v) in G.E: print('({}, {}): {}.'.format(u, v, d(u,v)), end=" ")
#> full