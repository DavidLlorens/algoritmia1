#coding: latin1
import unittest
from algoritmia.problems.shortestpaths.positive import DijkstraWithPriorityDictShortestPathsFinder
from algoritmia.data.iberia import cities, roads, km
from algoritmia.problems.shortestpaths.kedges import KEdgesDistance, SpaceReducedKEdgesDistance
from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph, WeightingFunction
from algoritmia.utils import infinity
from math import sqrt

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.iberia = UndirectedGraph(V=cities, E=roads)
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))
        
    def test_KEdgesDistance(self):
        kesp = KEdgesDistance()
        d = kesp.distance(self.unconnected, self.unconnected_weight, [0], [5], 2)
        self.assertEqual(d, 2)
        d = kesp.distance(self.unconnected, self.unconnected_weight, [0], [5], 3)
        self.assertEqual(d, 3)
        d = kesp.distance(self.unconnected, self.unconnected_weight, [0], [5], 4)
        self.assertEqual(d, infinity)
        
        dijkstra = DijkstraWithPriorityDictShortestPathsFinder()
        d0 = dijkstra.distance(self.iberia, km, 'Madrid', 'Gandia')
        d = tuple(kesp.distance(self.iberia, km, ['Madrid'], ['Gandia'], i) for i in range(10, 12))
        self.assertEqual(d0, min(d))

    def test_SpaceReducedKEdgesDistance(self):
        kesp = SpaceReducedKEdgesDistance()
        d = kesp.distance(self.unconnected, self.unconnected_weight, [0], [5], 2)
        self.assertEqual(d, 2)
        d = kesp.distance(self.unconnected, self.unconnected_weight, [0], [5], 3)
        self.assertEqual(d, 3)
        d = kesp.distance(self.unconnected, self.unconnected_weight, [0], [5], 4)
        self.assertEqual(d, infinity)

        dijkstra = DijkstraWithPriorityDictShortestPathsFinder()
        d0 = dijkstra.distance(self.iberia, km, 'Madrid', 'Gandia')
        d = tuple(kesp.distance(self.iberia, km, ['Madrid'], ['Gandia'], i) for i in range(10, 12))
        self.assertEqual(d0, min(d))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()