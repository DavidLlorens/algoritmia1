class NextFitBinPacker:#[full
    def pack(self, w: "IList<Real>", C: "Real") -> "IList<int>":
        x = []
        cap_left = C
        bin = 0
        for i in range(len(w)):
            if cap_left < w[i]:
                cap_left = C
                bin += 1
            cap_left -= w[i]
            x.append(bin)
        return x

    def show_solution(self, x: "IList<int>", w: "IList<Real>"):
        for i in range(max(x)+1):
            print('{:2}:'.format(i+1), [w[j] for j in range(len(x)) if x[j] == i])#]full