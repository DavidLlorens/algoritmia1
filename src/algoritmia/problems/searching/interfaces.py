from abc import abstractmethod, ABCMeta

class ISortedSearcher(metaclass=ABCMeta):#[isearcher
    @abstractmethod
    def index(self, a: "sorted IList<T>", x: "T") -> "int or None":  pass #]isearcher

