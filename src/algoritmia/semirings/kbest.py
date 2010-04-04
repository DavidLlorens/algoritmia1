from algoritmia.semirings.interfaces import ISemiRing
from algoritmia.utils import infinity

class KMinTropicalSemiRing(ISemiRing): #[kmin
    def __init__(self, k):   
        self.k = k

    zero = property(lambda self: (infinity,) * self.k)
    one = property(lambda self: (0,) + (infinity,) * (self.k-1))

    def plus(self, left, right):
        result = [None] * self.k
        i, j, m = 0, 0, 0
        while i < len(left) and j < len(right) and m < self.k:
            if left[i] < right[j]: result[m] = left[i]; i += 1
            else: result[m] = right[j]; j += 1
            m += 1
        while i < self.k and m < self.k: result[m] = left[i]; i += 1; m += 1    
        while j < self.k and m < self.k: result[m] = right[j]; j += 1; m += 1
        return tuple(result)

    def times(self, left, right):
        return tuple(a + right for a in left) #]kmin