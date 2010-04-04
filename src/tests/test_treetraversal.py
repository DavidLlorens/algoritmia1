#coding: latin1
import unittest
from algoritmia.datastructures.trees import ListOfListsTree
from algoritmia.problems.traversals.treetraversals import *
from algoritmia.utils import count

class TestLevelOrderTreeTraverser(unittest.TestCase):
    def setUp(self):
        self.t = ListOfListsTree([0, [1, [4]], [2, [5], [6]], [3, [7, [9], [10]], [8]]])
                
    def test_LevelOrderTreeTraverser_onITree_enumeratesNodes(self):
        for i,v in enumerate(LevelOrderTreeTraverser().traverse(self.t)):
            self.assertEqual(i, v)

    def test_LevelOrderTreeTraverser_onITree_appliesVisitor(self):
        for i, child in enumerate(LevelOrderTreeTraverser().traverse(self.t, visitor=lambda t: t)):
            self.assertEqual(self.t.out_degree(i), child.out_degree(child.root))

class TestPreOrderTreeTraverser(unittest.TestCase):        
    def setUp(self):
        self.t = ListOfListsTree([0, [1, [2, [3, [4], [5, [6], [7]]], [8]], [9, [10]]]])

    def test_PreOrderTreeTraverser_onITree_enumeratesNodes(self):
        for i,v in enumerate(PreorderTreeTraverser().traverse(self.t)):
            self.assertEqual(i, v)

    def test_PreOrderTreeTraverser_onITree_appliesVisitor(self):
        for i, child in enumerate(PreorderTreeTraverser().traverse(self.t, visitor=lambda t: t)):
            self.assertEqual(self.t.out_degree(i), child.out_degree(child.root))

class TestPostOrderTreeTraverser(unittest.TestCase):        
    def setUp(self):
        self.t = ListOfListsTree([10, [9, [6, [4, [0], [3, [1], [2]]], [5]], [8, [7]]]])

    def test_PostOrderTreeTraverser_onITree_enumeratesNodes(self):
        for i,v in enumerate(PostorderTreeTraverser().traverse(self.t)):
            self.assertEqual(i, v)

    def test_PostOrderTreeTraverser_onITree_appliesVisitor(self):
        for i, child in enumerate(PostorderTreeTraverser().traverse(self.t, visitor=lambda t: t)):
            self.assertEqual(self.t.out_degree(i), child.out_degree(child.root))
            
class TestInOrderTreeTraverser(unittest.TestCase):        
    def setUp(self):
        self.t = ListOfListsTree([5, [3, [1, [0], [2]], [4]], [7, [6], [8]]])

    def test_InOrderTreeTraverser_onITree_enumeratesNodes(self):
        for i, v in enumerate(InorderTreeTraverser().traverse(self.t)):
            self.assertEqual(i, v)

    def test_InOrderTreeTraverser_onITree_appliesVisitor(self):
        for i, child in enumerate(InorderTreeTraverser().traverse(self.t, visitor=lambda t: t)):
            self.assertEqual(self.t.out_degree(i), child.out_degree(child.root))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()