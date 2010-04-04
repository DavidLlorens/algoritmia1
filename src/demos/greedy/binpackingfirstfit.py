#coding: latin1

#< full
from algoritmia.problems.binpacking.firstfitbinpacker import FirstFitBinPacker

w = [1, 2, 8, 7, 8, 3]
packer = FirstFitBinPacker()
x = packer.pack(w, 10)
packer.show_solution(x, w)
#> full