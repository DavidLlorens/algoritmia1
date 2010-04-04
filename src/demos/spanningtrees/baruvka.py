#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from algoritmia.problems.spanningtrees import BaruvkasMinimumSpanningForestFinder

baruvka = BaruvkasMinimumSpanningForestFinder()
d = WeightingFunction({(0,1): 0, (0,2): 15, (0,3): 2, (1,3): 3, (1,4): 13, (2,3): 11, #?{?¶{? #?(0,1?¶(0,1? 
            (2,5): 4, (3,4): 5, (3,5): 8, (3,6): 12, (4,7): 9, (5,6): 16, #?(2,5?»»(2,5?
            (5,8):10, (6,7): 17, (6,8): 1, (6,9): 6, (7,9): 14, (8,9): 7},#?(5,8?»»(5,8? 
            symmetrical=True) #?symm?»symm?
MST = list(baruvka.minimum_spanning_forest(UndirectedGraph(E=d.keys()), d))
print('MST: {} con peso {}.'.format(MST, sum(d(u,v) for (u,v) in MST)))
#> full
