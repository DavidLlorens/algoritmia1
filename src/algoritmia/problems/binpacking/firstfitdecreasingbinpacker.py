from algoritmia.problems.binpacking.nextfitbinpacker import NextFitBinPacker
from algoritmia.problems.binpacking.firstfitbinpacker import FirstFitBinPacker

class FirstFitDecreasingBinPacker(NextFitBinPacker):#[full
    def pack(self, w: "IList<Real>", C: "Real") -> "IList<int>":
        W = list(sorted([(w[i], i) for i in range(len(w))], reverse=True))
        w_prime = [w[0] for w in W]
        x = FirstFitBinPacker().pack(w_prime, C)
        x_prime = [None] * len(x)
        for i in range(len(x)): x_prime[W[i][1]] = x[i]
        return x_prime#]full