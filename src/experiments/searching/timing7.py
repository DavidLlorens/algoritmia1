#coding: latin1

#< full
from algoritmia.problems.searching import SequentialSearcher
from algoritmia.utils import chronometer
from random import seed, sample

tmin = 1 # Tiempo m�nimo de ejecuci�n: un segundo.
seed(0)
searcher = SequentialSearcher()
print('SequentialSearcher')
for n in range(1, 11):
    a = sorted(sample(range(5*n), n))
    for x in a:
        t = chronometer(tmin, searcher.index, a, x)
        print('({}, {:.8f}),'.format(n, t))
#> full