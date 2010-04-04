#coding: latin1

#< full
from algoritmia.problems.orderstatistics.selecting import MedianOf5Selector

v = [1, 6, 8, 56, 12, 9, 48, 0, 23, 40, 2, 31, 23, 7, 87, 18]
print('Ordenado  :', sorted(v))
print('Con select:', [MedianOf5Selector().select(v[:], i) for i in range(len(v))])
#> full