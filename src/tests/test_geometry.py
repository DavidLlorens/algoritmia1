#coding: latin1
import unittest
from algoritmia.problems.geometry.utils import Point2D, left, right, triangle_area

class TestPoint2D(unittest.TestCase):
    def test_ctor(self):
        p = Point2D(0, 0)
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)
        p = Point2D(1.0, 2.0)
        self.assertEqual(p, Point2D(1.0, 2.0))
        
class TestTurn(unittest.TestCase):
    def test_left_right(self):
        p = Point2D(0, 0)
        q = Point2D(1, 0)
        r = Point2D(0, 1)
        self.assertTrue(left(p, q, r))
        self.assertFalse(left(p, r, q))
        self.assertFalse(right(p, q, r))
        self.assertTrue(right(p, r, q))
        
class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        p = Point2D(0, 0)
        q = Point2D(1, 0)
        r = Point2D(0, 1)
        self.assertEqual(triangle_area(p, q, r), 0.5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPoint2D']
    unittest.main()