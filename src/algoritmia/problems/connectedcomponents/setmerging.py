from algoritmia.problems.connectedcomponents.interfaces import IConnectedComponentsFinder
from algoritmia.datastructures.mergefindsets.mergefindset import MergeFindSet

class SetMergingConnectedComponentsFinder(IConnectedComponentsFinder): #[ccmf
    def __init__(self, createMergeFindSet: "Iterable<T> -> IMergeFindSet<T>"
                 =lambda V: MergeFindSet((v,) for v in V)):
        self.createMergeFindSet = createMergeFindSet
        
    def connected_components(self, 
                             G: "undirected IDigraph<T>") -> "Iterable<Iterable<T>>":
        mfset = self.createMergeFindSet(G.V)
        for (u, v) in G.E: mfset.merge(u, v)
        for set in mfset: yield set #]ccmf