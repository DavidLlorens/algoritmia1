#coding: latin1

#< full
from algoritmia.sorting import SemiIterativeInPlaceQuickSorter, RandomizedSemiIterativeInPlaceQuickSorter
from random import sample, seed
from time import clock
instances = 10
tmin = 1

qs = SemiIterativeInPlaceQuickSorter()
rqs = RandomizedSemiIterativeInPlaceQuickSorter()

measure = {qs: {}, rqs: {}}

sizes = [1000, 2000, 3000, 4000, 5000, 10000]
for size in sizes:
    print("sz:", size)
    for m in measure: measure[m][size] = 0
    for instance in range(instances):
        for method in qs, rqs:
            t1 = t2 = clock()
            r = 0
            while t2 - t1 < tmin:
                seed(r)
                a = sample(range(5*size), size)
                a = list(reversed(sorted(a)))
                method.sort(a)
                t2 = clock()
                r += 1
            
            t3 = t4 = clock()
            aux = 0
            while aux < r:
                t4 - t3
                seed(r)
                a = sample(range(5*size), size)
                a = list(reversed(sorted(a)))
                t4 = clock()
                aux += 1
        
            t = ((t2 - t1) - (t4 - t3)) / r
                        
            measure[method][size] += t
            print("{:<35} {:.8f} {:.8f}".format(method.__class__.__name__, t, measure[method][size]))

label = {str(rqs): r'[#quicksort#] aleatorizado', str(qs): r'[#quicksort#] \phantom{aleatorizado}'}
print(r"\begin{tabular}[b]{lrrrrrr}\toprule")

print("$n$ ", end="")
for sz in sizes: print("& {}".format(sz), end=" ")
print(r"\\\midrule")

for m in rqs, qs:
    print(label[str(m)], end=" ")
    for size in sorted(measure[m]):
        print("& {:.2f}".format(measure[m][size] / instances * 1e3), end=" ")
    print(r"\\")
print(r'\bottomrule')

print(r"\end{tabular}")        
#> full