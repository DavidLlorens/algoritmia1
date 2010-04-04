#coding: latin1
import unittest
from algoritmia.problems.geometry.closestpair import *

class TestClosestPair(unittest.TestCase):
    def setUp(self):
        self.z = [(0.5,3.5), (1,2), (3,2), (3.5,1.5), (4,3.5), (5,0.5), (5,3), (5.5,1.5)]
    
    def test_distance1(self):
        cpf = ClosestPointsFinder1()
        bfcpf = BruteForceClosestPointsFinder()
        self.assertEqual(cpf.distance_between_closest_points(self.z), 
                         bfcpf.distance_between_closest_points(self.z))

    def test_distance(self):
        cpf = ClosestPointsFinder()
        bfcpf = BruteForceClosestPointsFinder()
        self.assertEqual(cpf.distance_between_closest_points(self.z), 
                         bfcpf.distance_between_closest_points(self.z))

    def test_closestpair1(self):
        cpf = ClosestPointsFinder1()
        bfcpf = BruteForceClosestPointsFinder()
        self.assertEqual(cpf.closest_points(self.z), 
                         bfcpf.closest_points(self.z))

    def test_closestpair(self):
        cpf = ClosestPointsFinder()
        bfcpf = BruteForceClosestPointsFinder()
        self.assertEqual(cpf.closest_points(self.z), 
                         bfcpf.closest_points(self.z))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()