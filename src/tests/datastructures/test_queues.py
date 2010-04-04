#coding: latin1

import unittest
from algoritmia.datastructures.queues import Fifo, Lifo

class TestFifo(unittest.TestCase):
    def setUp(self):
        self.a = Fifo()
        self.b = Fifo([1,2,3])
        self.c = Fifo(createList=list)
        self.d = Fifo([1,2,3], createList=list)
        
    def test_ctor(self):
        self.assertEqual(len(self.a), 0)
        self.assertEqual(len(self.b), 3)
        self.assertEqual(len(self.c), 0)
        self.assertEqual(len(self.d), 3)

    def test_push(self):
        self.a.push(1)
        self.assertEqual(len(self.a), 1)
        self.a.push(2)
        self.assertEqual(len(self.a), 2)
        v = self.a.pop()
        self.assertEqual(v, 1)
        self.b.push(1)
        self.assertEqual(len(self.b), 4)
        self.c.push(1)
        self.assertEqual(len(self.c), 1)
        self.d.push(1)
        self.assertEqual(len(self.d), 4)
        
    def test_pop(self):
        self.assertRaises(IndexError, self.a.pop)
        i = 1
        while len(self.b) > 0:
            v = self.b.pop()
            self.assertEqual(v, i)
            i+=1
        self.assertRaises(IndexError, self.c.pop)
        i = 1
        while len(self.d) > 0:
            v = self.d.pop()
            self.assertEqual(v, i)
            i+=1
    
    def test_top(self):
        self.assertRaises(IndexError, self.a.top)
        self.assertEqual(self.b.top(), 1)
        
    def test_repr(self):
        self.assertEqual(list(self.b), list(eval(repr(self.b))))
        
class TestLifo(unittest.TestCase):
    def setUp(self):
        self.a = Lifo()
        self.b = Lifo([1,2,3])

    def test_ctor(self):
        a = Lifo()
        b = Lifo([1,2,3])
        self.assertEqual(len(a), 0)
        self.assertEqual(len(b), 3)

    def test_push(self):
        self.a.push(1)
        self.assertEqual(len(self.a), 1)
        self.a.push(2)
        self.assertEqual(len(self.a), 2)
        v = self.a.pop()
        self.assertEqual(v, 2)
        
        self.assertEqual(len(self.b), 3)
        self.b.push(1)
        self.assertEqual(len(self.b), 4)
        
    def test_pop(self):
        self.assertRaises(IndexError, self.a.pop)
        i = 3
        while len(self.b) > 0:
            v = self.b.pop()
            self.assertEqual(v, i)
            i-=1
    
    def test_top(self):
        self.assertRaises(IndexError, self.a.top)
        self.assertEqual(self.b.top(), 3)
                
    def test_repr(self):
        self.assertEqual(list(self.b), list(eval(repr(self.b))))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()