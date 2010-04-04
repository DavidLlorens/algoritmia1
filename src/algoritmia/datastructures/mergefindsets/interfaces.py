#coding: latin1
from collections import Iterable, Sized
from abc import abstractmethod 

class IMergeFindSet(Iterable, Sized): #[abstract
    @abstractmethod
    def add(self, x: "T"):  pass
    
    @abstractmethod
    def find(self, x: "T") -> "T": pass
    
    @abstractmethod
    def merge(self, x: "T", y: "T"): pass #]abstract
