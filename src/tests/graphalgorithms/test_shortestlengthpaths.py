#coding: latin1
from algoritmia.problems.shortestpaths.backtracer import Backtracer
import unittest
from algoritmia.data.iberia import cities, roads, km, coords
from algoritmia.problems.shortestpaths.length import BreadthFirstShortestPaths
from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph, WeightingFunction
from algoritmia.utils import infinity
from math import sqrt

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.iberia = UndirectedGraph(V=cities, E=roads)
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))
        self.bfsp = BreadthFirstShortestPaths()
        
    def test_bfs_length(self):
        self.assertEqual(self.bfsp.distance(self.iberia, "Gandia", "Cullera"), 1)
        self.assertEqual(self.bfsp.distance(self.iberia, "València", "Daroca"), 5)
        self.assertEqual(self.bfsp.distance(self.unconnected, 0, 4), None)
        self.assertEqual(self.bfsp.distance(self.unconnected, 0, 6), 2)

    def test_bfs_shortest_path(self):
        self.assertEqual(self.bfsp.shortest_path(self.iberia, "Gandia", "Cullera"), ["Gandia", "Cullera"])
        self.assertEqual(self.bfsp.shortest_path(self.iberia, "València", "Daroca"), 
                         ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        self.assertEqual(self.bfsp.shortest_path(self.unconnected, 0, 4), None)
        self.assertEqual(self.bfsp.shortest_path(self.unconnected, 0, 6), [0, 2, 6])
        
    def test_bfs_shortest_path_backpointers_one_to_all(self):
        t = self.bfsp.some_to_some_backpointers(self.iberia, ['Gandia'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Cullera'), ["Gandia", "Cullera"])
        t = self.bfsp.one_to_all_backpointers(self.iberia, 'València')
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Daroca'), 
                         ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        t = self.bfsp.one_to_all_backpointers(self.unconnected, 0)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace(4), None)
        self.assertEqual(Backtracer(bp).backtrace(6), [0, 2, 6])

    def test_bfs_shortest_path_backpointers_some_to_all(self):
        t = self.bfsp.some_to_some_backpointers(self.iberia, ['Gandia', 'Vigo'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Cullera'), ["Gandia", "Cullera"])
        self.assertEqual(Backtracer(bp).backtrace('Ourense'), ["Vigo", "Ribadavia", "Ourense"])
        t = self.bfsp.some_to_some_backpointers(self.iberia, ['València', 'Madrid'], self.iberia.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace('Daroca'), 
                         ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        self.assertEqual(Backtracer(bp).backtrace('Cuenca'), 
                         ["Madrid", "Arganda del Rey", "Tarancón", "Cuenca"])
        t = self.bfsp.some_to_some_backpointers(self.unconnected, [0, 1], self.unconnected.V)
        bp = dict(t)
        self.assertEqual(Backtracer(bp).backtrace(4), None)
        self.assertEqual(Backtracer(bp).backtrace(6), [0, 2, 6])
        self.assertEqual(Backtracer(bp).backtrace(3), [1, 3])
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()