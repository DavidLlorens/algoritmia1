from algoritmia.problems.generalizedcoinchange.dynamicprogramming4a import SpaceSavingDynamicCoinChanger
from algoritmia.utils import infinity, min

class DynamicCoinChanger(SpaceSavingDynamicCoinChanger):#[class
    def __init__(self, v: "IList<int>", w: "IList<Real>"=None):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n
        self.maxmem = max(v)

    def weight(self, Q: "int") -> "Real":
        memlen = min(Q, max(self.v)) + 1
        mem = [0] * memlen
        for q in range(1, Q+1):
            mem[q%memlen] = min((mem[(q-self.v[i])%memlen] + self.w[i] 
                                 for i in range(self.n) if self.v[i] <= q), 
                                ifempty=infinity)
        return mem[Q%memlen]#]class