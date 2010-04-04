#coding: latin1

import unittest
from algoritmia.problems.traversals import DepthFirstTraverser, RecursiveDepthFirstTraverser, BreadthFirstTraverser
from algoritmia.datastructures.digraphs import Digraph, UndirectedGraph
from random import seed

class TestTraversers(unittest.TestCase):
    def setUp(self):
        self.G = Digraph(E={0:[1,2], 1:[3], 2:[3], 3: [4], 5:[6]})
        self.bft = BreadthFirstTraverser()
        self.rdft = RecursiveDepthFirstTraverser()
        self.dft = DepthFirstTraverser()
        seed(0)
        
    def test_breadth_first_traversal(self):
        self.assertTrue(tuple(self.bft.traverse(self.G, 0)) in ((0,1,2,3,4), (0,2,1,3,4)))

    def test_breadth_first_full_traversal(self):
        self.assertTrue(tuple(self.bft.full_traverse(self.G)) in \
                        ((0,1,2,3,4,5,6), 
                         (0,2,1,3,4,5,6),
                         (5,6,0,1,2,3,4),
                         (5,6,0,2,1,3,4),
                         ))
        
    def test_recursive_preorder_traversal(self):
        self.assertTrue(tuple(self.rdft.traverse(self.G, 0)) in ((0,1,3,4,2), (0,2,3,4,1)))

    def test_recursive_postorder_traversal(self):
        self.assertTrue(tuple(self.rdft.traverse(self.G, 0, postorder_visitor=lambda u, v: v)) in ((4,3,1,2,0), (4,3,2,1,0)))

    def test_preorder_traversal(self):
        self.assertTrue(tuple(self.dft.traverse(self.G, 0)) in ((0,1,3,4,2), (0,2,3,4,1)))

    def test_postorder_traversal(self):
        self.assertTrue(tuple(self.dft.traverse(self.G, 0, postorder_visitor=lambda u, v: v)) in ((4,3,1,2,0), (4,3,2,1,0)))

    def test_preorder_full_traversal(self):
        self.assertTrue(tuple(self.dft.full_traverse(self.G)) in ((0,1,3,4,2,5,6), (0,2,3,4,1,5,6)))

    def test_postorder_full_traversal(self):
        self.assertTrue(tuple(self.dft.full_traverse(self.G, postorder_visitor=lambda u, v: v)) in ((4,3,1,2,0,6,5), (4,3,2,1,0,6,5)))


    def test_breadth_first_traversal_from_some(self):
        self.assertTrue(tuple(self.bft.traverse_from_some(self.G, [0, 5])) in \
                        ((0,5,1,2,6,3,4), 
                         ))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()