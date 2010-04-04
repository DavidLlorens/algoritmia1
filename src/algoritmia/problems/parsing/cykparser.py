#coding: latin1

#< full
class CYKParser:
    def __init__(self, P: "IList<(str, str) or (str)>", S: "str", 
                 createMap: "IList<(str, str), int -> IMap<int, int, str>"=lambda P, n: dict()):
        self.P, self.S = P, S
        self.createMap = createMap

    def accepts(self, x: "str") -> "bool":
        n = len(x)
        Pi = self.createMap(self.P, n)
        for i in range(n):
            for A in self.P:
                Pi[i,i,A] = any(right[0] == x[i] for right in self.P[A] if len(right) == 1)
        for l in range(1, n):
            for i in range(0, n-l):
                for A in self.P:
                    Pi[i,i+l,A] = any(Pi[i,k,right[0]] and Pi[k+1,i+l,right[1]]
                                      for k in range(i,i+l) for right in self.P[A] if len(right) == 2)
        return Pi[0,n-1,self.S]
#> full
#< tree
    def parse_tree(self, x: "str") -> "ParseTree":
        n = len(x)
        Pi = self.createMap(self.P, n)
        back = self.createMap(self.P, n)
        for i in range(len(x)):
            for A in self.P:
                Pi[i,i,A], back[i,i,A] = False, None
                for right in self.P[A]:
                    if len(right) == 1 and right[0] == x[i]:
                        Pi[i,i,A], back[i,i,A] = True, x[i]
                        break
        for l in range(1, n):
            for i in range(0, n-l):
                for A in self.P:
                    Pi[i,i+l,A], back[i,i+l,A] = False, None
                    for right in self.P[A]:
                        if len(right) == 2:
                            for k in range(i,i+l):
                                if Pi[i,k,right[0]] and Pi[k+1,i+l,right[1]]:
                                    Pi[i,i+l,A], back[i,i+l,A] = True, (k, right[0], right[1])
                                    break
        def backtrace(i, k: "int", A: "str") -> "ParseTree":
            if len(back[i,k,A]) == 1: return back[i,k,A]
            j, B_prime, C_prime = back[i,k,A]
            return [A, backtrace(i,j,B_prime), backtrace(j+1,k,C_prime)]
        return backtrace(0, n-1, self.S)
#> tree