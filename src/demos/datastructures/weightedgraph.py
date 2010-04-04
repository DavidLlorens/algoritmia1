#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from math import sqrt

G = UndirectedGraph(E= [((0,6),(2,2)), ((0,6),(2,6)), ((2,2),(4,4)), ((2,2),(4,0)),
                     ((2,2),(6,4)), ((2,6),(4,4)), ((4,0),(6,4))])

def d(u, v):
    return sqrt( (u[0]-v[0])**2 + (u[1]-v[1])**2 )

for (u, v) in G.E:
    print('{{{}, {}}}: {:4.2f}'.format(u, v, d(u,v)))
#> full