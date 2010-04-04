#coding: latin1

#< full
from algoritmia.problems.allshortestpaths import AllShortestPaths
from algoritmia.data.mallorca import Mallorca, km

back = dict(AllShortestPaths().backpointers(Mallorca, km))
for i, path in enumerate(sorted(AllShortestPaths().shortest_paths(Mallorca, back))):
    print(', '.join(path))
    if i == 20: break
print("...")
#> full