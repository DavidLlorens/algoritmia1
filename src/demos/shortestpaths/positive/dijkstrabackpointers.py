#coding: latin1

#< full
from algoritmia.problems.shortestpaths.positive import \
    DijkstraWithPriorityDictShortestPathsFinder
from algoritmia.data.mallorca import Mallorca, km

sp =DijkstraWithPriorityDictShortestPathsFinder()
for (u, v) in sp.some_to_some_backpointers(Mallorca, km, ['Andratx'], set(Mallorca.V)):
    print('({}, {})'.format(u, v), end = ", ")
#> full