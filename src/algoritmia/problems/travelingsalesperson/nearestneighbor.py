from algoritmia.utils import argmin
from math import sqrt

def d(a: "IList<Real>", b: "IList<Real>") -> "Real":#[nn
    return sqrt(sum((a[i]-b[i])**2 for i in range(len(a))))

class NearestNeighborTravelingSalesPerson:
    def travel(self,  points: "IList<(Real, Real)>") -> "Iterable<(Real, Real)>":
        path = [ points[0] ]
        unvisited = set(points[1:])
        while len(unvisited) > 0:
            nn = argmin(unvisited, lambda xy: d(path[-1], xy))
            unvisited.remove(nn)
            path.append(nn)
        path.append(points[0])
        return path#]nn