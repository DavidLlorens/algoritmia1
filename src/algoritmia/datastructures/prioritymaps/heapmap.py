from algoritmia.datastructures.prioritymaps.interfaces import IPriorityMap
from algoritmia.datastructures.maps import IMap
from collections.abc import Sequence
from itertools import chain, repeat
 
class HeapMap(IPriorityMap): #[pdict
    def __init__(self, opt: "min or max", data: "Iterable<(K, T)>"=[], capacity: "int"=0,
            createMap: "-> IMap<K, T>"=dict,
            redimMap: "IMap<K, T>, K -> IMap<K, T>"=lambda map, maxkey: map):
        self.createMap = createMap
        self.redimMap = redimMap
        self._opt = opt
        self._index = self.createMap()
        if isinstance(data, IMap): data = data.items()
        elif not isinstance(data, Sequence): data = tuple(data)
        for (i, (key, _)) in enumerate(data): self._index[key] = i+1
        self._size = len(data)
        self._heap = list(chain((None,), ((v, k) for (k, v) in data), 
                                repeat(None, max(0, capacity-self._size))))
        for i in range(self._size//2, 0, -1): self._heapify(i)
        
    def _heapify(self, i: "int"):
        while True:
            l, r = 2*i, 2*i+1
            if l <= self._size and self._opt(self._heap[l], self._heap[i]) != self._heap[i]:
                best = l
            else:
                best = i
            if r <= self._size and self._opt(self._heap[r], self._heap[best]) != self._heap[best]: 
                best = r
            if best == i: break
            self._index[self._heap[i][1]], self._index[self._heap[best][1]] = best, i
            self._heap[i], self._heap[best] = self._heap[best], self._heap[i]
            i = best

    def _bubble_up(self, i: "int"):
        p = i // 2
        while i > 1 and self._opt(self._heap[i], self._heap[p]) != self._heap[p]:
            self._index[self._heap[i][1]], self._index[self._heap[p][1]] = p, i
            self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
            i, p = p, p // 2

    def opt(self) -> "K":
        if self._size == 0: raise IndexError('opt from an empty priority dict')
        return self._heap[1][1]

    def opt_item(self) -> "(K, T)":
        if self._size == 0: raise IndexError('opt from an empty priority dict')
        return (self._heap[1][1], self._heap[1][0])

    def opt_value(self) -> "T":
        if self._size == 0: raise IndexError('opt from an empty priority dict')
        return self._heap[1][0]

    def extract_opt(self) -> "K":
        return self.extract_opt_item()[0]

    def extract_opt_item(self) -> "(K, T)":
        m = self.opt_item()
        if self._size > 1:
            self._heap[1], self._index[self._heap[self._size][1]] = self._heap[self._size], 1
            self._heap[self._size] = None
        self._size -= 1
        if self._size > 1: self._heapify(1)
        del self._index[m[0]]
        return m

    def __contains__(self, key: "K") -> bool:
        return key in self._index

    def __getitem__(self, key: "K") -> "T":
        return self._heap[self._index[key]][0]

    def __setitem__(self, key: "K", score: "T") -> "T":
        if key in self._index:
            i = self._index[key]
            if score == self._heap[i][0]: return score
            if self._opt(score, self._heap[i][0]) != score:
                self._heap[i] = (score, key)
                self._heapify(i)
                return score
        else:
            self.redimMap(self._index, key)
            if self._size + 1 >= len(self._heap): self._heap.append(None)
            self._index[key] = i = self._size = self._size + 1
        self._heap[i] = (score, key)
        self._bubble_up(i)
        return score

    def __delitem__(self, key: "K"):
        if key not in self._index: raise KeyError(key)
        i = self._index[key]
        self._heap[i], self._index[self._heap[self._size][1]] = self._heap[self._size], i
        self._size -= 1
        self._heapify(i)
        if i > 1 and self._heap[i] < self._heap[i//2]:
            p = i // 2
            while i > 1 and self._heap[i] < self._heap[p]:
                self._index[self._heap[i][1]], self._index[self._heap[p][1]] = p, i
                self._heap[i], self._heap[p] = self._heap[p], self._heap[i]
                i, p = p, p//2
        else:
            self._heapify(i) 
        del self._index[key]

    def keys(self) -> "Iterable<K>":
        for key in self._index: yield key

    def values(self) -> "Iterable<T>":
        for key in self._index: yield self._heap[self._index[key]][0]
        
    def items(self) -> "Iterable<(K, T)>":
        for key in self._index: 
            yield (self._heap[self._index[key]][1], self._heap[self._index[key]][0])

    def get(self, key: "K", default: "T"):
        if key in self._index: return self[key]
        return default

    def setdefault(self, key: "K", default: "T"):
        if key in self._index: return self[key]
        self[key] = default
        return default

    def __iter__(self) -> "Iterable<K>":
        for key in self._index: yield key
        
    def __len__(self) -> "int":
        return self._size

    def __repr__(self) -> "str":
        b = 'min' if self._opt == min else 'max'
        return '{}({}, {!r})'.format(self.__class__.__name__, b, [(k, self[k]) for k in self])

class MinHeapMap(HeapMap):
    def __init__(self, data: "Iterable<(K, T)>"=[], capacity: "int"=0, **kw):
        super().__init__(min, data, capacity, **kw)

class MaxHeapMap(HeapMap):
    def __init__(self, data: "Iterable<(K, T)>"=[], capacity: "int"=0, **kw):
        super().__init__(max, data, capacity, **kw) #]pdict