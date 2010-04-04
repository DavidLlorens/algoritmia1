from algoritmia.datastructures.mergefindsets.rankunionmergefindset import RankUnionMFset
from algoritmia.datastructures.mergefindsets.pathcompressionmergefindset import PathCompressionMFset

class MergeFindSet(RankUnionMFset, PathCompressionMFset): #[mfset
    def __init__(self, sets: "Iterable<Iterable<T>>"=[], **kw): 
        super().__init__(sets, **kw)

    def find(self, x: "T") -> "T":
        return PathCompressionMFset.find(self, x) #]mfset