from algoritmia.datastructures.priorityqueues.interfaces import IPriorityQueue
from collections import Iterable
from itertools import chain, repeat #[]init

class Heap(IPriorityQueue, Iterable): #[]opt #[]add #[]heapify #[init #[]utils 
    def __init__(self, opt: "min or max", data: "Iterable<T>"=[], capacity=0): 
        self._opt = opt
        self._size = len(data)
        self._heap = list(chain((None,), data, repeat(None, max(0, capacity-self._size))))
        for i in range(self._size//2, 0, -1): self._heapify(i) #]init

    def _heapify(self, i: "int"): #[heapify
        while True:
            l, r = 2*i, 2*i+1
            if l <= self._size and self._opt(self._heap[l], self._heap[i]) != self._heap[i]:
                best = l
            else:
                best = i
            if r <= self._size and self._opt(self._heap[r], self._heap[best]) != self._heap[best]: 
                best = r
            if best == i: break
            self._heap[i], self._heap[best] = self._heap[best], self._heap[i]
            i = best #]heapify

    def opt(self) -> "T": #[opt
        if self._size == 0: raise IndexError('opt from an empty heap')
        return self._heap[1]

    def extract_opt(self) -> "T":
        if self._size == 0: raise IndexError('extract opt from an empty heap')
        m = self._heap[1]
        if self._size > 1: self._heap[1], self._heap[self._size] = self._heap[self._size], None
        self._size -= 1
        if self._size > 1: self._heapify(1)
        return m #]opt

    def add(self, item: "T"): #[add
        if self._size + 1 == len(self._heap): self._heap.append(None)
        i = self._size = self._size + 1
        self._heap[i] = item
        self._bubble_up(i)

    def _bubble_up(self, i: "int"):
        parent = i // 2
        while i > 1 and self._opt(self._heap[i], self._heap[parent]) != self._heap[parent]:
            self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            i, parent = parent, parent // 2 #]add

    def __iter__(self) -> "Iterable<T>": #[utils
        for i in range(1, self._size+1): yield self._heap[i] 

    def __len__(self) -> "int":
        return self._size 

    def __repr__(self) -> "str":
        b = 'min' if self._opt == min else 'max'
        return '{}({}, {!r})'.format(self.__class__.__name__, b, self._heap[1:self._size+1])#]utils
    

class MinHeap(Heap): #[minmaxheap
    def __init__(self, data: "Iterable<T>"=[], capacity: "int"=0):
        super().__init__(min, data, capacity)

class MaxHeap(Heap):
    def __init__(self, data: "Iterable<T>"=[], capacity: "int"=0):
        super().__init__(max, data, capacity) #]minmaxheap