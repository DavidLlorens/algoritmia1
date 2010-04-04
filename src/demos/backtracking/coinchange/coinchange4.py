#coding: latin1
from algoritmia.problems.coinchange.backtracking4 import ChangeEnumerator #[main
from algoritmia.problems.coinchange.backtracking3 import MoneyChangeStateSpace3

space = MoneyChangeStateSpace3(11, [1,2,5,10])
for d in ChangeEnumerator().enumerate(space): print(d, end=" ") #]main
