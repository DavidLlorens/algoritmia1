#coding: latin1
from algoritmia.problems.coinchange.backtracking1 import ChangeEnumerator #[full
from algoritmia.problems.coinchange.backtracking2 import MoneyChangeStateSpace2

space = MoneyChangeStateSpace2(11, [1,2,5,10])
ce = ChangeEnumerator()
for d in ce.enumerate(space): print(d)#]full
