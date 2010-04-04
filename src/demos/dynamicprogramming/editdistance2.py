#coding: latin1

#< full
from algoritmia.problems.sequencecomparison.editdistance import SpaceSavingEditDistanceComputer

x, y = "ejemplo", "campos"
print("Distancia entre %s y %s: %d" % (x, y, SpaceSavingEditDistanceComputer().distance(x, y)))
#> full