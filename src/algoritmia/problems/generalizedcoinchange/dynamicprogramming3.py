from algoritmia.utils import infinity, min
from itertools import chain
from algoritmia.problems.generalizedcoinchange.dynamicprogramming2 import MemoizedDynamicCoinChanger

class IterativeDynamicCoinChanger(MemoizedDynamicCoinChanger):#[class
    def weight(self, Q: "int") -> "Real":
        mem = self.createMap()
        mem[0,0] = 0
        for q in range(1, Q+1): mem[q,0] = infinity
        for n in range(1, self.n+1):
            mem[0, n] = 0
            for q in range(1, Q+1):
                mem[q, n] = min((mem[q-i*self.v[n-1],n-1]+i*self.w[n-1] \
                                             for i in range(q // self.v[n-1]+1)), ifempty=infinity)
        return mem[Q, self.n]#]class