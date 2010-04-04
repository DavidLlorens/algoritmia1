#coding: latin1

#< full
from algoritmia.problems.binpacking.nextfitbinpacker import NextFitBinPacker

w = [1, 2, 8, 7, 8, 3]
packer = NextFitBinPacker()
x = packer.pack(w, 10)
packer.show_solution(x, w)
#> full