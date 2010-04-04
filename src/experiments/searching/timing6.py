#coding: latin1

#< full
from algoritmia.problems.searching import SequentialSearcher
from algoritmia.utils import chronometer
from random import seed, randrange, sample

tmin = 1 # Tiempo mínimo de ejecución: un segundo.
seed(0)
searcher = SequentialSearcher()
print('SequentialSearcher')
for n in range(1, 11):
    a = sorted(sample(range(5*n), n))
    x = a[randrange(n)]
    t = chronometer(tmin, searcher.index, a, x)
    print('{}\t{:.8f}'.format(n, t))
#> full