from algoritmia.problems.sorting.interfaces import IInPlaceSorter, ISorter
from random import randrange

class InPlaceQuickSorter(IInPlaceSorter):#[three
    def sort(self, a: "IList<T>"):
        def _quicksort(p: "int", r: "int"):
            while r - p > 1:
                pivot = a[r-1]
                i = p - 1
                for j in range(p, r-1):
                    if a[j] <= pivot:
                        i += 1
                        a[i], a[j] = a[j], a[i]
                a[i+1], a[r-1] = a[r-1], a[i+1]
                pivot_index = i + 1 
                if r - pivot_index < pivot_index - p:
                    _quicksort(pivot_index+1, r)
                    r = pivot_index
                else:
                    _quicksort(p, pivot_index)
                    p = pivot_index + 1
        _quicksort(0, len(a))#]three

                
                
class BasicQuickSorter(ISorter): #[quicksort1
    def sorted(self, a: "IList<T>") -> "sorted Iterable<T>": 
        if len(a) <= 1:
            return a
        else:
            pivot = a[0]
            left = [x for x in a if x < pivot]
            right = [x for x in a[1:] if x >= pivot]
            return self.sorted(left) + [pivot] + self.sorted(right) #]quicksort1

class BasicInPlaceQuickSorter(IInPlaceSorter): #[partition
    def _partition(self, a: "IList<T>", p: "int", r: "int") -> "int": 
        pivot = a[r-1]
        i = p - 1
        for j in range(p, r-1):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[r-1] = a[r-1], a[i+1]
        return i + 1 

    def _quicksort(self, a: "IList<T>", p: "int", r: "int"):
        if r - p > 1:
            pivot_index = self._partition(a, p, r)
            self._quicksort(a, p, pivot_index)
            self._quicksort(a, pivot_index+1, r)        

    def sort(self, a: "IList<T>"):
        self._quicksort(a, 0, len(a)) #]partition

class RandomizedInPlaceQuickSorter(BasicInPlaceQuickSorter): #[random
    def _partition(self, a: "IList<T>", p: "int", r: "int") -> "int": 
        q = randrange(p, r)
        a[r-1], a[q] = a[q], a[r-1]
        return BasicInPlaceQuickSorter._partition(self, a, p, r) #]random

class BasicSemiIterativeInPlaceQuickSorter(RandomizedInPlaceQuickSorter): #[qssemi
    def _quicksort(self, a: "IList<T> -> IList<T>", p: "int", r: "int"):
        while r - p > 1:
            pivot_index = self._partition(a, p, r)
            self._quicksort(a, p, pivot_index)
            p = pivot_index + 1 #]qssemi

class SemiIterativeInPlaceQuickSorter1(RandomizedInPlaceQuickSorter): #[qssemi2
    def _quicksort(self, a: "IList<T>", p: "int", r: "int"):
        while r - p > 1:
            pivot_index = self._partition(a, p, r)
            if r - pivot_index < pivot_index - p:
                self._quicksort(a, pivot_index+1, r)
                r = pivot_index
            else:
                self._quicksort(a, p, pivot_index)
                p = pivot_index + 1 #]qssemi2

class RandomizedSemiIterativeInPlaceQuickSorter(IInPlaceSorter): #[randqssemi3
    def sort(self, a: "IList<T>"):
        def _quicksort(p: "int", r: "int"):
            while r - p > 1:
                q = randrange(p, r)
                a[r-1], a[q] = a[q], a[r-1]
                pivot = a[r-1]
                i = p - 1
                for j in range(p, r-1):
                    if a[j] <= pivot:
                        i += 1
                        a[i], a[j] = a[j], a[i]
                a[i+1], a[r-1] = a[r-1], a[i+1]
                pivot_index = i + 1 
                if r - pivot_index < pivot_index - p:
                    _quicksort(pivot_index+1, r)
                    r = pivot_index
                else:
                    _quicksort(p, pivot_index)
                    p = pivot_index + 1 
        _quicksort(0, len(a)) #]randqssemi3

                
class SemiIterativeInPlaceQuickSorter(IInPlaceSorter): #[qssemi3
    def sort(self, a: "IList<T>"):
        def _quicksort(p: "int", r: "int"):
            while r - p > 1:
                pivot = a[r-1]
                i = p - 1
                for j in range(p, r-1):
                    if a[j] <= pivot:
                        i += 1
                        a[i], a[j] = a[j], a[i]
                a[i+1], a[r-1] = a[r-1], a[i+1]
                pivot_index = i + 1 
                if r - pivot_index < pivot_index - p:
                    _quicksort(pivot_index+1, r)
                    r = pivot_index
                else:
                    _quicksort(p, pivot_index)
                    p = pivot_index + 1 
        _quicksort(0, len(a)) #]qssemi3

