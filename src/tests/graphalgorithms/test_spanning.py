#coding: latin1
import unittest
from algoritmia.data.iberia import cities, roads
from algoritmia.problems.spanningtrees import GraphTraversalSpanningTreeFinder, GraphTraversalSpanningForestFinder
from algoritmia.datastructures.digraphs import UndirectedGraph, WeightingFunction
from algoritmia.utils import count
from random import seed

class TestSpanning(unittest.TestCase):
    def setUp(self):
        self.iberia = UndirectedGraph(V=cities, E=roads)
        self.unconnected = UndirectedGraph(E={0: [1,2], 1:[2,3], 2:[4, 5], 3: [4], 4: [5], 6: [7, 8], 7: [8]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E), symmetrical=True)
        self.d = WeightingFunction({(0,1): 0, (0,2): 15, (0,3): 2, 
                                    (1,3): 3, (1,4): 13, 
                                    (2,3): 11, (2,5): 4, 
                                    (3,4): 5, (3,5): 8,  (3,6): 12, 
                                    (4,7): 9, 
                                    (5,6): 16, (5,8):10, (6,7): 17, 
                                    (6,8): 1, (6,9): 6, 
                                    (7,9): 14, 
                                    (8,9): 7},
                                    symmetrical=True)
        self.g = UndirectedGraph(E=self.d.keys())
        seed(0)

    def test_breadth_first_spanning_tree(self):
        spf = GraphTraversalSpanningTreeFinder()
        self.assertEqual(count(spf.spanning_tree(self.iberia, 'Madrid')), len(cities)-1)
        self.assertEqual(count(spf.spanning_tree(self.unconnected, 0)), 5)
        self.assertEqual(count(spf.spanning_tree(self.g, 0)), 9)

    def test_breadth_first_spanning_forest(self):
        sff = GraphTraversalSpanningForestFinder()
        f = tuple(sff.spanning_forest(self.iberia))
        self.assertEqual(len(f), 1)
        self.assertEqual(count(f[0]), len(cities)-1)
        f = tuple(sff.spanning_forest(self.unconnected))
        self.assertEqual(len(f), 2)
        self.assertEqual(count(f[0])+count(f[1]), 7)
        forest = tuple(sff.spanning_forest(self.g))
        self.assertEqual(len(forest), 1)
        self.assertEqual(count(forest[0]), 9)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()