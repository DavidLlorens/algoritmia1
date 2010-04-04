from algoritmia.datastructures.trees.interfaces import IRootedTree

class DigraphTree(IRootedTree): #[graph
    def __init__(self, G: "IDigraph", root: "node"):
        self._G, self._root = G, root
    
    root = property(lambda self: self._root)

    def succs(self, v: "T") -> "Iterable<T>": 
        return self._G.succs(v)
    
    def preds(self, v: "T") -> "empty Iterable<T> or Iterable<T> with a single item": 
        if v != self._root:
            for u in self._G.preds(v):
                yield u

    def in_degree(self, v: "T") -> "0 or 1":
        return 1 if v != self._root else 0

    def out_degree(self, v: "T") -> "int":
        return self._G.out_degree(v)

    def subtrees(self) -> "Iterable<DigraphTree<T>>":
        for v in self._G.succs(self._root):
            yield DigraphTree(self._G, v)
    
    def tree(self, v: "int") -> "DigraphTree<T>":
        return DigraphTree(self._G, v)
    
    def __repr__(self) -> "str":
        return "{}({!r}, {!r})".format(self.__class__.__name__, 
                                       self._G, self._root) #]graph