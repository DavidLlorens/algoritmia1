#coding: latin1

from algoritmia.schemes.decreaseandconquer import IDecreaseAndConquerProblem
from algoritmia.problems.searching.interfaces import ISortedSearcher

class BinarySearcher(ISortedSearcher):#[alg
    def index(self, a: "sorted IList<T>", x: "T") -> "int or None":
        left, right = 0, len(a)
        while left < right:
            i = (right + left) // 2
            if x == a[i]:
                return i
            elif x < a[i]: 
                right = i
            else: 
                left = i + 1
        return None #]alg

class RecursiveBinarySearcher(ISortedSearcher):#[Recursivebinarysearch 
    def index(self, a: "sorted IList<T>", x: "T") -> "int or None":
        def _binary_search(left: "int", right: "int") -> "int or None":
            if left < right:
                i = (right + left) // 2
                if a[i] == x:
                    return i
                elif a[i] > x:
                    return _binary_search(left, i)
                else:
                    return _binary_search(i+1, right)
            else:
                return None 
        return _binary_search(0, len(a))#]Recursivebinarysearch
    

class BinarySearchProblem(IDecreaseAndConquerProblem): #[binsearchfromscheme
    def __init__(self, a: "sorted IList<T>", v: "T", i: "int"=0, k: "int or None"=None):
        if k == None: k = len(a)
        self.a, self.v, self.i, self.k = a, v, i, k
            
    def is_simple(self) -> "bool":
        return self.k - self.i <= 1

    def trivial_solution(self) -> "int or None":
        if self.i == self.k or self.v != self.a[self.i]: return None
        return self.i

    def decrease(self) -> "BinarySearchProblem":
        j = (self.i + self.k) // 2
        if self.v < self.a[j]: return BinarySearchProblem(self.a, self.v, self.i, j)
        elif self.v == self.a[j]: return BinarySearchProblem(self.a, self.v, j, j+1)
        else: return BinarySearchProblem(self.a, self.v, j+1, self.k) #]binsearchfromscheme

class ThresholdedBinarySearcher(ISortedSearcher): #[binsearchthreshold
    def __init__(self, threshold: "int"):
        self.threshold = threshold 
        
    def index(self, a: "sorted IList<T>", v: "T") -> "int or None":
        def _index(i: "int", k: "int") -> "int or None":
            if k-i <= self.threshold:
                for j in range(i, k):
                    if v == a[j]: return j
                return None
            else:
                j = (i + k) // 2
                if v == a[j]:   return j #?return?¶return?
                elif v < a[j]:  return _index(i, j) #?return?»return?
                else:           return _index(j+1, k) #?return?»return? 
        return _index(0, len(a)) #]binsearchthreshold

class IterativeBinarySearcher(ISortedSearcher):#[binsearchiterative
    def index(self, a: "sorted IList<T>", v: "T") -> "int or None":
        i, k = 0, len(a)
        while k-i > 1 and a[(i+k)//2] != v:
            j = (i+k) // 2
            if v < a[j]: k = j
            if v > a[j]: i = j+1
        return (i+k)//2 if k-i >= 1 and a[(i+k)//2] == v else None #]binsearchiterative