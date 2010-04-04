#coding: latin1

#< full
from algoritmia.problems.searching import NaiveSequentialSearcher
from algoritmia.utils import chronometer 
from random import seed, randrange, sample

tmin = 2 # Tiempo m�nimo de ejecuci�n: dos segundos.
seed(0)
n = 100
a = sorted(sample(range(5*n), n))
x = a[randrange(n)]
searcher = NaiveSequentialSearcher()
t = chronometer(tmin, searcher.index, a, x)
print('Tiempo medio por ejecuci�n: {:.8f} segundos'.format(t))
#> full