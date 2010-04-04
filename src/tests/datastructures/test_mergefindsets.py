#coding: latin1

import unittest
from algoritmia.datastructures.mergefindsets import (NaiveMergeFindSet, RankUnionMFset, 
                                                     PathCompressionMFset, MergeFindSet)
from algoritmia.datastructures.maps import IntKeyMap

class TestNaiveMFset(unittest.TestCase):
    def setUp(self):
        self.mf1 = NaiveMergeFindSet()
        self.mf2 = NaiveMergeFindSet(((i,) for  i in range(10)), createMap=lambda nodes: IntKeyMap(capacity=max(nodes)+1))

    def test_mfsets(self):
        for i in range(10):
            self.mf1.add(i)
        for i in range(10):
            self.assertEqual(self.mf1.find(i), i)
            self.assertEqual(self.mf2.find(i), i)
        for i in range(0, 10, 2):
            self.mf1.merge(i, i+1)
            self.mf2.merge(i, i+1)
        for i in range(0, 10, 2):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
        for i in range(0, 10-3, 4):
            self.mf1.merge(i, i+3)
            self.mf2.merge(i, i+3)
        for i in range(0, 10-4, 4):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+2))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+3))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+2))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+3))
            
    def test_repr(self):
        aux = dict((i, set()) for i in range(10))
        for i in range(10):
            aux[self.mf2.find(i)].add(i)
        all = set(frozenset(v) for v in aux.values())

        mf2 = eval(repr(self.mf2))
        aux = dict((i, set()) for i in range(10))
        for i in range(10):
            aux[self.mf2.find(i)].add(i)
        all2 = set(frozenset(v) for v in aux.values())
        self.assertEqual(all, all2)
        
class TestRankUnionMFset(unittest.TestCase):
    def setUp(self):
        self.mf1 = RankUnionMFset()
        self.mf2 = RankUnionMFset(((i,) for i in range(10)), createMap=lambda nodes: IntKeyMap(capacity=max(nodes)+1))

    def test_mfsets(self):
        for i in range(10):
            self.mf1.add(i)
        for i in range(10):
            self.assertEqual(self.mf1.find(i), i)
            self.assertEqual(self.mf2.find(i), i)
        for i in range(0, 10, 2):
            self.mf1.merge(i, i+1)
            self.mf2.merge(i, i+1)
        for i in range(0, 10, 2):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
        for i in range(0, 10-3, 4):
            self.mf1.merge(i, i+3)
            self.mf2.merge(i, i+3)
        for i in range(0, 10-4, 4):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+2))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+3))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+2))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+3))

    def test_repr(self):
        aux = dict((i, set()) for i in range(10))
        for i in range(10):
            aux[self.mf2.find(i)].add(i)
        all = set(frozenset(v) for v in aux.values())

        mf2 = eval(repr(self.mf2))
        aux = dict((i, set()) for i in range(10))
        for i in range(10):
            aux[self.mf2.find(i)].add(i)
        all2 = set(frozenset(v) for v in aux.values())
        self.assertEqual(all, all2)
                    
class TestPathCompressionMFset(unittest.TestCase):
    def setUp(self):
        self.mf1 = PathCompressionMFset()
        self.mf2 = PathCompressionMFset(((i,) for i in range(10)), createMap=lambda nodes: IntKeyMap(capacity=max(nodes)+1))

    def test_mfsets(self):
        for i in range(10):
            self.mf1.add(i)
        for i in range(10):
            self.assertEqual(self.mf1.find(i), i)
            self.assertEqual(self.mf2.find(i), i)
        for i in range(0, 10, 2):
            self.mf1.merge(i, i+1)
            self.mf2.merge(i, i+1)
        for i in range(0, 10, 2):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
        for i in range(0, 10-3, 4):
            self.mf1.merge(i, i+3)
            self.mf2.merge(i, i+3)
        for i in range(0, 10-4, 4):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+2))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+3))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+2))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+3))
    
    def test_repr(self):
        aux = dict((i, set()) for i in range(10))
        for i in range(10):
            aux[self.mf2.find(i)].add(i)
        all = set(frozenset(v) for v in aux.values())

        mf2 = eval(repr(self.mf2))
        aux = dict((i, set()) for i in range(10))
        for i in range(10):
            aux[self.mf2.find(i)].add(i)
        all2 = set(frozenset(v) for v in aux.values())
        self.assertEqual(all, all2)
    
class TestMFset(unittest.TestCase):
    def setUp(self):
        self.mf1 = MergeFindSet()
        self.mf2 = MergeFindSet(((i,) for i in range(10)), createMap=lambda nodes: IntKeyMap(capacity=max(nodes)+1))

    def test_mfsets(self):
        for i in range(10):
            self.mf1.add(i)
        for i in range(10):
            self.assertEqual(self.mf1.find(i), i)
            self.assertEqual(self.mf2.find(i), i)
        for i in range(0, 10, 2):
            self.mf1.merge(i, i+1)
            self.mf2.merge(i, i+1)
        for i in range(0, 10, 2):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
        for i in range(0, 10-3, 4):
            self.mf1.merge(i, i+3)
            self.mf2.merge(i, i+3)
        for i in range(0, 10-4, 4):
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+1))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+2))
            self.assertEqual(self.mf1.find(i), self.mf1.find(i+3))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+1))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+2))
            self.assertEqual(self.mf2.find(i), self.mf2.find(i+3))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()