#coding: latin1

#< full
from algoritmia.problems.sorting import ThresholdedInPlaceMergeSorter

a = [11, 21, 3, 1, 98, 0, 12, 82, 29, 30, 11, 18, 43, 4, 75, 37]
ThresholdedInPlaceMergeSorter(5).sort(a)
print('Ordenado:', a)
#> full