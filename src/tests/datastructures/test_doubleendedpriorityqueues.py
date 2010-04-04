#coding: latin1
import unittest
from algoritmia.datastructures.doubleendedpriorityqueues import IntervalHeap
from random import seed, shuffle, randrange

class TestIntervalHeap(unittest.TestCase):
    def setUp(self):
        a = list(range(10)) * 2
        seed(0)
        shuffle(a)
        self.ih = IntervalHeap(a)
        
    def test_ctor_fromIterable_shouldGiveElementsInOrder(self):
        a = IntervalHeap([1,2,5,4,0,3,9,7,6,8])
        for i in range(5):
            v = a.extract_min()
            self.assertEqual(v, i)
            v = a.extract_max()
            self.assertEqual(v, 9-i)
        self.assertRaises(IndexError, a.extract_min)
        self.assertRaises(IndexError, a.extract_max)
            
    def test_iter_onIntervalHeap_shouldGiveAllItsElements(self):
        self.assertEqual(list(sorted(self.ih)), list(sorted(list(range(10))*2))) 

    def test_stress(self):
        seed(0)
        d = []
        ih1 = IntervalHeap()
        ih2 = IntervalHeap()
        for i in range(200):
            v = randrange(1000)
            d.append(v)
            ih1.add(v)
            ih2.add(v)
        self.assertEqual(len(ih1), 200)
        d.sort()
        self.assertEqual(d, list(sorted(ih1)))
        for i in range(len(d)):
            self.assertEqual(ih1.min(), d[i])
            self.assertEqual(ih2.max(), d[-i-1])
            v = ih1.extract_min()
            w = ih2.extract_max()
            self.assertEqual(v, d[i])
            self.assertEqual(w, d[-i-1])

    def test_repr_onIntervalHeap_shouldReturnEvaluableExpression(self):
        self.assertEqual(list(sorted(self.ih)), list(sorted(eval(repr(self.ih)))))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()