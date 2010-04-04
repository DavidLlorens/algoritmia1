#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.dynamicprogramming2 import MemoizedDynamicCoinChanger

print(MemoizedDynamicCoinChanger([1, 2, 5], [1, 1, 4]).weight(7))
#> full