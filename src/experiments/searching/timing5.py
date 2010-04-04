#coding: latin1

#< full
from algoritmia.problems.searching import NaiveSequentialSearcher
from algoritmia.utils import chronometer
from random import seed, randrange, sample

tmin = 1 # Tiempo mínimo de ejecución: un segundo.
seed(0)
searcher = NaiveSequentialSearcher()
print('NaiveSequentialSearcher')
for n in range(1, 11):
    a = sorted(sample(range(5*n), n))
    x = a[randrange(n)]
    t = chronometer(tmin, searcher.index, a, x)
    print('Tiempo medio por ejecución n={:2d}: {:.8f} segundos'.format(n, t))
#> full
    #print('{}\t{:.8f}'.format(n, t).replace('.', ','))
