from abc import ABCMeta, abstractproperty, abstractmethod #[rooted

class IRootedTree(metaclass=ABCMeta):
    @abstractproperty
    def root(self) -> "T": pass

    @abstractmethod
    def succs(self, v: "T") -> "Iterable<T>": pass
    
    @abstractmethod
    def preds(self, v: "T") -> "empty Iterable<T> or Iterable<T> with a single item": 
        pass

    @abstractmethod
    def in_degree(self, v: "T") -> "0 or 1": pass

    @abstractmethod
    def out_degree(self, v: "T") -> "int": pass

    @abstractmethod
    def subtrees(self) -> "Iterable<IRootedTree<T>>": pass
    
    @abstractmethod
    def tree(self, v: "T") -> "IRootedTree<T>": pass  #]rooted
        