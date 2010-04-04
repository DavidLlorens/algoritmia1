#coding: latin1
from collections import Container, Iterable, Sized #[full 

class RangeSet(Container, Iterable, Sized):
    def __init__(self, min: "int", max: "int"):
        self._min, self._max = min, max
    
    def __contains__(self, v: "int") -> "bool":
        return self._min <= v <= self._max
        
    def __iter__(self) -> "Iterable<int>":
        for i in range(self._min, self._max+1): yield i
    
    def __len__(self) -> "int":
        return self._max - self._min + 1
    
    def __repr__(self) -> "str":
        return '{}({!r}, {!r})'.format(self.__class__.__name__, self._min, self._max) #]full
