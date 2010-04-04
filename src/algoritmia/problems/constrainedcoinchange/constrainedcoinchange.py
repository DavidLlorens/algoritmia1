from algoritmia.utils import infinity, min

class CoinChanger: #[class
    def __init__(self, v, w, m, createMap=dict):
        self.v, self.w, self.m, self.n = v, w, m, len(v)
        self.createMap = createMap
        
    def weight(self, Q):
        L = self.createMap()
        for q in range(1, Q+1): L[q, 0] = infinity
        L[0, 0] = 0
        for n in range(1, self.n+1):
            for q in range(Q+1):
                L[q,n] = min((L[q-i*self.v[n-1],n-1] + i * self.w[n-1]
                             for i in range(min(q//self.v[n-1]+1, self.m[n-1]+1))), ifempty=infinity)
        return L[Q,self.n] #]class