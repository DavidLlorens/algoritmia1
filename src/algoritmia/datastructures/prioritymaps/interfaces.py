from algoritmia.datastructures.maps import IMap
from abc import abstractmethod

class IPriorityMap(IMap): #[abstract
    @abstractmethod
    def opt(self) -> "K": pass

    @abstractmethod
    def opt_item(self) -> "(K, T)": pass

    @abstractmethod
    def opt_value(self) -> "T": pass

    @abstractmethod
    def extract_opt(self) -> "K":  pass

    @abstractmethod
    def extract_opt_item(self) -> "(K, T)": pass #]abstract
    