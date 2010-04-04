#coding: latin1

#< full
from algoritmia.problems.activityselection.greedy2 import ActivitiesSelector

x = ActivitiesSelector().select([(1,5), (1,2), (3,6), (4,7), (6,7)])
print('Actividades seleccionadas:', tuple(sorted(x)))
#> full