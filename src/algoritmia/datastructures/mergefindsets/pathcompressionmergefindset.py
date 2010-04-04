from algoritmia.datastructures.mergefindsets.naivemergefindset import NaiveMergeFindSet

class PathCompressionMFset(NaiveMergeFindSet): #[path
    def __init__(self, sets: "Iterable<Iterable<T>>"=[], ** kw):
        super().__init__(sets, **kw)
        
    def find(self, x: "T"):
        r = x
        while r != self._parent[r]: r = self._parent[r]
        while x != self._parent[x]: self._parent[x], x = r, self._parent[x]
        return r #]path