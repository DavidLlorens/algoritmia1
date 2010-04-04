#coding: latin1

import unittest
from algoritmia.problems.searching import (BinarySearcher, NaiveSequentialSearcher, 
                                  SequentialSearcher, RecursiveBinarySearcher, 
                                  ThresholdedBinarySearcher, 
                                  IterativeBinarySearcher, BinarySearchProblem)

from algoritmia.schemes.decreaseandconquer import DecreaseAndConquerSolver, TailRecursiveDecreaseAndConquerSolver, IterativeDecreaseAndConquerSolver

class TestSortedSeracherMethods(unittest.TestCase):
    def setUp(self):
        self.lists = ([10, 20, 30, 40, 60], [1], [10], [1,2], [1,20], [10,20])
    
    def test_BinarySearcher_onEmptyList_returnsNone(self):
        a = BinarySearcher().index([], 1)
        self.assertEqual(a, None)
    
    def test_RecursiveBinarySearcher_onEmptyList_returnsNone(self):
        a = RecursiveBinarySearcher().index([], 1)
        self.assertEqual(a, None)

    def test_IterativeBinarySearcher_onEmptyList_returnsNone(self):
        a = IterativeBinarySearcher().index([], 1)
        self.assertEqual(a, None)
    
    def test_NaiveSequentialSearcher_onEmptyList_returnsNone(self):
        a = NaiveSequentialSearcher().index([], 1)
        self.assertEqual(a, None)

    def test_SequentialSearcher_onEmptyList_returnsNone(self):
        a = SequentialSearcher().index([], 1)
        self.assertEqual(a, None)
    
    def test_BinarySearcher_searchesExistingItem_andFindsIt(self):
        for alist in self.lists:
            for i in range(len(alist)):
                a = BinarySearcher().index(alist, alist[i])
                self.assertEqual(a, i)

    def test_NaiveSequentialSearcher_searchesExistingItem_andFindsIt(self):
        for alist in self.lists:
            for i in range(len(alist)):
                a = NaiveSequentialSearcher().index(alist, alist[i])
                self.assertEqual(a, i)

    def test_SequentialSearcher_searchesExistingItem_andFindsIt(self):
        for alist in self.lists:
            for i in range(len(alist)):
                a = SequentialSearcher().index(alist, alist[i])
                self.assertEqual(a, i)

    def test_RecursiveBinarySearcher_searchesExistingItem_andFindsIt(self):
        for alist in self.lists:
            for i in range(len(alist)):
                a = IterativeBinarySearcher().index(alist, alist[i])
                self.assertEqual(a, i)

    def test_IterativeBinarySearcher_searchesExistingItem_andFindsIt(self):
        for alist in self.lists:
            for i in range(len(alist)):
                a = IterativeBinarySearcher().index(alist, alist[i])
                self.assertEqual(a, i)

    def test_ThresholderBinarySearch_searchesExistingItemWithDifferentThreshold_andFindsIt(self):
        for alist in self.lists:
            for i in range(len(alist)):
                for t in range(5):
                    a = ThresholdedBinarySearcher(t).index(alist, alist[i])
                    self.assertEqual(a, i)

    def test_BinarySearcher_searchesNonExistingItem_andReturnsNone(self):
        for alist in self.lists:
            for i in 5, 15, 25, 45, 65:
                a = BinarySearcher().index(alist, i)
                self.assertEqual(a, None)

    def test_NaiveSequentialSearcher_searchesNonExistingItem_andReturnsNone(self):
        for alist in self.lists:
            for i in 5, 15, 25, 45, 65:
                a = NaiveSequentialSearcher().index(alist, i)
                self.assertEqual(a, None)

    def test_SequentialSearcher_searchesNonExistingItem_andReturnsNone(self):
        for alist in self.lists:
            for i in 5, 15, 25, 45, 65:
                a = SequentialSearcher().index(alist, i)
                self.assertEqual(a, None)

    def test_RecursiveBinarySearcher_searchesNonExistingItem_andReturnsNone(self):
        for alist in self.lists:
            for i in 5, 15, 25, 45, 65:
                a = RecursiveBinarySearcher().index(alist, i)
                self.assertEqual(a, None)

    def test_IterativeBinarySearcher_searchesNonExistingItem_andReturnsNone(self):
        for alist in self.lists:
            for i in 5, 15, 25, 45, 65:
                a = IterativeBinarySearcher().index(alist, i)
                self.assertEqual(a, None)

    def test_ThresholderBinarySearch_searchesNonExistingItemWithDifferentThreshold_andReturnsNone(self):
        for alist in self.lists:
            for i in 5, 15, 25, 45, 65:
                for t in range(5):
                    a = ThresholdedBinarySearcher(t).index(alist, i)
                    self.assertEqual(a, None)
                    
class TestDivideAndConquerBynarySearch(unittest.TestCase):
    def setUp(self):
        self.lists = ([10, 20, 30, 40, 60], [], [1], [10], [1,2], [1,20], [10,20])

    def test_DecreaseAndConquerBinarySearchProblem_searchesExistingItem_andFindsIt(self):
        for a in self.lists:
            for i in range(len(a)):
                p = BinarySearchProblem(a, a[i])
                j = DecreaseAndConquerSolver().solve(p)
                self.assertEqual(i, j)
                
    def test_TailRecursiveDecreaseAndConquerBinarySearchProblem_searchesExistingItem_andFindsIt(self):
        for a in self.lists:
            for i in range(len(a)):
                p = BinarySearchProblem(a, a[i])
                j = TailRecursiveDecreaseAndConquerSolver().solve(p)
                self.assertEqual(i, j)

    def test_IterativeDecreaseAndConquerBinarySearchProblem_searchesExistingItem_andFindsIt(self):
        for a in self.lists:
            for i in range(len(a)):
                p = BinarySearchProblem(a, a[i])
                j = IterativeDecreaseAndConquerSolver().solve(p)
                self.assertEqual(i, j)

    def test_DecreaseAndConquerBinarySearchProblem_searchesNoneExistingItem_andReturnNone(self):
        for a in self.lists:
            for v in 5, 15, 25, 45, 65:
                p = BinarySearchProblem(a, v)
                i = DecreaseAndConquerSolver().solve(p)
                self.assertEqual(i, None)

    def test_TailRecursiveDecreaseAndConquerBinarySearchProblem_searchesNoneExistingItem_andReturnNone(self):
        for a in self.lists:
            for v in 5, 15, 25, 45, 65:
                p = BinarySearchProblem(a, v)
                i = TailRecursiveDecreaseAndConquerSolver().solve(p)
                self.assertEqual(i, None)

    def test_IterativeDecreaseAndConquerBinarySearchProblem_searchesNoneExistingItem_andReturnNone(self):
        for a in self.lists:
            for v in 5, 15, 25, 45, 65:
                p = BinarySearchProblem(a, v)
                i = IterativeDecreaseAndConquerSolver().solve(p)
                self.assertEqual(i, None)

    def test_DecreaseAndConquerBinarySearchProblem_onEmptyList_returnsNone(self):
        p = BinarySearchProblem([], 1)
        j = DecreaseAndConquerSolver().solve(p)
        self.assertEqual(j, None)

    def test_TailRecursiveDecreaseAndConquerBinarySearchProblem_onEmptyList_returnsNone(self):
        p = BinarySearchProblem([], 1)
        j = TailRecursiveDecreaseAndConquerSolver().solve(p)
        self.assertEqual(j, None)

    def test_IterativeDecreaseAndConquerBinarySearchProblem_onEmptyList_returnsNone(self):
        p = BinarySearchProblem([], 1)
        j = IterativeDecreaseAndConquerSolver().solve(p)
        self.assertEqual(j, None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()