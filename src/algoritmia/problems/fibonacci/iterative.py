
#< it
class IterativeFibonacciNumbers:
    def __init__(self, createMap=lambda n: dict):
        self.createMap = createMap

    def number(self, n):
        F = self.createMap(n) 
        F[0] = F[1] = 0
        for i in range(2, n+1):
            F[i] = F[i-2] + F[i-1]
        return F[n]
#> it
