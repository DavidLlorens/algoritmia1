from algoritmia.problems.spanningtrees.interfaces import ISpanningTreeFinder, ISpanningForestFinder
from algoritmia.problems.traversals import BreadthFirstTraverser

class GraphTraversalSpanningTreeFinder(ISpanningTreeFinder): #[bfspan
    def __init__(self, 
            createGraphTraverser: "undirected IDigraph<T> -> IBreadthFirstTraverser<T>"
                =lambda G: BreadthFirstTraverser()):
        self.createGraphTraverser = createGraphTraverser
        
    def spanning_tree(self, G: "undirected IDigraph<T>", s: "T"):
        traverser = self.createGraphTraverser(G)
        for (u, v) in traverser.traverse(G, s, visitor=lambda u, v: (u, v)):
            if u != v: yield (u, v) #]bfspan

class GraphTraversalSpanningForestFinder(ISpanningForestFinder):#[bfforest 
    def __init__(self, 
            createGraphTraverser: "undirected IDigraph<T> -> IBreadthFirstTraverser<T>"
                =lambda G: BreadthFirstTraverser()):
        self.createGraphTraverser = createGraphTraverser
        
    def spanning_forest(self, G: "undirected IDigraph<T>"):
        traverser = self.createGraphTraverser(G)
        tree = []
        for (u, v) in traverser.full_traverse(G, visitor=lambda u, v: (u,v)):
            if u == v:
                if len(tree) > 0: 
                    yield tree
                    tree = []
            else: 
                tree.append((u, v))
        if len(tree) > 0: 
            yield tree #]bfforest