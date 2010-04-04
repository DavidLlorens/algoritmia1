import unittest

from algoritmia.problems.convexmin import ConvexMin1, ConvexMin, IterativeConvexMin

class Test(unittest.TestCase):
    def setUp(self):
        self.lists = [9.5, 8, 6, 5, 4.5, 3.5, 3.25, 5.75, 6.5, 8.25], [10, 4, 3, 0], [0, 2, 10, 60], [1]

    def test_convexmin1(self):
        for l in self.lists:
            self.assertEqual(min(l), ConvexMin1().min(l))

    def test_convexmin(self):
        for l in self.lists:
            self.assertEqual(min(l), ConvexMin().min(l))

    def test_iterativeconvexmin(self):
        for l in self.lists:
            self.assertEqual(min(l), IterativeConvexMin().min(l))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()