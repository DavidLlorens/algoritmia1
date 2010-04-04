#coding: latin1
import unittest
from algoritmia.problems.arithmetics.power import power1, power

class TestPower(unittest.TestCase):
    def test_power1_and_power(self):
        N = (0, 10, 100, 1024)
        E = (0, 1, 2, 4, 5, 7, 10)
        for n in N:
            for e in E:
                self.assertEqual(n**e, power1(n, e)) 
                self.assertEqual(n**e, power(n, e)) 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()