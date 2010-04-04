from algoritmia.utils import infinity

class MemoizedDynamicCoinChanger: #[class
    def __init__(self, v: "IList<int>", w: "IList<Real>"=None, 
                 createMap: "-> IMap<(int, int), Real>"=dict):
        self.v, self.w, self.n = v, w, len(v)
        if w == None: self.w = [1] * self.n
        self.createMap = createMap
        
    def weight(self, Q: "int") -> "Real":
        mem = self.createMap()
        def L(q, n):
            if q == 0: return 0
            if n == 0: return infinity
            for i in range(q // self.v[n-1]+1):
                if (q-i*self.v[n-1],n-1) not in mem:
                    mem[q-i*self.v[n-1],n-1] = L(q-i*self.v[n-1],n-1)
            return min(mem[q-i*self.v[n-1],n-1]+i*self.w[n-1] for i in range(q//self.v[n-1]+1))
        mem[Q,self.n] = L(Q,self.n)
        return mem[Q,self.n] #]class
