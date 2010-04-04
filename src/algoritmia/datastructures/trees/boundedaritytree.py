from algoritmia.datastructures.trees.interfaces import IRootedTree

class BoundedArityTree(IRootedTree):  #[bounded
    def __init__(self, arity: "int"=0, seq: "Iterable<T>"=[], 
                 bounded_arity_tree: "BoundedArityTree<T>"=None, root_index: "int"=0):
        if bounded_arity_tree != None:
            self._arity = bounded_arity_tree._arity
            self._list = bounded_arity_tree._list
        else:
            self._arity = arity
            self._list = list(seq)
        self._root_index = root_index

    root = property(lambda self: self._list[self._root_index])
       
    def succs(self, v: "T") -> "Iterable<T>":
        for i in range(self._root_index, len(self._list)):
            if v == self._list[i]:
                first_child = self._arity * i + 1
                for i in range(first_child, min(len(self._list), first_child + self._arity)):
                    if self._list[i] != None:
                        yield self._list[i]
                break
        
    def preds(self, v: "T") -> "empty Iterable<T> or Iterable<T> with a single item": 
        if v != self._list[self._root_index]:
            for i in range(self._root_index, len(self._list)):
                if v == self._list[i]:
                    yield self._list[(i-1) // self._arity]

    def in_degree(self, v: "T") -> "0 or 1":
        return 1 if v != self._list[self._root_index] else 0

    def out_degree(self, v: "T") -> "int":
        return sum(1 for _ in self.succs(v))
    
    def subtrees(self) -> "Iterable<BoundedArityTree<T>>":
        first_child = self._arity * self._root_index + 1
        for i in range(first_child, min(len(self._list), first_child + self._arity)):
            if self._list[i] != None:
                yield BoundedArityTree(bounded_arity_tree=self, root_index=i)
                
    def tree(self, v: "T") -> "BoundedArityTree<T>":
        i = self._list.index(v)
        if i >= self._root_index:
            return BoundedArityTree(bounded_arity_tree=self, root_index=i)

    def __repr__(self) -> "str":
        return "{}({}, {!r}, root_index={!r})".format(
            self.__class__.__name__, self._arity, self._list, self._root_index) #]bounded