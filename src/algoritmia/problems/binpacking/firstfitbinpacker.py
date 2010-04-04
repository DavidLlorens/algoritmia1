from algoritmia.problems.binpacking.nextfitbinpacker import NextFitBinPacker

class FirstFitBinPacker(NextFitBinPacker):#[full
    def pack(self, w: "IList<Real>", C: "Real") -> "IList<int>":
        x = [None] * len(w)
        free = []
        for i in range(len(w)):
            for j in range(len(free)):
                if free[j] >= w[i]:
                    x[i] = j
                    free[j] -= w[i]
                    break
            if x[i] == None:
                x[i] = len(free)
                free.append(C-w[i])
        return x#]full