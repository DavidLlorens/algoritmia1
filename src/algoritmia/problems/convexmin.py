#coding: latin1

#< cv1
class ConvexMin1:
    def min(self, a: "convex IList<T>") -> "T":
        if len(a) == 1:
            return a[0]
        elif len(a) == 2:
            return min(a[0], a[1])
        else:
            j = len(a) // 2
            if a[j-1] < a[j]: 
                return self.min(a[:j])
            else:
                return self.min(a[j:])
#> cv1

#< cv
class ConvexMin:
    def min(self, a: "convex IList<T>") -> "T":
        def _min(i: "int", k: "int") -> "T":
            if k - i == 1:
                return a[i]
            elif k - i == 2:
                return min(a[i], a[i+1])
            else:
                j = (i + k) // 2
                if a[j-1] < a[j]:
                    return _min(i, j)
                else:
                    return _min(j, k)
        
        return _min(0, len(a))

#> cv

#< cvit
class IterativeConvexMin:
    def min(self, a: "convex sequence of values"):
        i, k = 0, len(a)
        while k-i > 2:
            j = (i + k) // 2
            if a[j-1] < a[j]:
                k = j # No hace falta modificar el valor de $i$.
            else:
                i = j # No hace falta modificar el valor de $k$.
        return a[i] if k-i == 1 else min(a[i], a[i+1])
#> cvit