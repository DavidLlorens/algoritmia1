#coding: latin1

#< full
from algoritmia.problems.shortestpaths.positive import DijkstraWithPriorityDictShortestPathsFinder
from algoritmia.data.mallorca import Mallorca, km

sp = DijkstraWithPriorityDictShortestPathsFinder()
path = sp.shortest_path(Mallorca, km, 'Andratx', 'Manacor')
print(', '.join(path)+'.') 
print('Distancia:', sum(km(path[i], path[i+1]) for i in range(len(path)-1)))
#> full