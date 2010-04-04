from algoritmia.problems.geometry.utils import Point2D, left
from algoritmia.utils import argmax
from algoritmia.datastructures.queues.lifo import Lifo
from math import atan2

#< graham
class GrahamConvexHullFinder:
    def find(self, S: "IList<Point2D>") -> "IList<int>":
        S1 = S = [Point2D(*p) for p in S]
        min_y = min(pt.y for pt in S)
        p = argmax((pt for pt in S if pt.y == min_y), lambda pt: pt.x)
        S = [p] + sorted((q for q in S if q!=p), key=lambda q: (atan2(p.y-q.y, p.x-q.x), q.x))
        Q = Lifo()
        Q.push(0); Q.push(1); Q.push(2)
        for pi in range(3, len(S)):
            pj, pk = Q[-1], Q[-2]
            while not left(S[pk], S[pj], S[pi]):
                Q.pop()
                pj, pk = Q[-1], Q[-2]
            Q.push(pi)
        return [S1.index(S[Q.pop()]) for i in range(len(Q))]
#> graham