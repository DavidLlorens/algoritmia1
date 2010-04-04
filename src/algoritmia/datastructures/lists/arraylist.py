from algoritmia.datastructures.lists.interfaces import IList
from array import array
from itertools import repeat

class ArrayList(IList): #[arraylist #[]arraylist2 #[]arraylist3 #[]arraylist4 #[]arraylist5
    _zeros = {'b': 0, 'B': 0, 'u': '\0', 'h': 0, 'H': 0, 'i': 0, 'I': 0, 'l': 0, 'L': 0, 
              'f': 0.0, 'd': 0.0}
    
    def __init__(self, T: "str", data:" Iterable<T>"=[]):
        data = tuple(data)
        self._type = T
        self._zero = ArrayList._zeros[T]
        self._array = array(self._type, data) 
        self._length = len(self._array)
        if self._length == 0: self._array = array(self._type, [self._zero])
        self._capacity = len(self._array) #]arraylist
    
    def append(self, value: "T"): #[arraylist2
        if self._length == self._capacity: self._double()
        if value == None: value = self._zero
        self._array[self._length] = value
        self._length += 1

    def _double(self):
        self._array = array(self._type, 
                            (e for s in (self._array, repeat(self._zero, self._capacity)) for e in s))
        self._capacity = 2 * self._capacity #]arraylist2
    
    def __getitem__(self, index: "int") -> "T": #[arraylist3
        if not (-self._length <= index < self._length): raise IndexError()
        if index < 0: index = self._length + index
        return self._array[index]
    
    def __setitem__(self, index: "int", value: "T") -> "T":
        if not (-self._length <= index < self._length): raise IndexError()
        if index < 0: index = self._length + index
        self._array[index]= value
        return value #]arraylist3
    
    def __delitem__(self, index: "int"):#[arraylist4
        if not (-self._length <= index < self._length): raise IndexError()
        if index < 0: index = self._length + index
        for i in range(index, self._length-1): self._array[i] = self._array[i+1]
        if self._length > 0: self._array[self._length-1] = self._zero
        self._length -= 1
        if self._length < self._capacity // 2: self._halve()

    def _halve(self):
        self._capacity = self._capacity // 2
        self._array = array(self._type, (self._array[i] for i in range(self._capacity))) #]arraylist4
            
    def __iter__(self) -> "Iterable<T>": #[arraylist5
        for i in range(self._length): yield self._array[i] 
    
    def __contains__(self, value: "T") -> "bool":
        return any(value == v for v in self)
        
    def __len__(self) -> "int":
        return self._length

    def __repr__(self) -> "str":
        return '{}({!r}, {!r})'.format(self.__class__.__name__, self._type, list(self)) #]arraylist5

