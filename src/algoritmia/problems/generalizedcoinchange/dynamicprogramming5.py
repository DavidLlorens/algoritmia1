from itertools import chain
from algoritmia.utils import infinity, argmin
from algoritmia.problems.generalizedcoinchange.dynamicprogramming4a import SpaceSavingDynamicCoinChanger

class DynamicCoinChanger(SpaceSavingDynamicCoinChanger):#[class
    def change(self, Q: "int") -> "Real":
        mem = self.createMap()
        mem[0,0] = 0
        for q in range(1, Q+1): mem[q,0] = infinity
        back = self.createMap()
        for n in range(1, self.n+1):
            for q in range(Q+1):
                i_prime = argmin(range(q//self.v[n-1]+1), 
                                        lambda i: mem[q-i*self.v[n-1],n-1]+i*self.w[n-1])
                mem[q, n] = mem[q-i_prime*self.v[n-1],n-1]+i_prime*self.w[n-1]
                back[q, n] = i_prime
        (q, n) = (Q, self.n)
        decisions = []
        while (q, n) in back:
            i = back[q, n]
            q, n = q-i*self.v[n-1], n-1
            decisions.append(i)
        decisions.reverse()
        return decisions#]class