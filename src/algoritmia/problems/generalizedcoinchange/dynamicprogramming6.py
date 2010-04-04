from algoritmia.utils import infinity, min

class RecursiveDynamicCoinChanger:#[class
    def __init__(self, v: "IList<int>", w: "IList<Real>"=None):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n

    def weight(self, Q: "int") -> "Real":
        def L(q: "int") -> "Real":
            if q == 0: return 0
            return min((L(q-self.v[i])+self.w[i] for i in range(self.n) if self.v[i] <= q), 
                            ifempty=infinity)
        return L(Q)#]class
