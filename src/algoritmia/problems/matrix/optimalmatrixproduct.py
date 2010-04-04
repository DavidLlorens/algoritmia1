#coding: latin1

#< flops
class OptimalMatrixProduct:
    def __init__(self, createMap: "-> IMap<(int, int), int>"=lambda n: dict()):
        self.createMap = createMap
        
    def flops(self, dim: "IList<(int, int)>") -> "int":
        n = len(dim)
        P = self.createMap(n)
        for i in range(n): P[i,i] = 0
        for l in range(1, n):
            for i in range(0, n-l):
                P[i,i+l] = min(P[i,j] + dim[i][0]*dim[j][1]*dim[i+l][1] + P[j+1,i+l]
                                               for j in range(i,i+l))
        return P[0,n-1]
#> flops
#< par
    def parenthesized(self, dim: "IList<(int, int)>") -> "Parenthesization":
        n = len(dim)
        P = self.createMap(n)
        for i in range(n): P[i,i] = 0
        back = self.createMap(n)
        for i in range(n): back[i,i] = None
        for l in range(1, n):
            for i in range(0, n-l):
                P[i,i+l],back[i,i+l]=min((P[i,j]+dim[i][0]*dim[j][1]*dim[i+l][1]+P[j+1,i+l],j)
                                                     for j in range(i, i+l) )
        def backtrace(i: "int", k: "int") -> "Parenthesization":
            j = back[i,k]
            return (backtrace(i,j), backtrace(j+1,k)) if j != None else i
        return backtrace(0, n-1)
#> par