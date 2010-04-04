#coding: latin1

#< full
from algoritmia.problems.compression.huffman2 import HuffmanCodeBuilder

print(HuffmanCodeBuilder().build_code({'a':30, 'b':25, 'c':15, 'd':20, 'e':10}))
#> full