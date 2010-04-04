#coding: latin1
from algoritmia.problems.spanningtrees.baruvka import BaruvkasMinimumSpanningForestFinder
from algoritmia.problems.spanningtrees.kruskal import KruskalsMinimumSpanningForestFinder
from algoritmia.problems.spanningtrees.prim import PrimsMinimumSpanningFinder,\
    PrimsWithPriorityQueueMinimumSpanningTreeFinder
import unittest
from algoritmia.data.iberia import cities, roads, km, coords

from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph, WeightingFunction
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

    def test_baruvka(self):
        sff = BaruvkasMinimumSpanningForestFinder()
        self.assertEqual(count(sff.minimum_spanning_forest(self.iberia, km)), len(cities)-1)
        self.assertEqual(count(sff.minimum_spanning_forest(self.unconnected, self.unconnected_weight)), 7)
        w = sum(self.d(u,v) for (u, v) in sff.minimum_spanning_forest(self.g, self.d))
        self.assertEqual(w, 45)

    def test_Kruskal(self):
        sff = KruskalsMinimumSpanningForestFinder()
        self.assertEqual(count(sff.minimum_spanning_forest(self.iberia, km)), len(cities)-1)
        self.assertEqual(count(sff.minimum_spanning_forest(self.unconnected, self.unconnected_weight)), 7)
        w = sum(self.d(u,v) for (u, v) in sff.minimum_spanning_forest(self.g, self.d))
        self.assertEqual(w, 45)

    def test_Prim(self):
        stf = PrimsMinimumSpanningFinder()
        self.assertEqual(count(stf.minimum_spanning_tree(self.iberia, km, "Gandia")), len(cities)-1)
        self.assertEqual(count(stf.minimum_spanning_tree(self.unconnected, self.unconnected_weight, 0)), 5)
        w = sum(self.d(u,v) for (u, v) in stf.minimum_spanning_tree(self.g, self.d, 0))
        self.assertEqual(w, 45)

    def test_Prim_with_priority_dict(self):
        stf = PrimsMinimumSpanningFinder()
        self.assertEqual(count(stf.minimum_spanning_tree(self.iberia, km, "Gandia")), len(cities)-1)
        self.assertEqual(count(stf.minimum_spanning_tree(self.unconnected, self.unconnected_weight, 0)), 5)
        pstf = PrimsWithPriorityQueueMinimumSpanningTreeFinder()
        w = sum(self.d(u,v) for (u, v) in pstf.minimum_spanning_tree(self.g, self.d, 0))
        self.assertEqual(w, 45)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()