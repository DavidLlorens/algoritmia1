#coding: latin1

import unittest
from algoritmia.datastructures.digraphs import Digraph, UndirectedGraph
from algoritmia.problems.connectedcomponents import StrongConnectedComponentsFinder, SetMergingConnectedComponentsFinder, GraphTraversalConnectedComponentsFinder

class TestConnectedComponents(unittest.TestCase):
    def setUp(self):
        self.G = UndirectedGraph(E={0: [1, 2], 1: [2], 2:[], 3: [4], 4: [], 5:[6,7,8], 6: [7,8],  7:[8], 8:[]})
        self.chain = UndirectedGraph(E=[(0,1), (1,2), (2,3), (3,4), (4,5)])
        self.loop = UndirectedGraph(E=[(0,1), (1,2), (2,3), (3,4), (4,5), (5, 0)])
        self.islands= UndirectedGraph(E=[(0,1), (1,2), (2,0), (3, 4), (4,3)])
        
    def test_graph_traversal_connected_components(self):
        ccf = GraphTraversalConnectedComponentsFinder()
        ccs = []
        for cc in ccf.connected_components(self.G):
            ccs.append(tuple(sorted(cc)))
        ccs.sort()
        self.assertEqual(tuple(ccs), ((0, 1, 2), (3, 4), (5, 6, 7, 8)))
        
        ccs = []
        for cc in ccf.connected_components(self.chain):
            ccs.append(tuple(sorted(cc)))
        ccs.sort()
        self.assertEqual(tuple(ccs), ((0, 1, 2, 3, 4, 5),))
        
    def test_is_connected(self):
        ccf = GraphTraversalConnectedComponentsFinder()
        self.assertFalse(ccf.is_connected(self.G))
        self.assertTrue(ccf.is_connected(self.chain))
        self.assertTrue(ccf.is_connected(self.loop))

    def test_connected_components(self):
        ccf = SetMergingConnectedComponentsFinder()
        ccs = []
        for cc in ccf.connected_components(self.G):
            ccs.append(tuple(sorted(cc)))
        ccs.sort()
        self.assertEqual(tuple(ccs), ((0, 1, 2), (3, 4), (5, 6, 7, 8)))
        
        ccs = []
        for cc in ccf.connected_components(self.chain):
            ccs.append(tuple(sorted(cc)))
        ccs.sort()
        self.assertEqual(tuple(ccs), ((0, 1, 2, 3, 4, 5),))
        
    def test_strong_components(self):
        sccf = StrongConnectedComponentsFinder()
        self.G = Digraph(E={0: [1], 1: [2, 3], 2:[0, 3], 3: [6, 4], 4: [5, 6], 5:[4, 8], 6: [7],  7:[6, 8], 8:[]})
        ccs = []
        for cc in sccf.strong_connected_components(self.G):
            ccs.append(tuple(sorted(cc)))
        ccs.sort()
        self.assertEqual(tuple(ccs), ((0, 1, 2), (3,), (4, 5), (6, 7), (8,)))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()