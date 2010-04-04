from algoritmia.problems.topsort.interfaces import ITopsorter
from algoritmia.problems.traversals import DepthFirstTraverser

class Topsorter(ITopsorter):#[topsort
    def __init__(self, createDepthFirstTraverser: "IDIgraph<T> -> IDepthFirstTraverser" 
                 =lambda G: DepthFirstTraverser()):
        self.createDepthFirstTraverser = createDepthFirstTraverser
        
    def topsorted(self, G):
        traverser = self.createDepthFirstTraverser(G)
        return reversed(list(traverser.full_traverse(G, postorder_visitor=lambda u, v: v))) #]topsort
    