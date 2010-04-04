import unittest

from algoritmia.problems.searching.randomizedbinary import RandomizedBinarySearcher
from random import seed

class TestRandomizedBinSearch(unittest.TestCase):
    def setUp(self):
        self.lists = ([10, 20, 30, 40, 60], [], [1], [10], [1,2], [1,20], [10,20])
        seed(0)
        
    def test_succesfullsearch(self):
        for alist in self.lists:
            for i in range(len(alist)):
                a = RandomizedBinarySearcher().index(alist, alist[i])
                self.assertEqual(a, i)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()