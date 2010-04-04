from algoritmia.semirings.interfaces import IIdempotentSemiRing

class _BooleanSemiRing(IIdempotentSemiRing):#[class
    zero = property(lambda self: False)
    one = property(lambda self: True)
    def plus(self, left, right): return left or right
    def times(self, left, right): return left and right
    
BooleanSemiRing = _BooleanSemiRing()#]class