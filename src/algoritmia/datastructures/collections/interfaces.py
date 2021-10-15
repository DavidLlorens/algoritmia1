from collections.abc import Container
from collections import Iterable, Sized
from abc import abstractmethod

class ICollection(Container, Iterable, Sized): #[collection
    @abstractmethod
    def add(self, item: "T"):  pass
    
    @abstractmethod
    def remove(self, item: "T"): pass
    
    @abstractmethod
    def clear(self): pass #]collection