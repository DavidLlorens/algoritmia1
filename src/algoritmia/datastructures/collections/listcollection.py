#coding: latin1
from algoritmia.datastructures.collections.interfaces import ICollection

class ListCollection(ICollection): #[linkedlistcollection
    def __init__(self, data: "Iterable<T>"=[],  #?data?¶data?
                 createList: "Iterable<T> -> IList<T>" #?seq?»seq? #?List?¶List? 
                    =lambda data: list(data)): #?=?»»=?
        self.createList = createList
        self._list = createList(data)
    
    def add(self, item: "T"):
        self._list.append(item)
 
    def remove(self, item: "T"):
        self._list.remove(item)

    def __contains__(self, item: "T") -> "bool":
        return item in self._list

    def __len__(self) -> "int":
        return len(self._list)

    def clear(self):
        try:
            self._list.clear()
        except AttributeError:
            self._list = self.createList(())

    def __iter__(self) -> "Iterable<T>":
        return self._list.__iter__()

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self)) 
