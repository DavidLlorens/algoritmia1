#coding: latin1

#< intro
from random import gauss
from math import sqrt

class BrownianMotionpointsGenerator1:
    def points(self, a: "(R, R)", b: "(R, R)", v: "R") -> "Iterable<(R, R)>":
        def _recursion(pa: "(R, R)", pb: "(R, R)", v: "R"):
            ((xa, ya), (xb, yb)) = pa, pb
            if (xb-xa) <= 1:
                return
            else:
                delta = gauss(0, sqrt(v))
                (xc,yc) = ((xa+xb)/2.0, (ya+yb)/2.0 + delta)
                _recursion((xa,ya), (xc,yc), v/2)
                points.append((xc, yc))
                _recursion((xc,yc), (xb,yb), v/2)
        points = [a]
        _recursion(a, b, v)
        points.append(b)
        return points

#> intro

#< intro2
class BrownianMotionpointsGenerator:
    def points(self, a: "(R, R)", b: "(R, R)", v: "R") -> "Iterable<(R, R)>":
        def _recursion(pa, pb, v):
            ((xa, ya), (xb, yb)) = pa, pb
            if (xb-xa) <= 1:
                return []
            else:
                delta = gauss(0, sqrt(v))
                (xc,yc) = ((xa+xb)/2.0, (ya+yb)/2.0 + delta)
                return _recursion((xa,ya), (xc,yc), v/2) + [(xc,yc)] + \
                       _recursion((xc,yc), (xb,yb), v/2)
        return [a] + self._recursion(a, b, v) + [b]

#> intro2
