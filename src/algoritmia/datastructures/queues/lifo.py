from algoritmia.datastructures.queues import ILifo
from algoritmia.datastructures.lists import LinkedList

class Lifo(ILifo): #[lifo
    def __init__(self, data: "Iterable<T>"=[], 
                 createList: "Iterable<T> -> IList<T>"=lambda data: LinkedList(data)):
        self._list = createList(data)
    
    def push(self, item: "T"):
        self._list.append(item)

    def pop(self) -> "T":
        return self._list.pop()

    def top(self) -> "T":
        return self._list[-1]
    
    def __len__(self) -> "int":
        return len(self._list)
    
    def __iter__(self) -> "Iterable<T>":
        for item in reversed(self._list): yield item

    def __getitem__(self, i):
        return self._list[i]

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self._list)) #]lifo
