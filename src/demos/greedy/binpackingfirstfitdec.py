    #coding: latin1

#< full
from algoritmia.problems.binpacking.firstfitdecreasingbinpacker import FirstFitDecreasingBinPacker

w = [1, 2, 8, 7, 8, 3]
packer = FirstFitDecreasingBinPacker()
x = packer.pack(w, 10)
packer.show_solution(x, w)
#> full