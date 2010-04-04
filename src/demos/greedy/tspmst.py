#coding: latin1

#< full
from algoritmia.problems.travelingsalesperson.spanningtree import SpanningTreeTravelingSalesPerson, d

traveler = SpanningTreeTravelingSalesPerson()
path = traveler.travel([(6,4), (0,6), (1,0), (2,6), (3,1), (4,1), (4,4)])
print(path)
print('Distancia recorrida:', sum(d(path[i], path[i+1]) for i in range(len(path)-1)))
#> full