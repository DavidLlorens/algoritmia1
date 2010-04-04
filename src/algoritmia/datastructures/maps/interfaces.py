from collections import Container, Iterable, Sized
from abc import abstractmethod

class IMap(Container, Iterable, Sized): #[imap
    @abstractmethod
    def __getitem__(self, key: "K") -> "T": pass

    @abstractmethod
    def __setitem__(self, key: "K", value: "T"): pass

    @abstractmethod
    def __delitem__(self, key: "K"): pass
    
    @abstractmethod
    def get(self, key: "K", default: "T"): pass    

    @abstractmethod
    def setdefault(self, key: "K", default: "T") -> "T": pass    
    
    @abstractmethod
    def keys(self) -> "Iterable<K> and Sized": pass

    @abstractmethod
    def values(self) -> "Iterable<T> and Sized": pass

    @abstractmethod
    def items(self) -> "Iterable<(K, T)> and Sized": pass #]imap
     
IMap.register(dict) #[]dict
