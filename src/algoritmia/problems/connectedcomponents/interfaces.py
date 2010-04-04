from abc import abstractmethod, ABCMeta
from algoritmia.utils import count

class IConnectedComponentsFinder(metaclass=ABCMeta): #[interface
    @abstractmethod
    def connected_components(self, 
        G: "undirected IDigraph<T>") -> "Iterable<Iterable<T>>": pass
    
    def is_connected(self, G: "undirected IDigraph<T>") -> "bool": 
        return count(self.connected_components(G)) == 1 #]interface
    
class IStrongConnectedComponentsFinder(metaclass=ABCMeta): #[interface2
    @abstractmethod
    def strong_connected_components(self, 
        G: "IDigraph<T>") -> "Iterable<Iterable<T>>": pass#]interface2
