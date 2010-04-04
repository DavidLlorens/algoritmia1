#coding: latin1
import unittest
from algoritmia.problems.closures import *
from algoritmia.datastructures.digraphs import Digraph

class TestMatrixTransitiveClosure(unittest.TestCase):
    def setUp(self):
        self.chain = [[0,1,0,0,0],
                      [0,0,1,0,0],
                      [0,0,0,1,0],
                      [0,0,0,0,1],
                      [0,0,0,0,0]]
        self.loop =  [[0,1,0,0,0],
                      [0,0,1,0,0],
                      [0,0,0,1,0],
                      [0,0,0,0,1],
                      [1,0,0,0,0]]
        self.islands=[[0,1,0,0,0],
                      [0,0,1,0,0],
                      [1,0,0,0,0],
                      [0,0,0,0,1],
                      [0,0,0,1,0]]
        
    def test_closure(self):
        mptc = MatrixTransitiveClosureFinder()
        wmtc = WarshallMatrixTransitiveClosureFinder()
        for func in (mptc.transitive_closure, wmtc.transitive_closure):
            c = func(self.chain)
            for i in range(len(c)):
                for j in range(len(c)):
                    if i < j: self.assertEqual(1, c[i][j])
                    else: self.assertEqual(0, c[i][j])
            c = func(self.loop)
            for i in range(len(c)):
                for j in range(len(c)):
                    self.assertEqual(1, c[i][j])
            c = func(self.islands)
            for i in range(len(c)):
                for j in range(len(c)):
                    if i < 3 and j < 3 or i >= 3 and j >= 3:
                        self.assertEqual(1, c[i][j])
                    else:
                        self.assertEqual(0, c[i][j])
                        

class TestDigraphTransitiveClosure(unittest.TestCase):
    def setUp(self):
        self.chain = Digraph(E=[(0,1), (1,2), (2,3), (3,4), (4,5)])
        self.loop = Digraph(E=[(0,1), (1,2), (2,3), (3,4), (4,5), (5, 0)])
        self.islands= Digraph(E=[(0,1), (1,2), (2,0), (3, 4), (4,3)])
        
    def test_closure(self):
        dtc = DigraphTransitiveClosureFinder()
        c = dtc.transitive_closure(self.chain)
        for i in c.V:
            for j in c.V:
                if i < j: self.assertTrue((i,j) in c.E)
                else: self.assertFalse((i,j) in c.E)
        c = dtc.transitive_closure(self.loop)
        for i in c.V:
            for j in c.V:
                self.assertTrue((i,j) in c.E)
        c = dtc.transitive_closure(self.islands)
        for i in c.V:
            for j in c.V:
                if i < 3 and j < 3 or i >= 3 and j >= 3:
                    self.assertTrue((i,j) in c.E)
                else:
                    self.assertFalse((i,j) in c.E)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()