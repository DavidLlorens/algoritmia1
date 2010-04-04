from itertools import chain
from algoritmia.utils import infinity, min
from algoritmia.problems.generalizedcoinchange.dynamicprogramming8 import IterativeDynamicCoinChanger

class SpaceSavingDynamicCoinChanger(IterativeDynamicCoinChanger):#[class
    def __init__(self, v: "IList<int>", w: "IList<Real>"=None):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n
        self.maxmem = max(v)

    def weight(self, Q: "int") -> "Real":
        memlen = max(self.maxmem, Q)
        mem = [None] * memlen
        mem[0] = 0
        for q in range(1, Q+1):
            mem[q%memlen] = min((mem[(q-self.v[i])%memlen] + self.w[i] 
                                 for i in range(self.n) if self.v[i] <= q), ifempty=infinity)
        return mem[Q%memlen]#]class
#]cl