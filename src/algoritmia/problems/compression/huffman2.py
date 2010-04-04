from algoritmia.problems.compression.huffman1 import HuffmanCodeBuilder1
from algoritmia.datastructures.priorityqueues.heap import MinHeap

class HuffmanCodeBuilder(HuffmanCodeBuilder1): #[full
    def build_tree(self, freq: "IMap<Symbol, Real>") -> "Tree of symbol": 
        T = MinHeap([ [(freq[symbol], symbol)] for symbol in freq])
        while len(T) > 1:
            left_tree = T.extract_opt()
            right_tree = T.extract_opt()
            T.add( [ (left_tree[0][0]+right_tree[0][0], ), left_tree, right_tree ] )
        return T.opt()
