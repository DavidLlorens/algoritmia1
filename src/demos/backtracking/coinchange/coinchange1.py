#coding: latin1
from itertools import islice#[full
from algoritmia.problems.coinchange.backtracking1 import *

ce = ChangeEnumerator()
space = MoneyChangeForwardStateSpace(11, [1,2,5,10])
for d in islice(ce.enumerate(space), 10): print(d) 
print("...")#]full