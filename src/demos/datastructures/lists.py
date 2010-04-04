#coding: latin1

#< full
from algoritmia.datastructures.lists import LinkedList

a = LinkedList()
a.append(1)
a.insert(0, 2)
a.extend((5,15))
print(a)
print(a.pop())
print(a)
#> full