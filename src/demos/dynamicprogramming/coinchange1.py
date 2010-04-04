#coding: latin1

#< full
from algoritmia.problems.generalizedcoinchange.dynamicprogramming1 import \
    RecursiveDynamicCoinChanger

print(RecursiveDynamicCoinChanger([1, 2, 5], [1, 1, 4]).weight(7))
#> full