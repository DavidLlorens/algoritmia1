#coding: latin1

#< full
from algoritmia.problems.searching import NaiveSequentialSearcher
from time import clock
from random import seed, randrange, sample

# Generaci�n de un vector aleatorio.
seed(0)
n = 100
a = sorted(sample(range(5*n), n))
x = a[randrange(n)]
searcher = NaiveSequentialSearcher()

# Ejecuci�n repetida con medici�n de tiempo.
r = 100000
t1 = clock()
for i in range(r):
    index = searcher.index(a, x)
t2 = clock()
for i in range(r):
    index = 0
t3 = clock()

t = ((t2 - t1) - (t3 - t2)) / r
print('Tiempo medio por ejecuci�n: {:.8f} segundos'.format(t))
#> full