#coding: latin1

import unittest
from algoritmia.datastructures.prioritymaps import (HeapMap, MinHeapMap, MaxHeapMap, FibonacciHeap)
from algoritmia.datastructures.doubleendedprioritymaps import MinMaxIntervalHeapMap

class TestPriorityDicts(unittest.TestCase):
    def setUp(self):
        self.pd1 = HeapMap(opt=min)
        self.mpd1 = MinMaxIntervalHeapMap()
        self.pairs = [('a', 1), ('z', 10), ('b', 5), ('c', 8), ('d', 12), ('e', 10)]
        self.pd2 = HeapMap(min, self.pairs)
        self.mpd2 = MinMaxIntervalHeapMap(self.pairs)
        self.pairdict = dict(self.pairs)
        self.pd3 = HeapMap(min, self.pairdict)
        self.mpd3 = MinMaxIntervalHeapMap(self.pairdict)
        
    def test_ctor(self):
        self.assertEqual(len(self.pd1), 0)
        self.assertEqual(len(self.mpd1), 0)
        self.assertEqual(len(self.pd2), 6)
        self.assertEqual(len(self.mpd2), 6)
        self.assertEqual(len(self.pd2), 6)
        self.assertEqual(len(self.mpd2), 6)

    def test_opt(self):
        self.assertRaises(IndexError, self.pd1.opt)
        self.assertRaises(IndexError, self.mpd1.opt)
        for i in (1, 5, 8, 10, 10, 12):
            self.assertEqual(self.pd2[self.pd2.opt()], i)
            self.pd2.extract_opt()
            self.assertEqual(self.mpd2[self.mpd2.opt()], i)
            self.mpd2.extract_opt()
            self.assertEqual(self.pd3[self.pd3.opt()], i)
            self.pd3.extract_opt()
            self.assertEqual(self.mpd3[self.mpd3.opt()], i)
            self.mpd3.extract_opt()

    def test_getitem(self):
        for k, v in self.pairs:
            self.assertEqual(self.pd2[k], v)
            self.assertEqual(self.mpd2[k], v)
            self.assertEqual(self.pd3[k], v)
            self.assertEqual(self.mpd3[k], v)
        self.assertRaises(KeyError, self.pd2.__getitem__, 'xx')
        self.assertRaises(KeyError, self.mpd2.__getitem__, 'xx')
        self.assertRaises(KeyError, self.pd3.__getitem__, 'xx')
        self.assertRaises(KeyError, self.mpd3.__getitem__, 'xx')

    def test_setitem(self):
        for pd in self.pd1, self.pd2, self.pd3, self.mpd1, self.mpd2, self.mpd3:
            for k, v in pd.items():
                pd[k] = pd[k] + 1
                self.assertEqual(pd[k], v+1)
                pd[k] = pd[k] - 10
                self.assertEqual(pd[k], v-9)
            for k, v in ('xx', 10), ('yy', 100):
                pd[k] = v
                self.assertEqual(pd[k], v)
                
    def test_opt_value_and_item(self):
        for pd in self.pd1, self.pd2, self.pd3, self.mpd1, self.mpd2, self.mpd3:
            if len(pd) > 0:
                self.assertEqual(pd.opt_item()[1], pd.opt_value())
                self.assertEqual(pd.opt_item()[0], pd.opt())
            else:
                self.assertRaises(IndexError, pd.opt_item)
                
    def test_contains(self):
        for pd in self.pd2, self.pd3, self.mpd2, self.mpd3:
            for k, v in self.pairs:
                self.assertTrue(k in pd)
        for pd in self.pd1, self.mpd1:
            for k, v in self.pairs:
                self.assertFalse(k in pd)
    
    def test_del(self):
        for pd in self.pd2, self.pd3, self.mpd2, self.mpd3:
            for k, v in self.pairs:
                del pd[k]
            self.assertEqual(len(pd), 0)
            
    def test_repr(self):
        i = 0
        for pd in self.pd1, self.pd2, self.pd3, self.mpd1, self.mpd2, self.mpd3:
            i += 1
            if len(pd) > 0:
                self.assertEqual(list(sorted(self.pairs)), list(sorted(eval(repr(pd)).items())))

    def test_min_and_max_prioritydics(self):
        a = MinHeapMap(self.pairs)
        b = MaxHeapMap(self.pairs)
        self.assertEqual(len(self.pairs), len(a))
        self.assertEqual(len(self.pairs), len(b))

class TestMinMaxPriorityDicts(unittest.TestCase):
    def setUp(self):
        self.pairs = [('a', 1), ('z', 11), ('b', 5), ('c', 8), ('d', 12), ('e', 10)]
        self.a = MinMaxIntervalHeapMap(self.pairs)
        
    def test_len(self):
        self.assertEqual(len(self.pairs), len(self.a))

    def test_opt_worst(self):
        self.assertEqual('a', self.a.opt())
        self.assertEqual(1, self.a.opt_value())
        self.assertEqual(('a', 1), self.a.opt_item())
        self.assertEqual('d', self.a.worst())
        self.assertEqual(12, self.a.worst_value())
        self.assertEqual(('d', 12), self.a.worst_item())
        
        self.assertEqual('a', self.a.extract_min())
        self.assertEqual(5, self.a.extract_min_value())
        self.assertEqual(('c', 8), self.a.extract_min_item())
        self.assertEqual('d', self.a.extract_max())
        self.assertEqual(11, self.a.extract_max_value())
        self.assertEqual(('e', 10), self.a.extract_max_item())
        
class TestFibonacciHeap(unittest.TestCase):
    def setUp(self):
        self.pairs = [('a', 1), ('z', 11), ('b', 5), ('c', 8), ('d', 12), ('e', 10)]
        self.a = FibonacciHeap(min, self.pairs)
        
    def test_len(self):
        self.assertEqual(len(self.pairs), len(self.a))
        
    def test_opt(self):
        for i in (1, 5, 8, 10, 11, 12):
            self.assertEqual(self.a[self.a.opt()], i)
            self.a.extract_opt()
    
    def test_getitem(self):
        for k, v in self.pairs:
            self.assertEqual(self.a[k], v)
        self.assertRaises(KeyError, self.a.__getitem__, 'xx')

    def test_setitem(self):
        for k, v in self.a.items():
            v = self.a[k]
            self.assertRaises(ValueError, self.a.__setitem__, k, v+1)
            self.a[k] = self.a[k] - 10
            self.assertEqual(self.a[k], v-10)
        for k, v in ('xx', 10), ('yy', 100):
            self.a[k] = v
            self.assertEqual(self.a[k], v)
        
        v = -100
        while len(self.a) > 0:
            w = self.a.opt_value()
            self.assertTrue(v <= w)
            self.a.extract_opt()
            v = w
            
    def test_opt_value_and_item(self):
        if len(self.a) > 0:
            self.assertEqual(self.a.opt_item()[1], self.a.opt_value())
            self.assertEqual(self.a.opt_item()[0], self.a.opt())
        else:
            self.assertRaises(IndexError, self.a.opt_item)

    def test_contains(self):
        for k, v in self.pairs:
            self.assertTrue(k in self.a)
        for k in 'x', 'y', '':
            self.assertFalse(k in self.a)

    def test_del(self): 
        for k, v in self.pairs:
            del self.a[k]
        self.assertEqual(len(self.a), 0)
        
    def test_repr(self):
        self.assertEqual(len(self.a), len(eval(repr(self.a))))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()