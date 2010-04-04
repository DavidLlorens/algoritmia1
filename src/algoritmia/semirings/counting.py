from algoritmia.semirings.interfaces import ISemiRing

class _CountingSemiRing(ISemiRing):#[class
    zero = property(lambda self: 1)
    one = property(lambda self: 1)
    def plus(self, left, right): return left + right
    def times(self, left, right): return left * right
    
CountingSemiRing = _CountingSemiRing()#]class