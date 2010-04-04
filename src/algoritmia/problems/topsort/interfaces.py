from abc import abstractmethod, ABCMeta

class ITopsorter(metaclass=ABCMeta):
    @abstractmethod
    def topsorted(self, G: "Digraph<T>") -> "Iterable<T>": pass #[]topsort
