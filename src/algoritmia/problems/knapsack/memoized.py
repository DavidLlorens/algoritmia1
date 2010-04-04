#< memo
class MemoizedKnaspsackSolver:
    def __init__(self, createMap=lambda N, W: dict()):
        self.createMap = createMap
        
    def profit(self, W, v, w):
        N = len(v)
        mem = self.createMap(N, W)
        def B(n, c):
            if n==0: return 0
            if c-w[n-1] >= 0:
                if (n-1, c) not in mem: mem[n,c] = B(n-1, c)
                if (n-1, c-w[n-1]) not in mem: mem[n,c] = B(n-1, c-w[n-1])
                return max(mem[n-1,c], mem[n-1, c-w[n-1]] + v[n-1])
            else:
                if (n-1, c) not in mem: mem[n-1, c] = B(n-1, c)
                return mem[n-1, c]
        if (N, W) not in mem:
            mem[N, W] = B(N, W)
        return mem[N, W]
#> memo