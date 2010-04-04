#coding: latin1
from math import sqrt

#< full
class DynamicTimeWarper:
    def __init__(self, d: "T, T -> Number"
                    =lambda v, w: sqrt((v[0]-w[0])**2 + (v[1]-w[1])**2)):
        self.d = d
             
    def distortion(self, a: "IList<T>", b: "IList<T>") -> "Number":
        D = [[None] * (1+len(b)) for _ in range(1+len(a))]
        D[0][0] = self.d(a[0], b[0])
        for i in range(1, len(a)): D[i][0] = D[i-1][0] + self.d(a[i], b[0])
        for j in range(1, len(b)):
            D[0][j] = D[0][j-1] + self.d(a[0], b[j])
            for i in range(1, len(a)):
                D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + self.d(a[i],b[j])
        return D[len(a)-1][len(b)-1]
#> full