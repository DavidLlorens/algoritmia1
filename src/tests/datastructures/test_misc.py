'''
Created on 20/05/2009

@author: Andres
'''
import unittest
from algoritmia.datastructures.misc import RangeSet

class TestRangeSet(unittest.TestCase):
    def setUp(self):
        self.r1 = RangeSet(0, 10)
        self.r2 = RangeSet(11, 20)
        self.r3 = RangeSet(0, 0)

    def test_len(self):
        self.assertEqual(len(self.r1), 11)
        self.assertEqual(len(self.r2), 10)
        self.assertEqual(len(self.r3), 1)

    def test_contains(self):
        for i in range(11):
            self.assertTrue(i in self.r1)
            self.assertFalse(i in self.r2)
        for i in range(11, 21):
            self.assertTrue(i in self.r2)
            self.assertFalse(i in self.r1)
            self.assertFalse(i in self.r3)
        self.assertTrue(0 in self.r3)

    def test_iter(self):
        self.assertEqual(list(range(11)), list(self.r1))
        self.assertEqual(list(range(11, 21)), list(self.r2))
        self.assertEqual([0], list(self.r3))

    def test_repr(self):
        self.assertEqual(list(range(11)), list(eval(repr(self.r1))))
        self.assertEqual(list(range(11, 21)), list(eval(repr(self.r2))))
        self.assertEqual([0], list(eval(repr(self.r3))))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()