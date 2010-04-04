from algoritmia.datastructures.prioritymaps.interfaces import IPriorityMap
from abc import abstractmethod

class IDoubleEndedPriorityDict(IPriorityMap): #[abstract
    @abstractmethod
    def worst(self) -> "K": pass

    @abstractmethod
    def worst_value(self) -> "T": pass

    @abstractmethod
    def worst_item(self) -> "(K, T)": pass

    @abstractmethod
    def extract_worst(self) -> "K": pass

    @abstractmethod
    def extract_worst_item(self) -> "(K, T)": pass #]abstract
    