from algoritmia.datastructures.trees.interfaces import IRootedTree

class ParentReferenceTree(IRootedTree): #[parentref
    def __init__(self, parent_references: "IMap<T, T>", root: "T"=None, 
                 createMap: "Iterable<T> -> IMap<T, T>"=lambda pr: dict(pr)):
        self._parent = createMap(parent_references)
        if root == None and len(self._parent) > 0:
            x = next(iter(self._parent.keys()))
            while x in self._parent and x != self._parent[x]: x = self._parent[x]
            self._root = x
        else:
            self._root = root

    root = property(lambda self: self._root)

    def succs(self, v: "T") -> "Iterable<T>":
        for w in self._parent:
            if self._parent[w] == v:
                yield w
        
    def preds(self, v: "T") -> "empty Iterable<T> or Iterable<T> with a single item": 
        if v != self._root:
            yield self._parent[v]

    def in_degree(self, v: "T") -> "0 or 1":
        return 1 if v != self._root else 0

    def out_degree(self, v: "T") -> "int":
        return sum(1 for _ in self.succs(v))
    
    def subtrees(self) -> "Iterable<ParentReferenceTree<T>>":
        for v in self.succs(self._root):
            yield ParentReferenceTree(None, v, createMap=lambda pr: self._parent)
            
    def tree(self, v: "T") -> "ParentReferenceTree<T>":
        return ParentReferenceTree(None, v, createMap=lambda pr: self._parent)

    def __repr__(self) -> "str":
        return "{}({!r}, {!r})".format(self.__class__.__name__, 
                                       list(self._parent.items()), self._root) #]parentref
