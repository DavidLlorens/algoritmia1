from algoritmia.utils import infinity, min

class MemoizedDynamicCoinChanger:#[class
    def __init__(self, v: "IList<int>", w: "IList<Real>"=None):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n

    def weight(self, Q: "int") -> "Real":
        mem = [None] * (Q+1)
        def L(q):
            if q == 0: return 0
            for i in range(self.n):
                if self.v[i] <= q and q-self.v[i] not in mem: 
                    mem[q-self.v[i]] = L(q-self.v[i])
            return min((mem[q-self.v[i]]+self.w[i] for i in range(self.n) if self.v[i]<=q), 
                            ifempty=infinity)
        if Q not in mem:
            mem[Q] = L(Q)
        return mem[Q]#]class
