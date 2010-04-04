from algoritmia.datastructures.sets import ISet
from algoritmia.datastructures.lists import IList

class IntSet(ISet): #[intset
    def __init__(self, it: "Iterable<int>"=[], capacity: "int"=0):
        if not isinstance(it, IList): it = tuple(it)
        if it: capacity = max(capacity, max(it)+1)
        self._contains = [False] * capacity
        for item in it: self._contains[item] = True

    def get_capacity(self) -> "int":
        return len(self._contains)

    def set_capacity(self, capacity: "int"):
        if capacity < len(self._contains): 
            self._contains = self._contains[:capacity]
        elif capacity > len(self._contains): 
            self._contains.extend([False] * (capacity - len(self._contains)))

    capacity = property(get_capacity, set_capacity)

    def add(self, item: "int"):
        self._contains[item] = True

    add_unchecked = add

    def remove(self, item: "int"):
        if not item in self: raise KeyError(item)
        self._contains[item] = False

    def discard(self, item: "int"):
        if item in self: self._contains[item] = False

    def clear(self):
        for i in range(len(self._contains)): self._contains[i] = False

    def __contains__(self, item: "int") -> bool:
        return (0 <= item < len(self._contains)) and self._contains[item]

    def __len__(self) -> "int":
        return sum(1 for item in self._contains if item)

    def __iter__(self) -> "Iterable<int>":
        for item in range(len(self._contains)):
            if self._contains[item]: yield item

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self)) #]intset