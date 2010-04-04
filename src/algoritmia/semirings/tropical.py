from algoritmia.semirings.interfaces import IIdempotentSemiRing
from algoritmia.utils import infinity

class _MinTropicalSemiRing(IIdempotentSemiRing): #[full
    zero = property(lambda self: infinity)
    one = property(lambda self: 0)
    def plus(self, left, right): return min(left, right)
    def times(self, left, right): return left + right
    
class _MaxTropicalSemiRing(IIdempotentSemiRing):
    zero = property(lambda self: -infinity)
    one = property(lambda self: 0)
    def plus(self, left, right): return max(left, right)
    def times(self, left, right): return left + right 

MinTropicalSemiRing = _MinTropicalSemiRing()
MaxTropicalSemiRing = _MaxTropicalSemiRing()#]full