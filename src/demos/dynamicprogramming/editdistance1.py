#coding: latin1

#< full
from algoritmia.problems.sequencecomparison.editdistance import EditDistanceComputer

x, y = "ejemplo", "campos"
print("Distancia entre %s y %s: %d"%(x, y, EditDistanceComputer().distance(x, y)))
#> full