from abc import abstractmethod
from collections.abc import Sized

class IPriorityQueue(Sized): #[abstract
    @abstractmethod
    def add(self, item: "T"): pass

    @abstractmethod
    def opt(self) -> "T": pass

    @abstractmethod
    def extract_opt(self) -> "T": pass #]abstract
    