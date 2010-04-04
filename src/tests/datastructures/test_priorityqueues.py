#coding: latin1
import unittest
from algoritmia.datastructures.priorityqueues import Heap, MinHeap, MaxHeap
from algoritmia.datastructures.doubleendedpriorityqueues import MinMaxIntervalHeap
from random import seed, shuffle, randrange

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.minh1 = Heap(min)
        self.maxh1 = Heap(max)
        self.minmax = MinMaxIntervalHeap()
        a = list(range(10))*2
        seed(0)
        shuffle(a)
        self.minh2 = Heap(min, a)
        self.maxh2 = Heap(max, a)
        
    def test_ctor(self):
        a = Heap(min, [1,2,5,4,0,3,9,7,6,8])
        b = Heap(max, [1,2,5,4,0,3,9,7,6,8])
        c = MinMaxIntervalHeap([1,2,5,4,0,3,9,7,6,8])
        d = MinMaxIntervalHeap([1,2,5,4,0,3,9,7,6,8])
        for i in range(10):
            v = a.extract_opt()
            self.assertEqual(v, i)
            v = b.extract_opt()
            self.assertEqual(v, 9-i)
            v = c.extract_min()
            self.assertEqual(v, i)
            v = d.extract_max()
            self.assertEqual(v, 9-i)
        a = Heap(min)
        b = Heap(max)
        self.assertRaises(IndexError, a.extract_opt)
        self.assertRaises(IndexError, b.extract_opt)

    def test_add(self):
        self.minh1.add(-1)
        self.assertEqual(self.minh1.opt(), -1)
        self.minh2.add(-1)
        self.assertEqual(self.minh2.opt(), -1)
        self.maxh1.add(100)
        self.assertEqual(self.maxh1.opt(), 100)
        self.maxh2.add(100)
        self.assertEqual(self.maxh2.opt(), 100)
        
    def test_extract_opt(self):
        for i in range(10):
            self.assertEqual(i, self.minh2.extract_opt())
            self.assertEqual(i, self.minh2.extract_opt())
        for i in range(9, -1, -1):
            self.assertEqual(i, self.maxh2.extract_opt())
            self.assertEqual(i, self.maxh2.extract_opt())
        self.assertEqual(len(self.minh2), 0)
        self.assertEqual(len(self.maxh2), 0)
        
        d = MinMaxIntervalHeap([1,2,5,4,0,3,9,7,6,8])
        for i in range(5):
            mi = d.extract_min()
            ma = d.extract_max()
            self.assertEqual(mi, i)
            self.assertEqual(ma, 9-i)
            
    def test_MinHeap(self):
        mh = MinHeap(list(self.minh2))
        self.assertEqual(list(self.minh2), list(mh))

    def test_MaxHeap(self):
        mh = MaxHeap(list(self.maxh2))
        self.assertEqual(list(self.maxh2), list(mh))
            
    def test_iter(self):
        self.assertEqual(list(sorted(self.minh2)), list(sorted(list(range(10))*2))) 

    def test_repr(self):
        self.assertEqual(list(sorted(self.minh2)), list(sorted(eval(repr(self.minh2))))) 


         
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPoint2D']
    unittest.main()