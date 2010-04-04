from algoritmia.datastructures.trees.interfaces import IRootedTree

class ListOfListsTree(IRootedTree): #[listoflists
    def __init__(self, list_of_lists: "list<list<T>>"):
        self._lol = list_of_lists

    root = property(lambda self: self._lol[0])

    def succs(self, v: "T") -> "Iterable<T>":
        lol = self._search(v, self._lol)
        if lol != None:
            for i in range(1, len(lol)):
                yield lol[i][0] 
    
    def preds(self, v: "T") -> "empty Iterable<T> or Iterable<T> with a single item": 
        if v != self._lol[0]:
            p = self._search_parent(v, self._lol)
            if p != None:
                yield p

    def in_degree(self, v: "T") -> "0 or 1":
        return 1 if v != self._lol[0] else 0

    def out_degree(self, v: "T") -> "int":
        lol = self._search(v, self._lol)
        return len(lol) - 1

    def subtrees(self) -> "Iterable<ListOfListsTree<T>>":
        for i in range(1, len(self._lol)):
            yield ListOfListsTree(self._lol[i])
            
    def tree(self, v: "T") -> "ListOfListsTree<T>":
        return ListOfListsTree(self._search(v, self._lol))
    
    def _search(self, v: "T", lol: "list<list<T>> or None"):
        if len(lol) > 0 and v == lol[0]:
            return lol
        for i in range(1, len(lol)):
            found = self._search(v, lol[i])
            if found != None:
                return found
        return None

    def _search_parent(self, v: "T", lol: "list<list<T>>") -> "T or None":
        for i in range(1, len(lol)):
            if lol[i][0] == v:  
                return lol[0]
        for i in range(1, len(lol)):
            found = self._search_parent(v, lol[i])
            if found != None:
                return found
        return None
        
    def __repr__(self) -> "str":
        return "{}({!r})".format(self.__class__.__name__, self._lol) #]listoflists
