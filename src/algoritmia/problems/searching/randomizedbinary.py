#coding: latin1

#< full
from random import randrange
from algoritmia.problems.searching import ISortedSearcher

class RandomizedBinarySearcher(ISortedSearcher):
    def index(self, a, v):
        def _index(i, k):
            if k-i == 1:
                if v == a[i]: return i
            elif k-i > 1:
                j = randrange(i, k)
                if v == a[j]:   return j #?return?¶return?
                elif v < a[j]:  return _index(i, j) #?return?»return?
                else:           return _index(j+1, k) #?return?»return?
            return None
        return _index(0, len(a))
#> full