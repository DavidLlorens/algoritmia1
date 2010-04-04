#coding: latin1
#< full
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.problems.connectedcomponents import StrongConnectedComponentsFinder

G = Digraph(E=[(0,1),(1,2),(1,3),(2,0),(2,3),(3,4),(3,6),\
               (4,5),(4,6),(5,4),(5,8),(6,7),(7,6),(7,8)])
sccf = StrongConnectedComponentsFinder()
print([list(comp) for comp in sccf.strong_connected_components(G)])
#> full