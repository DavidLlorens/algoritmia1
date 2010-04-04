from abc import abstractmethod, ABCMeta
from algoritmia.problems.shortestpaths.backtracer import Backtracer

class IShortestPathsFinder(metaclass=ABCMeta): #[isp
    @abstractmethod
    def some_to_some_distance(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", F: "SizedIterableContainer<T>") -> "R": 
        pass

    @abstractmethod
    def some_to_some_backpointers(self, G: "acyclic IDigraph<T>", d: "T, T -> R", 
            I: "SizedIterableContainer<T>", 
            F: "SizedIterableContainer<T>") -> "Iterable<(T, T or None)>": 
        pass

    def distance(self, G: "IDigraph<T>", d: "T, T -> R", s: "T", t: "T") -> "R":
        return self.some_to_some_distance(G, d, [s], [t])

    def shortest_path(self, G: "IDigraph<T>", d: "E -> R", s: "T", t: "T", 
                      createBacktracer: 
                        "Iterable<T, T or None> or IMap<T, T or None> -> IBacktracer<T>"
                        =lambda it: Backtracer(it)) -> "Iterable<T>":
        backtracer = createBacktracer(self.some_to_some_backpointers(G, d, [s], [t]))
        return backtracer.backtrace(t) #]isp
    
class IAllShortestPathsFinder(metaclass=ABCMeta):
    @abstractmethod
    def distances(self, G: "IDigraph<T>", d: "T, T -> R") -> "IMap<(T, T), R>": 
        pass
    
    @abstractmethod
    def backpointers(self, G: "IDigraph<T>", d: "T, T -> R") -> "IMap<T, (T or None)>": 
        pass

