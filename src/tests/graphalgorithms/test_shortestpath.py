#coding: latin1
import unittest
from algoritmia.data.iberia import cities, roads, km, coords
from algoritmia.problems.shortestpaths.general import BellmanFordShortestPathsFinder
from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph, WeightingFunction
from algoritmia.utils import infinity
from math import sqrt

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.iberia = UndirectedGraph(V=cities, E=roads)
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))
        self.sp = BellmanFordShortestPathsFinder()
        
    def test_bellman_ford_distance(self):
        d = self.sp.distance(self.unconnected, self.unconnected_weight, 0, 5)
        self.assertEqual(d, 2)
        
    def test_bellman_ford_shortest_path(self):
        p = self.sp.shortest_path(self.unconnected, self.unconnected_weight, 0, 5)
        self.assertEqual(p, [0, 2, 5])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()