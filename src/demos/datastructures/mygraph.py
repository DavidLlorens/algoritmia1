#coding: latin1

#< full
class MyGraph:
    def __init__(self, n):
        self.n = n

    def __getattr__(self, attr):
        if attr == 'V':
            return range(self.n)
        elif attr == 'E':
            return ((u,v) for u in range(self.n) for v in range(u+1,self.n))

    def succs(self, u):
        return range(u+1, self.n)

    def preds(self, v):
        return range(0, v)

    def out_degree(self, u):
        return self.n - u - 1

    def in_degree(self, v):
        return v
    
if __name__ == "__main__":
    G = MyGraph(5)
    for v in G.V: print(v, end=" ")
    print()
    for (u, v) in G.E: print((u,v), end=" ")
    print()
    print(tuple(G.succs(1)))
    print(G.out_degree(1))
#> full