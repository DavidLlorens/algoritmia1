from abc import abstractmethod, ABCMeta

class ISorter(metaclass=ABCMeta):#[isorter
    @abstractmethod
    def sorted(self, a: "IList<T>") -> "sorted Iterable<T>": pass #]isorter

class IInPlaceSorter(metaclass=ABCMeta):#[inplace
    @abstractmethod
    def sort(self, a: "IList<T>"): pass #]inplace