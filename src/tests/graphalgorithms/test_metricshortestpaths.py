#coding: latin1
import unittest
from algoritmia.data.iberia import cities, roads, km, coords
from algoritmia.problems.shortestpaths.metric import MetricDigraphShortestPaths
from algoritmia.datastructures.digraphs import UndirectedGraph, Digraph, WeightingFunction
from algoritmia.utils import infinity
from math import sqrt

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.iberia = UndirectedGraph(V=cities, E=roads)
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))
                
    def test_metric_shortest_path(self):
        def km(u, v, coords=coords):
            p, q = coords[u], coords[v]
            return sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
        
        sp = MetricDigraphShortestPaths(km)
        p = sp.shortest_path(self.iberia, km, 'Gandia', 'Cullera')
        self.assertEqual(p, ["Gandia", "Cullera"])
        p = sp.shortest_path(self.iberia, km, 'València', 'Daroca')
        self.assertEqual(p, ["València", "Sagunt", "Segorbe", "Teruel", "Monreal del Campo", "Daroca"])
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()