from collections import Sized, Iterable, Container
from abc import abstractmethod

class IList(Sized, Iterable, Container): #[ilist
    @abstractmethod
    def __getitem__(self, index: "int") -> "T": pass

    @abstractmethod
    def __setitem__(self, index: "int") -> "T": pass

    @abstractmethod
    def __delitem__(self, index: "int"): pass
    
    @abstractmethod
    def append(self, item: "T"): pass

    def pop(self):
        if len(self) == 0: raise IndexError("Cannot pop from an empty IList")
        result = self[-1]
        del self[-1]
        return result

    def extend(self, items: "Iterable<T>"): 
        for item in items: self.append(item)

    def __iadd__(self, items: "Iterable<T>"):
        self.extend(items)

    def insert(self, index: "int", value: "T"):
        self.append(None)
        if index > -1: last, slot = len(self)-1, index
        else: last, slot = -1, index-1
        for i in range(last, slot, -1): self[i] = self[i-1]
        self[index] = value

    def remove(self, item: "T"):
        found = False
        i = 0
        for it in self:
            if it == item:
                found = True
                break
            i += 1
        if not found: raise ValueError()
        del self[i]

    def reverse(self):
        n = len(self)
        for i in range(n // 2):
            n -= 1
            self[i], self[n] = self[n], self[i] #]ilist
            
IList.register(list) #[]list