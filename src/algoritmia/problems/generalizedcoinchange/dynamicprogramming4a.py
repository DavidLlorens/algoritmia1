from itertools import chain
from algoritmia.utils import infinity, min
from algoritmia.problems.generalizedcoinchange.dynamicprogramming3 import IterativeDynamicCoinChanger

class SpaceSavingDynamicCoinChanger(IterativeDynamicCoinChanger):#[class
    def weight(self, Q: "int") -> "Real":
        current = [0] + [infinity] * Q
        previous = [None] * (Q+1)
        for n in range(1, self.n+1):
            previous, current = current, previous
            for q in range(Q+1):
                current[q] = min((previous[q-i*self.v[n-1]] + i*self.w[n-1] \
                                          for i in range(q//self.v[n-1]+1)), ifempty=infinity)
        return current[Q]#]class
