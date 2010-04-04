#coding: latin1
 
from algoritmia.problems.sorting.interfaces import ISorter, IInPlaceSorter
from algoritmia.schemes.divideandconquer import IDivideAndConquerProblem

class MergeSorter(ISorter): #[mergesort
    def sorted(self, a: "IList<T>") -> "sorted Iterable<T>":
        if len(a) <= 1:
            return a
        else:
            return self.merge(self.sorted(a[:len(a)//2]), self.sorted(a[len(a)//2:])) 

    def merge(self, a: "sorted IList<T>", b: "sorted IList<T>") -> "sorted IList<T>": 
        c = [None] * (len(a)+len(b))
        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]: c[k] = a[i]; i += 1
            else: c[k] = b[j]; j += 1
            k += 1
        while i < len(a): c[k] = a[i]; i += 1; k += 1    
        while j < len(b): c[k] = b[j]; j += 1; k += 1
        return c #]mergesort

class InPlaceMergeSorter(IInPlaceSorter):#[inplace
    def sort(self, a: "IList<T>"):
        def _mergesort(p, q, c):
            if q-p > 1:
                _mergesort(p, (p+q)//2, c)
                _mergesort((p+q)//2, q, c)
                self.merge(a, p, q, c) 
        _mergesort(0, len(a), [None]*len(a))
    
    def merge(self, a: "IList<T>", p: "int", q: "int", c: "IList<T>"): 
        # Funde los «subvectores» $v\mathtt{[}p\mathtt{:}(p+q)//2\mathtt{]}$ y $v\mathtt{[}(p+q)//2\mathtt{:}q\mathtt{]}$.
        i, j, k = p, (p+q)//2, p
        while i < (p+q)//2 and j < q:
            if a[i] < a[j]: c[k] = a[i]; i += 1
            else: c[k] = a[j]; j += 1
            k += 1
        while i < (p+q)//2: c[k] = a[i]; i += 1; k += 1    
        while j < q: c[k] = a[j]; j += 1; k += 1
        for k in range(p, q): a[k] = c[k]#]inplace
    

class MergesortProblem(IDivideAndConquerProblem): #[mergesortfromscheme
    def __init__(self, a: "IList<T>"):
        self.a = a
        
    def is_simple(self) -> "bool":
        return len(self.a) <= 1

    def trivial_solution(self) -> "sorted IList<T>":
        return self.a

    def divide(self) -> "Iterable<MergesortProblem>":
        yield MergesortProblem(self.a[:len(self.a)//2])
        yield MergesortProblem(self.a[len(self.a)//2:])

    def combine(self, s: "Iterable<sorted IList<T>>") -> "sorted IList<T>":
        a, b = tuple(s)
        c = [None] * (len(a)+len(b))
        i, j, k = 0, 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]: c[k] = a[i]; i += 1
            else: c[k] = b[j]; j += 1
            k += 1
        while i < len(a): c[k] = a[i]; i += 1; k += 1
        while j < len(b): c[k] = b[j]; j += 1; k += 1
        return c #]mergesortfromscheme

class InPlaceMergesortProblem(IDivideAndConquerProblem): #[inplacefromscheme
    def __init__(self, a: "IList<T>", p: "int"=0, q: "int or None"=None, 
            c: "IList<T> or None"=None):
        self.a = a
        if q == None: q, c = len(a), a[:]
        self.p, self.q = p, q
        self.c = c
        
    def is_simple(self) -> "bool":
        return self.q - self.p <= 1

    def trivial_solution(self) -> "InPlaceMergesortProblem":
        return self 

    def divide(self) -> "Iterable<InPlaceMergesortProblem>":
        middle = (self.p + self.q) // 2
        yield InPlaceMergesortProblem(self.a, self.p, middle, self.c)
        yield InPlaceMergesortProblem(self.a, middle, self.q, self.c)

    def combine(self, s: "Iterable<InPlaceMergesortProblem>"
            ) -> "InPlaceMergesortProblem":
        a, b = tuple(s)
        i, j, k = a.p, b.p, a.p
        while i < a.q and j < b.q:
            if self.a[i] < self.a[j]: self.c[k] = self.a[i]; i += 1
            else: self.c[k] = self.a[j]; j += 1
            k += 1
        while i < a.q: self.c[k] = self.a[i]; i += 1; k += 1    
        while j < b.q: self.c[k] = self.a[j]; j += 1; k += 1
        for k in range(a.p, b.q): self.a[k] = self.c[k]
        return self #]inplacefromscheme

class ThresholdedInPlaceMergeSorter(InPlaceMergeSorter): #[mergethreshold
    def __init__(self, threshold: "int"):
        self.threshold = threshold

    def sort(self, a: "IList<T>"):
        def _mergesort(p: "int", q: "int", c: "IList<T>"):
            if q-p > self.threshold:
                _mergesort(p, (p+q)//2, c)
                _mergesort((p+q)//2, q, c)
                self.merge(a, p, q, c)
            elif q-p <= self.threshold:
                for i in range(p, q): # Insertion Sort
                    x = a[i]
                    j = i-1
                    while j >= 0 and x < a[j]:
                        a[j+1] = a[j]
                        j -= 1
                    a[j+1] = x 
        _mergesort(0, len(a), [None]*len(a))#]mergethreshold


