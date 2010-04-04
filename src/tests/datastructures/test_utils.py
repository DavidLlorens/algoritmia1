#coding: latin1
import unittest
from algoritmia.utils import min, max, argmax, argmin, infinity, count

class TestMinMax(unittest.TestCase):
    def testInfinty(self):
        self.assertTrue(infinity > 1)
        self.assertTrue(infinity > 2**1000)
        self.assertTrue(-infinity < 2**1000)

    def testMin(self):
        self.assertEqual(min(1,2,3,4), 1)
        self.assertEqual(min([1]), 1)
        self.assertEqual(min([], ifempty=123), 123)
        self.assertRaises(ValueError, min, [])
        
    def test_Max(self):
        self.assertEqual(max(1,2,3,4), 4)
        self.assertEqual(max([1]), 1)
        self.assertEqual(max([], ifempty=123), 123)
        self.assertRaises(ValueError, max, [])

    def test_argmin(self):
        self.assertEqual(argmin((1,2,3,4), lambda x: -x), 4)    
        self.assertEqual(argmin([], lambda x: -x), None)

    def test_argmax(self):
        self.assertEqual(argmax((1,2,3,4), lambda x: -x), 1)
        self.assertEqual(argmax([], lambda x: -x), None)
    
    def test_count(self):
        self.assertEqual(10, count(range(10)))
        self.assertEqual(10, count(list(range(10))))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()