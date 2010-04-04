from algoritmia.problems.sorting.interfaces import ISorter
from algoritmia.datastructures.priorityqueues.heap import MinHeap

class HeapSorter(ISorter):
    def sorted(self, seq: "IList<T>") -> "sorted Iterable<T>": #[heapsort
        Q = MinHeap(seq)
        return (Q.extract_opt() for i in range(len(Q))) #]heapsort