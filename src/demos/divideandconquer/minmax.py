#coding: latin1

#< full
from algoritmia.problems.orderstatistics.minmax import MinMaxFinder

a = [10, 8, 7, 5, 4, 3, 5, 9, 20]
print('M�nimo y m�ximo de {}: {}'.format(a, MinMaxFinder().min_max(a)))
#> full