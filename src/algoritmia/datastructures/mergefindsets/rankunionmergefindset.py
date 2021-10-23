from algoritmia.datastructures.mergefindsets.naivemergefindset import NaiveMergeFindSet
from collections.abc import Sequence

class RankUnionMFset(NaiveMergeFindSet): #[rankunion
    def __init__(self, sets: "Iterable<Iterable<T>>"=[],  
        createMap: "Iterable<T> -> IMap<T, S>"=lambda nodes: dict()):

        self.createMap = createMap
        if not isinstance(sets, Sequence): sets = tuple(sets)
        all = []
        for s in sets: all.extend(s)
        self._parent = self.createMap(all)
        self._rank = self.createMap(all)
        self._length = 0
        first = None
        for s in sets:
            if len(s) > 0:
                self._length += 1
                for item in s:
                    if first == None: first = item
                    self._parent[item] = first
                    self._rank[item] = self._rank.get(item, 0) + 1
                first = None

    def add(self, x: "T"):
        self._parent[x] = x
        self._rank[x] = 1
        self._length += 1

    def merge(self, x: "T", y: "T"):
        u = self.find(x)
        v = self.find(y)
        if u != v:
            self._length -= 1
            if self._rank[u] < self._rank[v]:
                self._parent[u] = v
            elif self._rank[u] > self._rank[v]:      
                self._parent[v] = u
            else:
                self._parent[v] = u
                self._rank[u] += 1 #]rankunion