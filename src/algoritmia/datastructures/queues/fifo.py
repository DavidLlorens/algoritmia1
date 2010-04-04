from algoritmia.datastructures.queues import IFifo
from algoritmia.datastructures.lists import LinkedList

class Fifo(IFifo):#[fifo
    def __init__(self, data: "Iterable<T>"=[], 
                 createList: "Iterable<T> -> IList<T>"=lambda data: LinkedList(data)):
        self._list = createList(data)

    def push(self, item: "T"):
        self._list.append(item)
        
    def pop(self) -> "T":
        v = self._list[0]
        del self._list[0]
        return v

    def top(self) -> "T":
        return self._list[0]
    
    def __len__(self) -> "int":
        return len(self._list)
    
    def __iter__(self) -> "Iterable<T>":
        for item in self._list: yield item

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self._list)) #]fifo
