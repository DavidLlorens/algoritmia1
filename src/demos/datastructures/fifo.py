#coding: latin1

#< full
from algoritmia.datastructures.queues import Fifo

dfltFifo = Fifo([0, 1])
listBasedFifo = Fifo([0, 1], createList=lambda data: list(data))
for i in range(2, 6):
    listBasedFifo.push(i)
    dfltFifo.push(i)
while len(listBasedFifo) > 0:
    print(dfltFifo.pop(), listBasedFifo.pop(), end=" : ")
#> full