#coding: latin1

#< full
from algoritmia.problems.allshortestpaths import AllShortestPaths
from algoritmia.data.mallorca import Mallorca, km

mindist = AllShortestPaths().distances(Mallorca, km)
print('     ', end="")
for u in Mallorca.V: print('{:4}'.format(u[:3]), end="")
print()

for u in Mallorca.V:
    print('{:4}'.format(u[:3]), end="")
    for v in Mallorca.V: print('{:4}'.format(mindist[u,v]), end="")
    print()
#> full