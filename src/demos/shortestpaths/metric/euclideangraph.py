#coding: latin1

#< full
from algoritmia.problems.shortestpaths.metric import MetricDigraphShortestPaths
from algoritmia.data.iberia import iberia, coords
from math import sqrt

def km(u, v, coords=coords):
    p, q = coords[u], coords[v]
    return sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

mdsp = MetricDigraphShortestPaths(km)
print('Camino {}'.format(mdsp.shortest_path(iberia, km, 'Ciudad Real', 'Soria')))
#> full