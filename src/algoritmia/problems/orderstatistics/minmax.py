#coding: latin1

#< minmax1
class DirectMinMaxFinder:
    def min_max(self, a):
        minimum = maximum = a[0]
        for i in range(1,len(a)):
            if a[i] < minimum: minimum = a[i]
            elif a[i] > maximum: maximum = a[i]
        return (minimum, maximum)
#> minmax1

#< minmax2
class MinMaxFinder:
    def min_max(self, a):
        def _min_max(i, k):
            if k - i == 1:
                return (a[i], a[i])
            elif k - i == 2:
                return (a[i], a[i+1]) if a[i+1] > a[i] else (a[i+1], a[i])
            else:
                j = (i + k) // 2
                (min1, max1) = _min_max(i, j)
                (min2, max2) = _min_max(j, k)
                return (min1 if min1 < min2 else min2, max1 if max1 > max2 else max2)
        return _min_max(0, len(a))

#> minmax2