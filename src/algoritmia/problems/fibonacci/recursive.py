#< rec
class RecursiveFibonacciSeries:
    def number(self, n: "int") -> "int":
        def F(n: "int") -> "int":
            if n == 0: return 0
            if n == 1: return 1
            return F(n-2) + F(n-1)
        return F(n)
#> rec