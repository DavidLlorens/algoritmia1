#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from algoritmia.problems.spanningtrees import PrimsMinimumSpanningFinder

d = WeightingFunction({(0,1): 0, (0,2): 15, (0,3): 2, (1,3): 3, (1,4): 13, (2,3): 11,
                       (2,5): 4, (3,4): 5, (3,5): 8, (3,6): 12, (4,7): 9, (5,6): 16, 
                       (5,8):10, (6,7): 17, (6,8): 1, (6,9): 6, (7,9): 14, (8,9): 7}, 
                       symmetrical=True)
G = UndirectedGraph(E=d.keys())
MST = list(PrimsMinimumSpanningFinder().minimum_spanning_forest(G, d))
print('MST: {} con peso {}.'.format(MST, sum (d(u,v) for (u,v) in MST)))
#> full