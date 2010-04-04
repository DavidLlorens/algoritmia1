#coding: latin1
from algoritmia.datastructures.collections import ICollection

class LinkedListCollection(ICollection): #[linkedlistcollection1 #[]linkedlistcollection2 #[]linkedlistcollection3 #[]linkedlistcollection4
    class Node:
        __slots__ = ("value", "prev", "next")
        
        def __init__(self, value, prev, next):
            self.value, self.prev, self.next = value, prev, next

    def __init__(self, seq: "Iterable<T>"=[]):
        self._head = self._last = None
        self._length = 0
        for item in seq: self.add(item) 

    def add(self, value: "T"): 
        node = LinkedListCollection.Node(value, self._last, None)
        if self._last == None:
            self._head = self._last = node
        else:
            self._last.next = node
            self._last = node
        self._length += 1 #]linkedlistcollection1

    def remove(self, value: "T"): #[linkedlistcollection2
        if self._head != None:
            node = self._head
            while node.value != value and node.next: node = node.next
            if node and node.value == value: 
                self._remove(node)
                self._length -= 1
                return
        raise ValueError("Cannot remove {!r}".format(value))

    def _remove(self, node: "Node<T>"): 
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        if self._head == node: self._head = node.next
        if self._last == node: self._last = node.prev #]linkedlistcollection2

    def clear(self): #[linkedlistcollection3
        self._head = self._last = None
        self._length = 0 #]linkedlistcollection3

    def __iter__(self) -> "Iterable<T>": #[linkedlistcollection4
        node = self._head
        while node != None: 
            yield node.value
            node = node.next

    def __contains__(self, value: "T") -> "bool":
        return any(value == v for v in self)
        
    def __len__(self) -> "int":
        return self._length

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self)) #]linkedlistcollection4
