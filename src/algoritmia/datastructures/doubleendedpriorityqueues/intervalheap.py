from algoritmia.datastructures.doubleendedpriorityqueues.interfaces import IDoubleEndedPriorityQueue

class IntervalHeap(IDoubleEndedPriorityQueue): #[interval1
    def __init__(self, data: "Iterable<T>"=[], capacity: "int"=0):
        capacity = max(capacity, len(data))
        self._heap = data + [None] * (capacity-len(data))
        self._size = len(data)
        for v in range(0, self._size, 2): 
            if v+1 < self._size: self._swap(v)
        last_parent = self._parent(self._size-1)
        for v in range(last_parent, -1, -2):
            self._heapify_min(v)
            self._heapify_max(v)

    def _swap(self, i: "int") -> "bool":
        if self._heap[i] > self._heap[i+1]:
            self._heap[i], self._heap[i+1] = self._heap[i+1], self._heap[i]
            return True
        return False 
    
    def _parent(self, i: "int") -> "int":
        return ((i // 2 - 1) // 2) * 2 #]interval1
    
    def _heapify_min(self, i: "int"): #[interval2
        smallest = i
        while True:
            for j in self._children(i):
                if self._heap[j] < self._heap[smallest]: smallest = j
            if smallest == i: break
            self._heap[smallest], self._heap[i] = self._heap[i], self._heap[smallest]
            i = smallest
            if i+1 < self._size: 
                self._swap(i)

    def _heapify_max(self, i: "int"):
        largest = i+1
        while True:
            for j in self._children(i):
                if j + 1 < self._size:
                    if self._heap[j+1] > self._heap[largest]: largest = j+1
                else:
                    if self._heap[j] > self._heap[largest]: largest = j
            if largest == i+1: break
            self._heap[largest], self._heap[i+1] = self._heap[i+1], self._heap[largest]
            i = largest // 2 * 2
            if i+1 < self._size: 
                self._swap(i)
    
    def _children(self, i: "int") -> "Iterable<int>":
        j = 2*(i+1)
        if j < self._size: yield j
        j += 2
        if j < self._size: yield j #]interval2
        
    def add(self, v: "T"): #[interval3
        if self._size == len(self._heap): 
            self._heap.append(None)
        if self._size == 0:
            self._heap[0] = v
            self._size += 1
        else:
            self._heap[self._size] = v
            self._size += 1
            if self._size % 2 == 0:
                i = self._size - 2
                if self._swap(i):  
                    self._bubble_up_min(i)
                else:
                    self._bubble_up_max(i)
            else:
                i = self._size - 1
                parent = self._parent(i)
                if parent >= 0:
                    if self._heap[parent] <= v <= self._heap[parent+1]: return
                    if v > self._heap[parent+1]:
                        self._heap[parent+1], self._heap[i] = self._heap[i], self._heap[parent+1]
                        self._bubble_up_max(parent)
                    elif v < self._heap[parent]:
                        self._heap[parent], self._heap[i] = self._heap[i], self._heap[parent]
                        self._bubble_up_min(parent) 

    def _bubble_up_max(self, i: "int"):
        while True:
            parent = self._parent(i)
            if parent < 0: return
            if self._heap[parent+1] >= self._heap[i+1]: return
            self._heap[parent+1], self._heap[i+1] = self._heap[i+1], self._heap[parent+1]
            i = parent
            
    def _bubble_up_min(self, i: "int"):
        while True:
            parent = self._parent(i)
            if parent < 0: return
            if self._heap[parent] <= self._heap[i]: return
            self._heap[parent], self._heap[i] = self._heap[i], self._heap[parent]
            i = parent #]interval3

    def min(self) -> "T": #[interval4
        if self._size == 0: raise IndexError("Empty Interval Heap")
        return self._heap[0]

    def max(self) -> "T":
        if self._size == 0: raise IndexError("Empty Interval Heap")
        if self._size == 1: return self._heap[0]
        return self._heap[1] #]interval4

    def extract_min(self) -> "T": #[interval5
        if self._size == 0: raise IndexError("Empty Interval Heap")
        retval = self._heap[0]
        if self._size <= 2:
            if self._size == 1:
                self._heap[0] = None
            else:
                self._heap[0], self._heap[1] = self._heap[1], None
            self._size -= 1
            return retval
        self._heap[0], self._heap[self._size-1] = self._heap[self._size-1], None
        self._size -= 1
        self._heapify_min(0)
        return retval

    def extract_max(self) -> "T":
        if self._size == 0: raise IndexError("Empty Interval Heap")
        if self._size == 1:
            retval = self._heap[0]
            self._heap[0] = None
            self._size -= 1
            return retval        
        retval = self._heap[1]
        if self._size == 2:
            self._heap[1] = None
            self._size -= 1
            return retval
        self._heap[1], self._heap[self._size-1] = self._heap[self._size-1], None
        self._size -= 1
        self._heapify_max(0)
        return retval #]interval5

    def __len__(self) -> "int": #[interval6
        return self._size

    def __iter__(self) -> "Iterable<T>":
        for i in range(self._size):
            yield self._heap[i]

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, self._heap[:self._size]) #]interval6

    opt = min
    extract_opt = extract_min

    worst = max
    extract_worst = extract_max
    
class MinMaxIntervalHeap(IntervalHeap, IDoubleEndedPriorityQueue): #[minmax
    opt = IntervalHeap.min
    extract_opt = IntervalHeap.extract_min

    worst = IntervalHeap.max
    extract_worst = IntervalHeap.extract_max

class MaxMinIntervalHeap(IntervalHeap, IDoubleEndedPriorityQueue):
    opt = IntervalHeap.max
    extract_opt = IntervalHeap.extract_max

    worst = IntervalHeap.min
    extract_worst = IntervalHeap.extract_min #]minmax