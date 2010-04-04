#coding: latin1
from algoritmia.problems.sorting import BasicInPlaceQuickSorter #[]select1
from abc import ABCMeta, abstractmethod

class ISelector(metaclass=ABCMeta): #[interface
    @abstractmethod
    def select(self, a: "IList<T>", k: "int") -> "T": pass #]interface

class QuickSelector(ISelector): #[select1
    _partition = BasicInPlaceQuickSorter._partition

    def _quickselect(self, a: "IList<T>", k:"int", p: "int", r: "int") -> "T":
        if r - p == 1:
            return a[p]
        else:
            q = self._partition(a, p, r)
            if k == q: return a[q]
            elif k < q: return self._quickselect(a, k, p, q)
            else: return self._quickselect(a, k, q+1, r)

    def select(self, a: "IList<T>", k: "int") -> "T":
        if not (0 <= k < len(a)): raise IndexError(repr(k))
        return self._quickselect(a, k, 0, len(a)) #]select1

class MedianOf5Selector(object): #[select2
    def __init__(self, threshold: "int"=10):
        self.threshold = threshold
        
    def _median_of_5(self, a: "IList<T>", i: "int") -> "T":
        u, v, w, x = a[i], a[i+1], a[i+2], a[i+3]
        if v > u: 
            u, v = v, u
        if x > w: 
            w, x = x, w
        if u < w:
            u = a[i+4]
            if v > u: u, v = v, u
        else:
            w = a[i+4]
            if w > x: w, x = x, w
        if u < w:
            return v if v < w else w
        else:
            return x if x < u else u
        
    def select(self, a: "IList<T>", k: "int"):  
        if not (0 <= k < len(a)): raise IndexError(repr(k))
        if len(a) <= self.threshold:
            return sorted(a)[k]
        else:
            m = [self._median_of_5(a, i) for i in range(0, len(a), 5) if len(a)-i >= 5]
            pivot = self.select(m, len(m)//2)
            lessthan, equal = 0, 0
            for v in a:
                if v < pivot: lessthan += 1
                elif v == pivot: equal += 1
            if k < lessthan:
                return self.select([v for v in a if v < pivot], k)
            elif k >= lessthan+equal:
                return self.select([v for v in a if v > pivot], k-lessthan-equal)
            else:
                return pivot #]select2