#coding: latin1

#< full
from algoritmia.problems.searching import NaiveSequentialSearcher
from time import clock
from random import seed, randrange, sample

# Generación de un vector aleatorio.
seed(0)                                     # Semilla del generador de números aleatorios. #?#?¶#?
n = 100                                     # Talla del vector. #?#?»#?
a = sorted(sample(range(5*n), n))           # Vector ordenado de $n$ valores aleatorios sin #?#?»#?
                                            # repetición en el rango $[0..5n-1]$.           #?#?»#?
x = a[randrange(n)]                         # Selección de un elemento al azar. #?#?»#?
searcher = NaiveSequentialSearcher()

# Ejecución con medición de tiempo.
t1 = clock() 
index = searcher.index(a, x)
t2 = clock()
t = t2 - t1

print('Tiempo transcurrido: {:.8f} segundos'.format(t))
#> full