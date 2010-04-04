#coding: latin1
#< full
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.problems.closures import DigraphTransitiveClosureFinder

G = Digraph(E=[(0,1), (0,3), (1,4), (2,4), (2,5), (3,0), (3,1), (4,3), (5,5)])
print(DigraphTransitiveClosureFinder().transitive_closure(G))
G2 = Digraph(E=[('C', 'C++'), ('C', 'Java'), ('C', 'C#'), ('C', 'ObjC'), #?[(?[¶(?
                ('C++', 'Java'), ('C++', 'C#'), ('Java', 'C#')]) #?('C++', 'J?»('C++', 'J?
print(DigraphTransitiveClosureFinder().transitive_closure(G2))
#> full