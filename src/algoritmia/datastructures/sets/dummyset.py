from algoritmia.datastructures.sets import ISet

class DummySet(ISet): #[dummy
    def __init__(self, seq=[]): pass
    def add(self, item: "T"): pass
    def discard(self, item: "T"): pass
    def __contains__(self, item: "T") -> "bool": return False
    def __len__(self) -> "int": return 0
    def __iter__(self) -> "Iterable<T>": return ()
    def __repr__(self) -> "str": return '{}()'.format(self.__class__.__name__) #]dummy