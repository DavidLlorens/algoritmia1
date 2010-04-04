#coding: latin1

import unittest
from algoritmia.problems.topsort import Topsorter 
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.datastructures.sets import IntSet
from algoritmia.problems.traversals import DepthFirstTraverser

class TestTopsorter(unittest.TestCase):
    def test_topsort(self):
        G = Digraph(E=[(0,1), (1,2), (2,3), (3,4), (4,5)])
        topsorter = Topsorter()
        self.assertEqual(tuple(topsorter.topsorted(G)), tuple(range(6)))
        int_topsorter = Topsorter(createDepthFirstTraverser=
                                  lambda G: DepthFirstTraverser(createSet=lambda V: IntSet(capacity=max(V)+1)))
        self.assertEqual(tuple(int_topsorter.topsorted(G)), tuple(range(6)))
        G = Digraph(E={'C': ['C++', 'Objective C', 'Java', 'C#'],
                       'C++': ['C#', 'Java'],
                       'Java': ['C#']})
        ts = tuple(topsorter.topsorted(G))
        for (u,v) in G.E:
            self.assertTrue(ts.index(u) < ts.index(v))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()