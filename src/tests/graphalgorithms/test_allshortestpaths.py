#coding: latin1
import unittest
from algoritmia.problems.allshortestpaths import AllShortestPaths, AllShortestPathDraft
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.utils import infinity
from algoritmia.data.mallorca import Mallorca, km

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))
        self.f = lambda a, b: 1
        
    def test_AllShortestPathsDraft_distances_onUnconnected(self):
        sp2 = AllShortestPathDraft()
        m = sp2.distances(self.unconnected, self.f)
        self.assertEqual(m[0,1], 1)
        self.assertEqual(m[0,5], 2)
        self.assertEqual(m[0,0], 0)
        self.assertEqual(m[5,0], infinity)

    def test_AllShortestPaths_distances_onUnconnected(self):
        sp = AllShortestPaths()
        m = sp.distances(self.unconnected, self.f)
        self.assertEqual(m[0,1], 1)
        self.assertEqual(m[0,5], 2)
        self.assertEqual(m[0,0], 0)
        self.assertEqual(m[5,0], infinity)
        
    def test_AllShortestPathsDraft_backpointers_onMallorca(self):
        sp1 = AllShortestPaths()
        sp2 = AllShortestPathDraft()
        m1 = sp1.distances(Mallorca, km)
        m2 = sp2.distances(Mallorca, km)
        self.assertEqual(m1, m2)
        
    def test_AllShortestPaths_backpointers_onUnconnected(self):
        sp2 = AllShortestPaths()
        back = dict(sp2.backpointers(self.unconnected, self.f))
        paths = tuple(sp2.shortest_paths(self.unconnected, back))
        self.assertTrue([1,3] in paths) 
        self.assertTrue([0,1,3] in paths)
        self.assertEqual(len(paths), 17)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()