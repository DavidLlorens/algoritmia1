from algoritmia.datastructures.lists.interfaces import IList

class LinkedList(IList): #[linkedlist #[]linkedlist2 #[]linkedlist3 #[]linkedlist4 #[]linkedlist5 #[]linkedlist6  #[]linkedlist7  #[]linkedlist8
    class Node:
        __slots__ = ("value", "prev", "next")
        
        def __init__(self, value, prev, next):
            self.value, self.prev, self.next = value, prev, next #]linkedlist

    def __init__(self, seq: "Iterable<T>"=[]): #[linkedlist2
        self._head = self._last = None
        self._length = 0
        for item in seq: self.append(item) 

    def append(self, value: "T"): 
        node = LinkedList.Node(value, self._last, None)
        if self._last == None:
            self._head = self._last = node
        else:
            self._last.next = node
            self._last = node
        self._length += 1 #]linkedlist2

    def _get_node_at(self, i: "int") -> "Node<T>": #[linkedlist3 
        if not (-self._length <= i < self._length): raise IndexError("{}".format(i))
        if i > self._length // 2:
            i -= self._length
        elif i < -self._length // 2:
            i += self._length
        if i >= 0:
            node, j = self._head, 0
            while node and j < i: node, j = node.next, j + 1
        else:
            i, node, j = -i, self._last, 1
            while node and j < i: node, j = node.prev, j + 1
        return node #]linkedlist3
        
    def __getitem__(self, i: "int") -> "T": #[linkedlist4
        node = self._get_node_at(i)
        if node == None: raise IndexError('No item at position {!r}'.format(i))
        return node.value

    def __setitem__(self, i: "int", value: "T") -> "T":
        node = self._get_node_at(i)
        if node == None: raise IndexError('No item at position {!r}'.format(i))
        node.value = value
        return value #]linkedlist4
    
    def _remove(self, node: "Node<T>"): #[linkedlist5 
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        if self._head == node: self._head = node.next
        if self._last == node: self._last = node.prev 

    def __delitem__(self, i: "int"):
        node = self._get_node_at(i)
        if node == None: raise IndexError('No item at position {!r}'.format(i))
        self._remove(node)
        self._length -= 1

    def remove(self, value: "T"): 
        if self._head != None:
            node = self._head
            while node.value != value and node.next: node = node.next
            if node and node.value == value: 
                self._remove(node)
                self._length -= 1
                return
        raise ValueError("Cannot remove {!r}".format(value)) 

    def pop(self) -> "T":
        if self._last == None: raise IndexError('pop from an empty linked list')
        value = self._last.value
        self._remove(self._last)
        self._length -= 1
        return value #]linkedlist5
        
    def insert(self, i: "int", item: "T"): #[linkedlist6 
        if i == 0:
            newnode = LinkedList.Node(item, None, self._head)
            if self._head != None:
                self._head.prev = newnode
                self._head = newnode
            else:
                self._head = self._last = newnode
            self._length += 1
        elif i == self._length:
            self.append(item)
        else:
            node = self._get_node_at(i-1)
            if node == None: raise IndexError('Cannot insert at position {!r}'.format(i))
            newnode = LinkedList.Node(item, node, node.next)
            if node.next: node.next.prev = newnode
            node.next = newnode
            if node == self._last: self._last = newnode
            self._length += 1 #]linkedlist6

    def reverse(self): #[linkedlist7
        left, right = self._head, self._last
        for _ in range(len(self) // 2):
            left.value, right.value = right.value, left.value
            left = left._next
            right = right._prev #]linkedlist7

    def __iter__(self) -> "Iterable<T>": #[linkedlist8
        node = self._head
        while node != None: 
            yield node.value
            node = node.next

    def __contains__(self, value: "T") -> "bool":
        return any(value == v for v in self)
        
    def __len__(self) -> "int":
        return self._length

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self)) #]linkedlist8