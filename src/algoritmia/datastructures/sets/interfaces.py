from collections import Sized, Iterable, Container
from abc import abstractmethod

class ISet(Sized, Iterable, Container): #[iset
    @abstractmethod
    def add(self, element: "T"): pass

    @abstractmethod
    def discard(self, element: "T"): pass

    def remove(self, element: "T"):
        if element not in self: raise KeyError(element)
        self.discard(element)
    
    def clear(self):
        for element in tuple(self):
            self.discard(element)

    def isdisjoint(self, other: "ISet<T>") -> "bool":
        for element in other:
            if element in self: return False
        return True
    
    def __and__(self, other: "Iterable<T>") -> "ISet<T>":
        return self.createSet(e for e in other if e in self)

    def __or__(self, other: "Iterable<T>") -> "ISet<T>":
        return self.createSet(e for s in (self, other) for e in s)

    def __sub__(self, other: "Iterable<T>") -> "ISet<T>":
        if not isinstance(other, ISet): other = self.createSet(other)
        return self.createSet(e for e in self if e not in other)
        
    def __xor__(self, other: "Iterable<T>") -> "ISet<T>":
        if not isinstance(other, ISet): other = self.createSet(other)
        return self.createSet((self - other) | (other - self))
    
    def __le__(self, other: "ISet<T>") -> "bool":
        if len(self) > len(other): return False
        return all(e in other for e in self)

    def __lt__(self, other: "ISet<T>") -> "bool":
        return len(self) < len(other) and self <= other

    def __ge__(self, other: "ISet<T>") -> "bool":
        return other <= self

    def __gt__(self, other: "ISet<T>") -> "bool":
        return other < self
    
    def __eq__(self, other: "ISet<T>") -> "bool":
        return len(self) == len(other) and self <= other
    
    def __ne__(self, other: "ISet<T>") -> "bool":
        return not (self == other)

    @classmethod
    def createSet(cls, it: "Iterable<T>") -> "ISet<T>":
        return cls(it)  #]iset


ISet.register(set) #[]set