from collections import Container, Iterable, Sized
from abc import abstractmethod, abstractproperty, ABCMeta 

class IDigraph(metaclass=ABCMeta): #[abstract1
    @abstractproperty
    def V(self) -> "IVertexSet<T>": pass
    
    @abstractproperty
    def E(self) -> "IEdgeSet<T>": pass
    
    @abstractproperty
    def is_directed(self) -> "bool": pass
    
    @abstractmethod
    def succs(self, u: "T") -> "Iterable<T>": pass
    
    @abstractmethod
    def preds(self, v: "T") -> "Iterable<T>": pass
    
    @abstractmethod
    def out_degree(self, u: "T") -> "int": pass
    
    @abstractmethod
    def in_degree(self, v: "T") -> "int": pass

    def degree(self, v: "T") -> "int": return self.out_degree(v) 

class IVertexSet(Container, Iterable, Sized): pass

class IEdgeSet(Container, Iterable, Sized): pass #]abstract1

class IEditableDigraph(IDigraph): #[abstract2
    @abstractproperty
    def V(self) -> "IEditableVertexSet<T>": pass
    
    @abstractproperty
    def E(self) -> "IEditableEdgeSet<T>": pass

class IEditableVertexSet(IVertexSet):
    @abstractmethod
    def add(self, v: "T"): pass

    @abstractmethod
    def remove(self, v: "T"): pass

class IEditableEdgeSet(IEdgeSet):
    @abstractmethod
    def add(self, u: "T or (T, T)", v: "T or None"): pass

    @abstractmethod
    def remove(self, u: "T or (T, T)", v: "T or None"): pass #]abstract2
