#< memo
class MemoizedFibonacciNumbers:
    def __init__(self, createMap=lambda n: dict):
        self.createMap = createMap
            
    def number(self, n):
        mem = self.createMap(n)
        def F(n):
            if n == 0: return 0
            if n == 1: return 1
            if n-2 not in mem: mem[n-2] = F(n-2)
            if n-1 not in mem: mem[n-1] = F(n-1)
            return mem[n-2] + mem[n-1]
        return F(n)
#> memo
