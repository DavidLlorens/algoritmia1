#coding: latin1

#< gas
class GasStationRoutePlanner:
    def plan(self, d: "IList<Real>", n: "int") -> "IList<int>":
        stop = [0]
        km = n
        for (i, dist) in enumerate(d):
            if dist >= km:
                stop.append(i)
                km = n
            km -= dist
        if stop[-1] != len(d): stop.append(len(d))
        return stop 
#> gas