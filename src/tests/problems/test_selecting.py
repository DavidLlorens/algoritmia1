#coding: latin1

import unittest
from algoritmia.problems.orderstatistics.selecting import *
from random import seed, randrange

class Test(unittest.TestCase):
    def setUp(self):
        seed(0)
        self.a = [randrange(100) for i in range(50)]
        self.sorted = list(sorted(self.a))
        self.rev = list(reversed(self.sorted))
        
    def test_quickselect(self):
        selector = QuickSelector()
        for i, v in enumerate(self.sorted):
            self.assertEqual(v, selector.select(self.a[:], i))
        for i, v in enumerate(self.sorted):
            self.assertEqual(v, selector.select(self.sorted[:], i))
        for i, v in enumerate(self.sorted):
            self.assertEqual(v, selector.select(self.rev[:], i))
        self.assertRaises(IndexError, selector.select, self.a[:], 200)

    def test_select(self):
        selector = MedianOf5Selector()
        for i, v in enumerate(self.sorted):
            self.assertEqual(v, selector.select(self.a[:], i))
        for i, v in enumerate(self.sorted):
            self.assertEqual(v, selector.select(self.sorted[:], i))
        rev = list(reversed(self.sorted))
        for i, v in enumerate(self.sorted):
            self.assertEqual(v, selector.select(self.rev[:], i))
        self.assertRaises(IndexError, selector.select, self.a[:], 200)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()