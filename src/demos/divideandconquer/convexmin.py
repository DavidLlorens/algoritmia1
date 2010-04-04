#coding: latin1

#< full
from algoritmia.problems.convexmin import ConvexMin1

for v in [9.5, 8, 6, 5, 4.5, 3.5, 3.25, 5.75, 6.5, 8.25], [10, 4, 3, 0], [0, 2, 10, 60]:
    print('Mínimo en {}: {}'.format(v, ConvexMin1().min(v)))
#> full