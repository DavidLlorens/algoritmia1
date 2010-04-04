#coding: latin1
import unittest
from algoritmia.problems.orderstatistics.minmax import DirectMinMaxFinder, MinMaxFinder

class TestDirectMinMax(unittest.TestCase):
    def setUp(self):
        self.lists = (list(reversed(range(100))),
                      list(reversed(range(100))) + list(range(0, 200, 3)),
                      list(range(100)),
                      list(range(0, 100, 2)))
    
    def test_directminmax(self):
        dmm = DirectMinMaxFinder()
        for l in self.lists:
            self.assertEqual(dmm.min_max(l), (min(l), max(l)))

    def test_minmax(self):
        dmm = MinMaxFinder()
        for l in self.lists:
            self.assertEqual(dmm.min_max(l), (min(l), max(l)))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()