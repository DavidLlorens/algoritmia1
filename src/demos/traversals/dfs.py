#coding: latin1

#< full
from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.problems.traversals import DepthFirstTraverser

G = UndirectedGraph(E=[(0,1), (0,3), (1,4), (2,5), (3,1), (4,3)])
dfs = DepthFirstTraverser()
print('Pre      : %r' % (list(dfs.traverse(G, 0, preorder_visitor=lambda u, v: v))))
print('Post     : %r' % (list(dfs.traverse(G, 0, postorder_visitor=lambda u, v: v))))
print('Full pre : %r' % (list(dfs.full_traverse(G, preorder_visitor=lambda u, v: v))))
print('Full post: %r' % (list(dfs.full_traverse(G, postorder_visitor=lambda u, v: v))))
#> full