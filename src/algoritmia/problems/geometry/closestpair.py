#coding: latin1

from algoritmia.utils import infinity
from math import sqrt 

def d(a: "(T, T)", b: "(T, T)") -> "R": #[brute
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

class BruteForceClosestPointsFinder:
    def distance_between_closest_points(self, z: "IList<(T, T)>") -> "R":
        return min(d(z[i], z[j]) for i in range(len(z)) for j in range(i+1, len(z)))

    def closest_points(self, z: "IList<(T, T)>") -> "((T, T), (T, T))":
        return min((d(z[i], z[j]), (z[i], z[j])) \
            for i in range(len(z)) for j in range(i+1, len(z)))[1] #]brute

class ClosestPointsFinder1: #[min1
    def distance_between_closest_points(self, z: "IList<(T, T)>") -> "R":
        def _minimum_distance(p: "int", r: "int") -> "R":
            if r - p < 2:
                return infinity
            elif r - p == 2:
                return d(z[x[p]], z[x[p+1]])
            else:
                q = (p + r) // 2
                d1 = _minimum_distance(p, q)
                d2 = _minimum_distance(q, r)
                d3 = min(d(z[x[i]], z[x[j]]) for i in range(p, q) for j in range(q, r))
                return min(d1, d2, d3)
        x = [i for (v, i) in sorted((z[0], i) for i in range(len(z)))]        
        return _minimum_distance(0, len(z)) #]min1
    
    def closest_points(self, z: "IList<(T, T)>") -> "((T, T), (T, T))":
        def _closest_points(p: "int", r: "int") -> "((T, T), (T, T))":
            if r - p < 2:
                return (infinity, (None, None))
            elif r - p == 2:
                return (d(z[x[p]], z[x[p+1]]), (z[x[p]], z[x[p+1]]))
            else:
                q = (p + r) // 2
                (d1, (p1a, p1b)) = _closest_points(p, q)
                (d2, (p2a, p2b)) = _closest_points(q, r)
                (d3, (p3a, p3b)) = min((d(z[x[i]], z[x[j]]), (z[x[i]], z[x[j]])) \
                    for i in range(p, q) for j in range(q, r))
                if d1 < d2:
                    if d1 < d3:
                        return (d1, (p1a, p1b))
                    else:
                        return (d3, (p3a, p3b))
                else:
                    if d2 < d3:
                        return (d2, (p2a, p2b))
                    else:
                        return (d3, (p3a, p3b))
        x = [i for (v, i) in sorted((z[0], i) for i in range(len(z)))]
        return _closest_points(0, len(z))[1]

class ClosestPointsFinder:#[min2 #[]pair
    def distance_between_closest_points(self, z: "IList<(T, T)>") -> "R":
        def _minimum_distance(x: "IList<int>", y: "IList<int>") -> "R":
            if len(x) <= 1: 
                return infinity
            elif len(x) == 2:
                return d(z[x[0]], z[x[1]])
            else:
                splitter = (z[x[len(x)//2-1]][0] + z[x[len(x)//2]][0])/2
                x1, x2 = [i for i in x if z[i][0] <= splitter], [i for i in x if z[i][0] > splitter]
                y1, y2 = [i for i in y if z[i][0] <= splitter], [i for i in y if z[i][0] > splitter]
                d1 = _minimum_distance(x1, y1)
                d2 = _minimum_distance(x2, y2)
                delta = min(d1, d2)
                strip = [i for i in y if abs(z[i][0] - splitter) < delta]
                for i in range(len(strip)):
                    for j in range(i+1, len(strip)):
                        if abs(z[strip[j]][1] - z[strip[i]][1]) > delta: break
                        delta = min(delta, d(z[strip[i]], z[strip[j]]))
            return delta
        x = [i for (v,i) in sorted([(z[i][0], i) for i in range(len(z))])]
        y = [i for (v,i) in sorted([(z[i][1], i) for i in range(len(z))])]
        return _minimum_distance(x, y) #]min2

    def closest_points(self, z: "IList<(T, T)>") -> "((T, T), (T, T))":#[pair
        def _closest_pair(x: "IList<int>", y: "IList<int>") -> "((T, T), (T, T))":
            if len(x) <= 1: 
                return (None, None, infinity)
            elif len(x) == 2:
                return (z[x[0]], z[x[1]], d(z[x[0]], z[x[1]]))
            else:
                splitter = (z[x[len(x)//2-1]][0] + z[x[len(x)//2]][0])/2
                x1, x2 = [i for i in x if z[i][0] <= splitter], [i for i in x if z[i][0] > splitter]
                y1, y2 = [i for i in y if z[i][0] <= splitter], [i for i in y if z[i][0] > splitter]
                (p1, q1, d1) = _closest_pair(x1, y1)
                (p2, q2, d2) = _closest_pair(x2, y2)
                (p, q, delta) = (p1, q1, d1) if d1 < d2 else (p2, q2, d2)
                strip = [i for i in y if abs(z[i][0] - splitter) < delta]
                for i in range(len(strip)):
                    for j in range(i+1, len(strip)):
                        if abs(z[strip[j]][1] - z[strip[i]][1]) > delta: break
                        dij = d(z[strip[i]], z[strip[j]])
                        if dij < delta: p, q, delta = z[strip[i]], z[strip[j]], dij
            return (p, q, delta)
        x = [i for (v,i) in sorted([(z[i][0], i) for i in range(len(z))])]
        y = [i for (v,i) in sorted([(z[i][1], i) for i in range(len(z))])]
        return _closest_pair(x, y)[:2] #]pair