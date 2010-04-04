from algoritmia.datastructures.maps.interfaces import IMap
from abc import abstractmethod, ABCMeta
from algoritmia.utils import infinity

class IBacktracer(metaclass=ABCMeta):
    @abstractmethod
    def backtrace(self, t: "T") -> "IList<T>": pass

    @abstractmethod
    def distance(self, t: "T", d: "T, T -> R"=lambda u, v: 1) -> "R": pass
    
class Backtracer(IBacktracer):
    def __init__(self, backpointers: "Iterable<(T, T or None)>", 
                 createMap: "Iterable<T, T or None> -> IMap<T, T or None>"=lambda it: dict(it)):
        if not isinstance(backpointers, IMap): 
            backpointers = createMap(backpointers)
        self._backpointers = backpointers
    
    def backtrace(self, t: "T") -> "IList<T> or None": #[backtrace
        if t not in self._backpointers: return None
        path = [t]
        v = t
        while self._backpointers.get(v, None) != None and v != self._backpointers[v]:
            v = self._backpointers[v]
            path.append(v)
        if v not in self._backpointers or self._backpointers[v] == None: return None
        path.reverse()
        return path 
    
    def distance(self, t: "T", d: "T, T -> R"=lambda u, v: 1) -> "R":
        path = self.backtrace(t)
        if path == None: return infinity
        return sum(d(path[i], path[i+1]) for i in range(len(path)-1)) #]backtrace
