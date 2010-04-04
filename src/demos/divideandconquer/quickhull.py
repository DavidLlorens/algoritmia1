#coding: latin1

#< full
from algoritmia.problems.geometry.convexhull import Point2D, QuickHullFinder
from random import seed, shuffle

# Creación de vector con 50 puntos aleatorios (no repetidos) con $0\leq x, y< 1000$.
seed(10)
x, y = list(range(1000)), list(range(1000))
shuffle(x); shuffle(y) # \emph{shuffle} «baraja» el contenido de la lista.
pts = [Point2D(x[i],y[i]) for i in range(50)]
qh = QuickHullFinder().quickhull(pts)
for point in qh: print(pts.index(point)+1, end=" ")
#> full 