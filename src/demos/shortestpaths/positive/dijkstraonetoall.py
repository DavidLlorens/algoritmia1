#coding: latin1

#< full
from algoritmia.problems.shortestpaths.positive import DijkstraShortestPathsFinder
from algoritmia.data.mallorca import Mallorca, km

sp = DijkstraShortestPathsFinder()
for u, v in sp.some_to_some_backpointers(Mallorca, km, ['Andratx'], Mallorca.V):
    print('({}, {})'.format(u, v), end=", ")
#> full