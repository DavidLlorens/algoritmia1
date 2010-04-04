from algoritmia.semirings.interfaces import IIdempotentSemiRing

class _FuzzySemiRing(IIdempotentSemiRing):
    zero = property(lambda self: 0.0)
    one = property(lambda self: 1.0)
    def plus(self, left, right): return max(left, right)
    def times(self, left, right): return min(left, right)
    
FuzzySemiRing = _FuzzySemiRing()#]full