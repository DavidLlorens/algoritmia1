from algoritmia.datastructures.maps import IMap
from algoritmia.datastructures.queues import Lifo

class LeftLeaningRedBlackTreeMap(IMap): #[redblacktree
    class Node:
        __slots__ = ("red", "key", "value", "left", "right")
        
        def __init__(self, key, value, red: "bool", left: "Node"=None, right: "Node"=None):
            self.key, self.value = key, value
            self.left, self.right = left, right
            self.red = red
            
        def __repr__(self):
            l = repr(self.left) if self.left != None else "[L]" 
            r = repr(self.right) if self.right != None else "[R]" 
            red = "*" if self.red else "-"
            return '[({}{!r}, {!r}) {} {}]'.format(red, self.key, self.value, l, r) 
            
    def __init__(self, comparison: "T, T -> {-1, 0, 1}"=None, createLifo: "-> ILIFO<T>"=Lifo):
        self.createLifo = createLifo
        self._cmp = comparison or (lambda a, b: (a > b) - (a < b))
        self._size = 0
        self._root = None

    def __delitem__(self, key: "K"):
        self._root = self._delete(key, self._root)
        if self._root != None: self._root.red = False

    def __getitem__(self, key: "K"):
        return self._search(key, self._root).value

    def _search(self, key: "K", node: "Node<T>"):
        while node != None:
            cmp = self._cmp(key, node.key)
            if cmp == 0: return node
            elif cmp < 0: node = node .left
            else: node = node.right
        raise KeyError()

    def __setitem__(self, key: "K", value: "T"):
        self._root = self._add(self._root, key, value)
        self._root.red = False
        return value

    def _add(self, node, key: "K", value: "T"):
        if node == None:
            self._size += 1 
            return LeftLeaningRedBlackTreeMap.Node(key, value, True) 
        if self._is_red(node.left) and self._is_red(node.right): 
            self._flip_color(node)
            
        cmp = self._cmp(key, node.key)
        if cmp < 0: node.left = self._add(node.left, key, value)
        elif cmp > 0: node.right = self._add(node.right, key, value)
        else: node.value = value
        if self._is_red(node.right):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        return node

    def _is_red(self, node: "Node<T>"):
        return node != None and node.red
    
    def _flip_color(self, node: "Node<T>"):
        node.red = not node.red
        node.left.red = not node.left.red
        node.right.red = not node.right.red

    def _rotate_left(self, node: "Node<T>"):
        x = node.right
        node.right = x.left
        x.left = node
        x.red = node.red
        node.red = True
        return x
    
    def _rotate_right(self, node: "Node<T>"):
        x = node.left
        node.left = x.right
        x.right = node
        x.red = node.red
        node.red = True
        return x

    def _move_red_left(self, node: "Node<T>"):
        self._flip_color(node)
        if self._is_red(node.right.left):
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            self._flip_color(node)
            if self._is_red(node.right.right):
                node.right = self._rotate_left(node.right)
        return node
    
    def _move_red_right(self, node: "Node<T>"):
        self._flip_color(node)
        if self._is_red(node.left.left):
            node = self._rotate_right(node)
            self._flip_color(node)
        return node

    def _fix_up(self, node:"Node<T>"):
        if self._is_red(node.right):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_color(node)
        if node.left != None and self._is_red(node.left.right) and not self._is_red(node.left.left):
            node.left = self._rotate_left(node.left)
            if self._is_red(node.left):
                node = self._rotate_right(node)
        return node

    def _inorder_traversal(self, node: "Node<T>", visitor=lambda n: n):
        stack = self.createLifo()
        current = node
        while current != None:
            if current.left != None:
                stack.push(current)
                current = current.left
            else:
                while current != None:
                    yield current
                    current = current.right
                    if current != None: break
                    if len(stack) == 0: break
                    current = stack.pop()

    def __iter__(self):
        for node in self._inorder_traversal(self._root):
            yield node.key

    def _min(self, node: "Node<T>"):
        while node.left != None: node = node.left
        return node
        
    def _delete(self, key: "K", node: "Node<T>"):
        if self._cmp(key, node.key) < 0:
            if node.left != None:
                if not self._is_red(node.left) and not self._is_red(node.left.left):
                    node = self._move_red_left(node)
                node.left = self._delete(key, node.left)
        else:
            if self._is_red(node.left):
                node = self._rotate_right(node)
            if self._cmp(key, node.key) == 0 and node.right == None:
                self._size -= 1
                return None
            if node.right != None:
                if not self._is_red(node.right) and not self._is_red(node.right.left):
                    node = self._move_red_right(node)
                if self._cmp(key, node.key) == 0:
                    minimum = self._min(node.right)
                    node.key, node.value = minimum.key, minimum.value 
                    node.right = self._delete_min(node.right)
                else:
                    node.right = self._delete(key, node.right)
        return self._fix_up(node)

    def _delete_min(self, node: "Node<T>"):
        if node == None: return None
        if not self._is_red(node.left) and not self._is_red(node.left.left):
            node = self._move_red_left(node)
        node.left = self._delete_min(node.left)
        self._size += 1
        return self._fix_up(node)

    def setdefault(self, key: "K", default: "T") -> "T":
        if key in self: return self[key]
        self[key] = default
        return default

    def get(self, key: "K", default: "T") -> "T":
        if key in self: return self[key]
        return default

    def keys(self):
        for key in self: yield key

    def items(self) -> "Iterable<(K, T)>":
        for node in self._inorder_traversal(self._root):
            yield (node.key, node.value)

    def values(self) -> "Iterable<T>":
        for node in self._inorder_traversal(self._root):
            yield node.value
 
    def __contains__(self, key: "K"):
        try:
            self._search(key, self._root)
        except KeyError:
            return False
        return True
    
    def __len__(self) -> "int":
        return self._size
    
    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self.items())) #]redblacktree