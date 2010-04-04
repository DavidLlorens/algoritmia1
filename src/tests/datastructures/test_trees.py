#coding: latin1

import unittest
from algoritmia.datastructures.trees import DigraphTree, ListOfListsTree, ParentReferenceTree, BoundedArityTree
from algoritmia.datastructures.digraphs import Digraph

class TestDigraphTree(unittest.TestCase):
    def setUp(self):
        self.t = DigraphTree(Digraph(E=[(1,2), (1,5), (2,3), (2,4), (5,6), (5,7)]), 1)
        
    def test_root(self):
        self.assertEqual(self.t.root, 1)
        
    def test_succs(self):
        self.assertEqual(list(self.t.succs(1)), [2, 5])
        self.assertEqual(list(self.t.succs(7)), [])

    def test_preds(self):
        self.assertEqual(list(self.t.preds(2)), [1])
        self.assertEqual(list(self.t.preds(1)), [])

    def test_in_degree(self):
        self.assertEqual(self.t.in_degree(2), 1)
        self.assertEqual(self.t.in_degree(1), 0)

    def test_out_degree(self):
        self.assertEqual(self.t.out_degree(2), 2)
        self.assertEqual(self.t.out_degree(1), 2)
        
    def test_subtrees(self):
        tt = list(self.t.subtrees())
        self.assertEqual(tt[0].root, 2)
        self.assertEqual(tt[1].root, 5)
        
    def test_subtree(self):
        self.assertEqual(self.t.tree(2).root, 2)
        self.assertEqual(self.t.tree(5).root, 5)

    def test_repr(self):
        t = eval(repr(self.t))
        self.assertEqual(self.t.root, t.root)
        self.assertEqual(list(self.t.succs(t.root)), list(t.succs(t.root)))
        
class TestLolTree(unittest.TestCase):
    def setUp(self):
        self.t = ListOfListsTree([1, [2, [3], [4]], [5, [6], [7]]])
        
    def test_root(self):
        self.assertEqual(self.t.root, 1)
        
    def test_succs(self):
        self.assertEqual(list(self.t.succs(1)), [2, 5])
        self.assertEqual(list(self.t.succs(7)), [])

    def test_preds(self):
        self.assertEqual(list(self.t.preds(2)), [1])
        self.assertEqual(list(self.t.preds(1)), [])

    def test_in_degree(self):
        self.assertEqual(self.t.in_degree(2), 1)
        self.assertEqual(self.t.in_degree(1), 0)

    def test_out_degree(self):
        self.assertEqual(self.t.out_degree(2), 2)
        self.assertEqual(self.t.out_degree(1), 2)
        
    def test_subtrees(self):
        tt = list(self.t.subtrees())
        self.assertEqual(tt[0].root, 2)
        self.assertEqual(tt[1].root, 5)
        
    def test_subtree(self):
        self.assertEqual(self.t.tree(2).root, 2)
        self.assertEqual(self.t.tree(5).root, 5)

    def test_repr(self):
        t = eval(repr(self.t))
        self.assertEqual(self.t.root, t.root)
        self.assertEqual(list(self.t.succs(t.root)), list(t.succs(t.root)))

class TestParentRefTree(unittest.TestCase):
    def setUp(self):
        self.t = ParentReferenceTree([(2,1), (5,1), (3,2), (4,2), (6,5), (7,5)], 1)
        
    def test_root(self):
        self.assertEqual(self.t.root, 1)
        
    def test_succs(self):
        self.assertEqual(list(self.t.succs(1)), [2, 5])
        self.assertEqual(list(self.t.succs(7)), [])

    def test_preds(self):
        self.assertEqual(list(self.t.preds(2)), [1])
        self.assertEqual(list(self.t.preds(1)), [])

    def test_in_degree(self):
        self.assertEqual(self.t.in_degree(2), 1)
        self.assertEqual(self.t.in_degree(1), 0)

    def test_out_degree(self):
        self.assertEqual(self.t.out_degree(2), 2)
        self.assertEqual(self.t.out_degree(1), 2)

    def test_subtrees(self):
        tt = list(self.t.subtrees())
        self.assertEqual(tt[0].root, 2)
        self.assertEqual(tt[1].root, 5)
        
    def test_subtree(self):
        self.assertEqual(self.t.tree(2).root, 2)
        self.assertEqual(self.t.tree(5).root, 5)

    def test_repr(self):
        t = eval(repr(self.t))
        self.assertEqual(self.t.root, t.root)
        self.assertEqual(list(self.t.succs(t.root)), list(t.succs(t.root)))
        
class TestBoundedArityTree(unittest.TestCase):
    def setUp(self):
        self.t = BoundedArityTree(2, [1,2,5,3,4,6,7])
        
    def test_root(self):
        self.assertEqual(self.t.root, 1)
        
    def test_succs(self):
        self.assertEqual(list(self.t.succs(1)), [2, 5])
        self.assertEqual(list(self.t.succs(7)), [])

    def test_preds(self):
        self.assertEqual(list(self.t.preds(2)), [1])
        self.assertEqual(list(self.t.preds(1)), [])

    def test_in_degree(self):
        self.assertEqual(self.t.in_degree(2), 1)
        self.assertEqual(self.t.in_degree(1), 0)

    def test_out_degree(self):
        self.assertEqual(self.t.out_degree(2), 2)
        self.assertEqual(self.t.out_degree(1), 2)

    def test_subtrees(self):
        tt = list(self.t.subtrees())
        self.assertEqual(tt[0].root, 2)
        self.assertEqual(tt[1].root, 5)
        
    def test_subtree(self):
        self.assertEqual(self.t.tree(2).root, 2)
        self.assertEqual(self.t.tree(5).root, 5)
        
    def test_repr(self):
        t = eval(repr(self.t))
        self.assertEqual(self.t.root, t.root)
        self.assertEqual(list(self.t.succs(t.root)), list(t.succs(t.root)))
      
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()