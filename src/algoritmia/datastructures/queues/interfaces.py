#coding: latin1

from abc import abstractmethod 
from collections import Sized, Iterable

class IQueue(Sized, Iterable): #[iqueue
    @abstractmethod
    def push(self, item: "T"): pass
    
    @abstractmethod
    def pop(self) -> "T": pass
    
    @abstractmethod
    def top(self) -> "T": pass #]iqueue
    
class IFifo(IQueue): #[ififo
    def enqueue(self, item: "T"):
        self.push(item)
        
    def dequeue(self) -> "T":
        return self.pop() #]ififo
    
class ILifo(IQueue): pass #[]ilifo