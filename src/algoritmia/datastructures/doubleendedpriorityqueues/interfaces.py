from algoritmia.datastructures.priorityqueues.interfaces import IPriorityQueue
from abc import abstractmethod

class IDoubleEndedPriorityQueue(IPriorityQueue): #[abstract
    @abstractmethod
    def worst(self): pass
    
    @abstractmethod
    def extract_worst(self): pass #]abstract 
