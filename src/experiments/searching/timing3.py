#coding: latin1

#< full
from algoritmia.problems.searching import NaiveSequentialSearcher
from time import clock
from random import seed, randrange, sample

tmin = 2 # Tiempo mínimo de ejecución: dos segundos.
seed(0)
n = 100
a = sorted(sample(range(5*n), n))
x = a[randrange(n)]
searcher = NaiveSequentialSearcher()

t1 = t2 = clock()
r = 0
while t2 - t1 < tmin:
    index = searcher.index(a, x)
    t2 = clock()
    r += 1

t3 = t4 = clock()
aux = 0
while aux < r:
    t4 - t3
    index = 0
    t4 = clock()
    aux += 1

t = ((t2 - t1) - (t4 - t3)) / r
print('Tiempo medio por ejecución: {:.8f} segundos'.format(t))
#> full