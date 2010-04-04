from itertools import chain
from algoritmia.utils import infinity, min
from algoritmia.problems.generalizedcoinchange.dynamicprogramming3 import IterativeDynamicCoinChanger

class SpaceSavingDynamicCoinChanger2(IterativeDynamicCoinChanger):#[class
    def weight(self, Q: "int") -> "Real":
        mem = self.createMap()
        mem[0,0] = 0
        for q in range(1, Q+1): mem[q,0] = infinity
        for n in range(1, self.n+1):
            for q in range(Q+1):
                mem[q,n%2] = min((mem[q-i*self.v[n-1],(n-1)%2]+i*self.w[n-1]
                                          for i in range(q//self.v[n-1]+1)), ifempty=infinity)
        return mem[Q,self.n%2]#]class