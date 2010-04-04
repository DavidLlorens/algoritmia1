#coding: latin1
from algoritmia.datastructures.digraphs import Digraph #[full
from algoritmia.problems.topsort import Topsorter

G = Digraph(E=[('C', 'C++'), ('C', 'Java'), ('C', 'C#'), ('C', 'ObjC'), #?[(?[¶(?
               ('C++', 'Java'), ('C++', 'C#'), ('Java', 'C#')]) #?('C++', 'J?»('C++', 'J?
print(list(Topsorter().topsorted(G))) #]full
