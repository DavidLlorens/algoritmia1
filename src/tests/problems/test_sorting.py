#coding: latin1

import unittest
from algoritmia.problems.sorting import *
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver
from random import seed, shuffle

class TestPoint2D(unittest.TestCase):
    def setUp(self):
        seed(0)
        a = list(range(10)) + list(range(10)) 
        self.lists = [a, [], [0], list(sorted(a)), list(reversed(sorted(a)))]
        b = a[:]
        shuffle(b)
        self.lists.append(b)
        
    def test_selectionsort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            InPlaceSelectionSorter().sort(s)
            self.assertEqual(s, a)

    def test_bubblesort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            InPlaceBubbleSorter().sort(s)
            self.assertEqual(s, a)
    
    def test_insertionsort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            InPlaceInsertionSorter().sort(s)
            self.assertEqual(s, a)

    def test_quicksort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            InPlaceQuickSorter().sort(s)
            self.assertEqual(s, a)
    
    def test_countingsort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            s = list(CountingSorter().sorted(s))
            self.assertEqual(s, a)

    def test_heapsort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            s = list(HeapSorter().sorted(s))
            self.assertEqual(s, a)

    def test_mergesort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            s = list(MergeSorter().sorted(s))
            self.assertEqual(s, a)

    def test_inplacemergesort(self):
        for a in self.lists:
            s = a[:]
            a.sort()
            InPlaceMergeSorter().sort(s)
            self.assertEqual(s, a)

    def test_mergesort_problem(self):
        for a in self.lists:
            p = MergesortProblem(a[:])
            a.sort()
            s = DivideAndConquerSolver().solve(p)
            self.assertEqual(s, a)

    def test_inplacemergesort_problem(self):
        for a in self.lists:
            p = InPlaceMergesortProblem(a[:])
            a.sort()
            p = DivideAndConquerSolver().solve(p)
            self.assertEqual(p.a, a)

    def test_inplacemergesort_with_threshold(self):
        for threshold in 1, 2, 3, 4, 5:
            for a in self.lists:
                s = a[:]
                a.sort()
                ThresholdedInPlaceMergeSorter(threshold).sort(s)
                self.assertEqual(s, a)

    def test_quicksort1(self):
        for a in self.lists:
            s = BasicQuickSorter().sorted(a)
            a.sort()
            self.assertEqual(s, a)

    def test_in_place_quicksort(self):
        for a in self.lists:
            s = a[:]
            BasicInPlaceQuickSorter().sort(s)
            a.sort()
            self.assertEqual(s, a)

    def test_randomized_quicksort(self):
        for a in self.lists:
            s = a[:]
            RandomizedInPlaceQuickSorter().sort(s)
            a.sort()
            self.assertEqual(s, a)

    def test_semi_iterative_quicksort1(self):
        for a in self.lists:
            s = a[:]
            BasicSemiIterativeInPlaceQuickSorter().sort(s)
            a.sort()
            self.assertEqual(s, a)

    def test_semi_iterative_quicksort2(self):
        for a in self.lists:
            s = a[:]
            SemiIterativeInPlaceQuickSorter1().sort(s)
            a.sort()
            self.assertEqual(s, a)

    def test_semi_iterative_quicksort(self):
        for a in self.lists:
            s = a[:]
            SemiIterativeInPlaceQuickSorter().sort(s)
            a.sort()
            self.assertEqual(s, a)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()