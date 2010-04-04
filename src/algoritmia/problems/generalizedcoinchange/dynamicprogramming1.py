from algoritmia.utils import infinity

class RecursiveDynamicCoinChanger:#[recursive
    def __init__(self, v: "IList<int>", w: "IList<Real>"=None):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n
        
    def weight(self, Q: "int") -> "Real":
        def L(q, n):
            if q == 0 and n==0: return 0
            if q > 0 and n == 0: return infinity
            return min((L(q-i*self.v[n-1],n-1)+i*self.w[n-1] for i in range(q//self.v[n-1]+1)))
        return L(Q, self.n)#]recursive
