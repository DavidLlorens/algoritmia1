from abc import abstractmethod, ABCMeta

class ISpanningTreeFinder(metaclass=ABCMeta): #[interface
    @abstractmethod
    def spanning_tree(self, G: "undirected IDigraph<T>", s: "T") -> "Iterable<(T, T)>":
        pass #]interface

class ISpanningForestFinder(metaclass=ABCMeta): #[interface2 
    @abstractmethod
    def spanning_forest(self, G: "undirected IDigraph<T>"\
            ) -> "Iterable<Iterable<(T, T)>>": pass #]interface2
            
class IMinimumSpanningTreeFinder(metaclass=ABCMeta): #[interface3
    @abstractmethod
    def minimum_spanning_tree(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R", u: "T") -> "Iterable<(T, T)>": pass 

class IMinimumSpanningForestFinder(metaclass=ABCMeta):
    @abstractmethod
    def minimum_spanning_forest(self, G: "undirected IDigraph<T>", 
            d: "T, T -> R") -> "Iterable<(T, T)>": pass #]interface3
