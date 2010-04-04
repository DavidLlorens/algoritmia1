#coding: latin1
from algoritmia.utils import argmax
from algoritmia.problems.geometry.utils import triangle_area, left, right

#< qh
class QuickHullFinder:
    def quickhull(self, S: "IList<(T, T)>") -> "Iterable<int>":
        if len(S) <= 2: return list(S)
        p, q = min(S), max(S)
        qhull = self._quickhull(p, [z for z in S if z != p and z != q and left(p, q, z)], q)[1:] + \
                self._quickhull(q, [z for z in S if z != p and z != q and right(p, q, z)], p)[1:]
        return qhull

    def _quickhull(self, p, A, q):
        if len(A) == 0: return [p, q]
        h = argmax(A, lambda z: triangle_area(p,q,z))
        return self._quickhull(p, [z for z in A if left(p, h, z)],h) + \
               self._quickhull(h, [z for z in A if left(h, q, z)],q)[1:]
#> qh
