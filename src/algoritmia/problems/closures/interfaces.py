from abc import abstractmethod, ABCMeta

class IMatrixTransitiveClosureFinder(metaclass=ABCMeta): #[interface
    @abstractmethod
    def transitive_closure(self, M: "square matrix<booL>") -> "square matrix<bool>": 
        pass #]interface

class IDigraphTransitiveClosureFinder(metaclass=ABCMeta): #[interface2
    @abstractmethod
    def transitive_closure(self, G: "IDigraph<T>") -> "IDigraph<T>": pass #]interface2
