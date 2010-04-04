
#< it2
class SpaceSavingFibonacciNumbers:
    def number(self, n):
        if n == 0: return 0
        if n == 1: return 1
        prev2, prev1 = 0, 1
        for _ in range(2, n+1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr
        return curr
#> it2

#< it3
class SpaceSavingFibonacciNumbers2:
    def fibonacci(self, n):
        if n == 0: return 0
        if n == 1: return 1
        prev, curr = 0, 1
        for _ in range(2, n+1):
            prev, curr = curr, prev + curr
        return curr
#> it3