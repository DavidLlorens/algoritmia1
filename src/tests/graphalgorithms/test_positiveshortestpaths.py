#coding: latin1
from algoritmia.problems.shortestpaths.backtracer import Backtracer
import unittest
from algoritmia.data.iberia import cities, roads, km, coords
from algoritmia.problems.shortestpaths.positive import DijkstraShortestPathsFinder, DijkstraWithPriorityDictShortestPathsFinder
from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph, WeightingFunction
from algoritmia.utils import infinity
from math import sqrt

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.iberia = UndirectedGraph(V=cities, E=roads)
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))
        
    def test_Dijkstra_shortest_path_backs_one_to_all_1(self):
        sp = DijkstraShortestPathsFinder()
        t = sp.some_to_some_backpointers(self.iberia, km, ['Gandia'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Cullera'), ["Gandia", "Cullera"])
        t = sp.some_to_some_backpointers(self.iberia, km, ['València'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Daroca'), 
                         ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        t = sp.some_to_some_backpointers(self.unconnected, self.unconnected_weight, [0], self.unconnected.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace(4), None)
        self.assertEqual(Backtracer(bp).backtrace(6), [0, 2, 6])
        
    def test_Dijkstra_shortest_path_backs_one_to_all(self):
        sp = DijkstraWithPriorityDictShortestPathsFinder()
        t = sp.some_to_some_backpointers(self.iberia, km, ['Gandia'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Cullera'), ["Gandia", "Cullera"])
        t = sp.some_to_some_backpointers(self.iberia, km, ['València'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Daroca'), 
                         ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        t = sp.some_to_some_backpointers(self.unconnected, self.unconnected_weight, [0], self.unconnected.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace(4), None)
        self.assertEqual(Backtracer(bp).backtrace(6), [0, 2, 6])

    def test_Dijkstra_shortest_path(self):
        sp = DijkstraShortestPathsFinder()
        p = sp.shortest_path(self.iberia, km, 'Gandia', 'Cullera')
        self.assertEqual(p, ["Gandia", "Cullera"])
        p = sp.shortest_path(self.iberia, km, 'València', 'Daroca')
        self.assertEqual(p, ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        p = sp.shortest_path(self.unconnected, self.unconnected_weight, 0, 4)
        self.assertEqual(p, None)
        p = sp.shortest_path(self.unconnected, self.unconnected_weight, 0, 6)
        self.assertEqual(p, [0, 2, 6])

    def test_Dijkstra_shortest_distances_one_to_all(self):
        sp = DijkstraWithPriorityDictShortestPathsFinder()
        d = sp.distance(self.iberia, km, 'Gandia', 'Cullera')
        self.assertAlmostEqual(d, 20.904)
        d = sp.distance(self.iberia, km, 'Gandia', 'Gandia')
        self.assertAlmostEqual(d, 0.0)
        d = sp.distance(self.iberia, km, 'València', 'Daroca')
        self.assertAlmostEqual(d, 191.914)
        d = sp.distance(self.unconnected, self.unconnected_weight, 0, 4)
        self.assertEqual(d, infinity)
        d = sp.distance(self.unconnected, self.unconnected_weight, 0, 6)
        self.assertEqual(d, 2)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()