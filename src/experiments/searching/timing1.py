#coding: latin1

#< full
from algoritmia.problems.searching import NaiveSequentialSearcher
from time import clock
from random import seed, randrange, sample

# Generaci�n de un vector aleatorio.
seed(0)                                     # Semilla del generador de n�meros aleatorios. #?#?�#?
n = 100                                     # Talla del vector. #?#?�#?
a = sorted(sample(range(5*n), n))           # Vector ordenado de $n$ valores aleatorios sin #?#?�#?
                                            # repetici�n en el rango $[0..5n-1]$.           #?#?�#?
x = a[randrange(n)]                         # Selecci�n de un elemento al azar. #?#?�#?
searcher = NaiveSequentialSearcher()

# Ejecuci�n con medici�n de tiempo.
t1 = clock() 
index = searcher.index(a, x)
t2 = clock()
t = t2 - t1

print('Tiempo transcurrido: {:.8f} segundos'.format(t))
#> full