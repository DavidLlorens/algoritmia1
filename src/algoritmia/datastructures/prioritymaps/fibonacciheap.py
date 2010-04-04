from algoritmia.datastructures.prioritymaps.interfaces import IPriorityMap
from math import log, sqrt #[]fibonacci

class FibonacciHeap(IPriorityMap): #[fibonacci1 #[]fibonacci2 #[]fibonacci3 #[]fibonacci4 #[]fibonacci5 #[]fibonacci6 #[]fibonacci
    class Node:
        def __init__(self, key: "K", value: "T"):
            self.parent = self.child = None
            self.left = self.right = self
            self.key = key
            self.value = value
            self.degree = 0
            self.mark = False

    def __init__(self, opt: "min or max"=min, data: "Iterable<(K, T)>"=[], 
                 createMap: "-> IMap<K, T>"=lambda: dict()):
        self._size = 0
        self._minroot = None
        self._map = createMap()
        self._opt = lambda a, b: None if a == None or b == None else opt(a, b)
        for key, value in data:
            self.add(key, value) 
            
    def __getitem__(self, key: "K") -> "T":
        return self._map[key].value #]fibonacci1

    def opt_item(self) -> "(K, T)": #[fibonacci2
        return self._minroot.key, self._minroot.value

    def opt(self) -> "K":
        return self._minroot.key

    def opt_value(self) -> "T":
        return self._minroot.value #]fibonacci2
    
    def add(self, key: "K", value: "T"): #[fibonacci3
        node = self._map[key] = FibonacciHeap.Node(key, value)
        if self._minroot == None:
            self._minroot = node
        else:
            node.left, node.right = self._minroot, self._minroot.right
            self._minroot.right = node.right.left = node
            if self._opt(node.value, self._minroot.value) != self._minroot.value: 
                self._minroot = node
        self._size += 1 #]fibonacci3

    def extract_opt(self) -> "K": #[fibonacci4
        opt = self.opt()
        self._remove_opt()
        return opt
    
    def extract_opt_item(self) -> "(K, T)":
        item = (self._minroot.key, self._minroot.value)
        self._remove_opt()
        return item

    def _remove_opt(self):
        z = self._minroot
        del self._map[z.key]
        if z != None:
            nchildren = z.degree
            x= z.child
            while nchildren > 0:
                t = x.right
                x.left.right, x.right.left = x.right, x.left
                x.left, x.right = self._minroot, self._minroot.right
                self._minroot.right = x.right.left = x
                x.parent = None
                x = t
                nchildren -= 1
            z.left.right, z.right.left = z.right, z.left
            if z == z.right:
                self._minroot = None
            else:
                self._minroot = z.right
                self._consolidate()
            self._size -= 1
            
    _philog = log((1 + sqrt(5)) / 2) 

    def _consolidate(self):
        a = [None] * int(log(self._size)/FibonacciHeap._philog)
        n_roots = self._count_roots()
        x = self._minroot
        while n_roots > 0:
            d = x.degree
            next = x.right
            while a[d] != None:
                y = a[d]
                if self._opt(x.value, y.value) != x.value: x, y = y, x
                self._link(y, x)
                a[d] = None
                d += 1
            a[d] = x
            x = next
            n_roots -= 1

        self._minroot = None
        for x in a:
            if x != None:
                if self._minroot != None:
                    x.left.right, x.right.left = x.right, x.left
                    x.left, x.right = self._minroot, self._minroot.right
                    self._minroot.right = x
                    x.right.left = x
                    if self._opt(x.value, self._minroot.value) != self._minroot.value:
                        self._minroot = x
                else:
                    self._minroot = x
    
    def _count_roots(self) -> "int":
        n_roots = 0
        x = self._minroot
        if x != None:
            n_roots += 1
            x = x.right
            while x != self._minroot:
                n_roots += 1
                x = x.right
        return n_roots

    def _link(self, y: "Node<K, T>", x: "Node<K, T>"):
        y.left.right, y.right.left = y.right, y.left
        y.parent = x
        if x.child == None:
            x.child = y.right = y.left = y
        else:
            y.left, y.right = x.child, x.child.right
            x.child.right = y.right.left = y
        x.degree += 1
        y.mark = False #]fibonacci4

    def __setitem__(self, key: "K", value: "T") -> "T":  #[fibonacci5
        if key not in self._map:
            self.add(key, value)
        else:
            self._improve_value(key, value)

    def _improve_value(self, key: "K", value: "T"):
        node = self._map[key]
        if self._opt(value, node.value) != value:
            raise ValueError(("{} at {} does not improve {}").format(value, key, node.value))
        node.value = value
        parent = node.parent
        if parent != None and self._opt(node.value, parent.value) != parent.value:
            self._cut(node, parent)
            self._cascading_cut(parent)
        if self._opt(node.value, self._minroot.value) != self._minroot.value: 
            self._minroot = node

    def _cut(self, x: "Node<K, T>", y: "Node<K, T>"):
        x.left.right, x.right.left = x.right, x.left
        y.degree -= 1
        if y.child == x: y.child = x.right
        if y.degree == 0: y.child = None
        x.left, x.right = self._minroot, self._minroot.right
        self._minroot.right = x
        x.right.left = x
        x.parent = None
        x.mark = False

    def _cascading_cut(self, node: "Node<K, T>"):
        parent = node.parent
        if parent != None:
            if not node.mark:
                node.mark = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent) #]fibonacci5

    def __delitem__(self, key: "K"): #[fibonacci6
        self._improve_value(key, None)
        self._remove_opt() #]fibonacci6

    def keys(self) -> "Iterable<K>": #[fibonacci
        return self._map.keys()

    def values(self) -> "Iterable<T>":
        for key in self._map: yield self._map[key].value 
        
    def items(self) -> "Iterable<(K, T)>":
        for key in self._map: 
            yield (key, self._map[key].value)

    def get(self, key: "K", default: "T"):
        if key in self._map: return self[key]
        return default

    def setdefault(self, key: "K", default: "T"):
        if key in self._map: return self[key]
        self[key] = default
        return default

    def __contains__(self, key: "K") -> "bool":
        return key in self._map

    def __len__(self) -> "int": 
        return self._size
    
    def __iter__(self) -> "Iterable<K>":
        for key in self._map: yield key
        
    def __repr__(self) -> "str":
        b = 'min' if self._opt == min else 'max'
        return '{}({}, {!r})'.format(self.__class__.__name__,b,[(k,self[k]) for k in list(self)])#]fibonacci