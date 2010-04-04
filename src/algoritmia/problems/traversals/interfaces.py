from abc import abstractmethod, ABCMeta

class IDigraphBreadthFirstTraverser(metaclass=ABCMeta): #[interface
    @abstractmethod
    def traverse(self, G: "IDigraph<T>", s: "T", visitor: "T, T -> S") -> "Iterable<S>":
        pass

    @abstractmethod
    def full_traverse(self, G: "IDigraph<T>", visitor: "T, T -> S") -> "Iterable<S>":  
        pass #]interface


class IDigraphDepthFirstTraverser(metaclass=ABCMeta):#[interface2
    @abstractmethod
    def traverse(self, G: "IDigraph<T>", s: "T", preorder_visitor: "T, T -> S",
                 postorder_visitor: "T, T -> S") -> "Iterable<S>":
        pass

    @abstractmethod
    def full_traverse(self, G: "IDigraph<T>", preorder_visitor: "T, T -> S",
                      postorder_visitor: "T, T -> S") -> "Iterable<S>":  
        pass #]interface2
    
