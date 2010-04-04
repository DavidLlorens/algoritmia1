#coding: latin1
#< full
from algoritmia.datastructures.digraphs import Digraph

def squared_graph(G):
    Gsquared = Digraph(V=G.V)
    for u in G.V:
        for v in G.succs(u):
            for w in G.succs(v):
                Gsquared.E.add( (u,w) )
    return Gsquared
if __name__ == "__main__":
    G = Digraph(E=[(0,1), (0,3), (1,4), (2,4), (2,5), (3,0), (3,1), (4,3), (5,5)])
    print('G:', G)
    print('G al cuadrado:', squared_graph(G))
#> full