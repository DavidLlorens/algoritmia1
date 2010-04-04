from algoritmia.utils import infinity, min
from algoritmia.problems.generalizedcoinchange.dynamicprogramming7 import MemoizedDynamicCoinChanger

class IterativeDynamicCoinChanger(MemoizedDynamicCoinChanger):#[class
    def weight(self, Q: "int") -> "Real":
        mem = [0] + [None] * Q
        for q in range(1, Q+1):
            mem[q] = min((mem[q-self.v[i]] + self.w[i] for i in range(self.n) if self.v[i] <= q), 
                            ifempty=infinity)
        return mem[Q]#]class
