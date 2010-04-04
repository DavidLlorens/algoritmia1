from algoritmia.datastructures.mergefindsets import IMergeFindSet
from collections import Sequence

class NaiveMergeFindSet(IMergeFindSet): #[naif
    def __init__(self, sets: "Iterable<Iterable<T>>"=[], 
                 createMap: "Iterable<T> -> IMap<T, T>"=lambda nodes: dict()):
        self.createMap = createMap
        if not isinstance(sets, Sequence): sets = tuple(sets)
        all = []
        for s in sets: all.extend(s)
        self._parent = self.createMap(all)
        first = None
        self._length = 0
        for s in sets:
            if len(s) > 0:
                self._length += 1
                for item in s:
                    if first == None: first = item
                    self._parent[item] = first
                first = None

    def add(self, x: "T"):
        self._parent[x] = x
        self._length += 1

    def find(self, x: "T") -> "T":
        while x != self._parent[x]: x = self._parent[x]
        return x

    def merge(self, x: "T", y: "T"):
        u = self.find(x)
        v = self.find(y)
        if u != v:
            self._parent[u] = v
            self._length -= 1
            
    def __iter__(self) -> "Iterable<Iterable<T>>":
        aux = self.createMap(self._parent.keys())
        for key in self._parent:
            aux.setdefault(self.find(key), []).append(key)
        for set in aux.values(): yield set

    def __len__(self):
        return self._length

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, tuple(self)) #]naif