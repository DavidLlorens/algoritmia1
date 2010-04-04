#coding: latin1

#< full
from algoritmia.problems.activityselection.greedy1 import ActivitiesSelector1

x = ActivitiesSelector1().select([(1,5), (1,2), (3,6), (4,7), (6,7)])
print('Actividades seleccionadas:', tuple(sorted(x)))
#> full