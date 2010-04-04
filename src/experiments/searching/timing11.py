#coding: latin1

#< full
from algoritmia.problems.searching import BinarySearcher
from algoritmia.utils import chronometer
from random import seed, sample

tmin = 1 # Tiempo mínimo de ejecución: un segundo.
seed(0)
searcher = BinarySearcher()
print('BinarySearcher')
for n in [1] + list(range(10, 101, 10)):
    a = sorted(sample(range(5*n), n))
    for x in a:
        t = chronometer(tmin, searcher.index, a, x)
        print('({}, {:.8f}),'.format(n, t))
#> full