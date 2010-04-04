from algoritmia.problems.generalizedcoinchange.dynamicprogramming4a import SpaceSavingDynamicCoinChanger
from algoritmia.utils import infinity, argmin

class DynamicCoinChanger(SpaceSavingDynamicCoinChanger):#[class
    def __init__(self, v: "IList<int>", w: "IList<Number>"=None):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n

    def change(self, Q: "int") -> "IList<int>": 
        mem, back = [None] * (Q+1), [None] * (Q+1)
        mem[0] = 0
        for q in range(1, Q+1):
            i_prime = argmin((i for i in range(self.n) if self.v[i] <= q), 
                                        lambda i: mem[q-self.v[i]] + self.w[i])
            mem[q] = mem[q - self.v[i_prime]] + self.w[i_prime]
            back[q] = q - self.v[i_prime]
        if mem[Q] == infinity:
            return []
        coins = []
        q = Q
        while back[q] != None:
            coins.append(q-back[q])
            q = back[q]
        return coins #]class