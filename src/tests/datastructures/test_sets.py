import unittest
from algoritmia.datastructures.sets import CollectionSet, IntSet
from algoritmia.datastructures.lists import LinkedList
from algoritmia.datastructures.collections import LinkedListCollection

class Test_ListSet(unittest.TestCase):
    def setUp(self):
        self.data = [10, 60, 20, 30, 30, 40, 50]
        self.set0 = set(self.data)
        self.set1 = CollectionSet(self.data) 

    def test_init(self):
        self.assertEqual(self.set1, self.set0)
        
    def test_len(self):
        self.assertEqual(len(self.set1), len(self.set0))

    def test_remove(self):
        self.set0.remove(10)
        self.set1.remove(10)
        self.assertEqual(self.set1, self.set0)
        self.assertRaises(KeyError, self.set0.remove, 1000)
        
    def test_discard(self):
        self.set0.discard(10)
        self.set1.discard(10)
        self.assertEqual(self.set1, self.set0)
        n = len(self.set0)
        self.set0.discard(10000)    
        self.assertEqual(n, len(self.set0))
    
    def test_contains(self):
        self.assertEqual(10 in self.set1, 10 in self.set0)
        self.assertEqual(1 in self.set1, 1 in self.set0)

    def test_clear(self):
        self.set1.clear()
        self.assertEqual(len(self.set1), 0)

    def test_iter(self):
        self.assertEqual(sorted(self.set1), sorted(self.set0))
        
    def test_add(self):
        n = len(self.set1)
        self.set1.add(5)
        self.assertEqual(len(self.set1), n+1)
        self.assertTrue(5 in self.set1)
        self.set1.add(10)
        self.assertEqual(len(self.set1), n+1)

    def test_add_unchecked(self):
        n = len(self.set1)
        self.set1.add_unchecked(5)
        self.assertEqual(len(self.set1), n+1)
        self.assertTrue(5 in self.set1)

    def test_ops(self):
        a = set([1,2,4])
        b = set([1,5,6])
        A = CollectionSet(a)
        B = CollectionSet(b)
        C = CollectionSet([2,4])
        self.assertEqual(tuple(sorted(a | b)), tuple(sorted(A | B)))
        self.assertEqual(tuple(sorted(a & b)), tuple(sorted(A & B)))
        self.assertEqual(tuple(sorted(a - b)), tuple(sorted(A - B)))
        self.assertEqual(tuple(sorted(a ^ b)), tuple(sorted(A ^ B)))
        self.assertTrue(C < A)
        self.assertTrue(C <= A)
        self.assertTrue(A > C)
        self.assertTrue(A|B == B|A)
        self.assertTrue(C.isdisjoint(B))
        self.assertFalse(A|B != B|A)
        
    def test_repr(self):
        self.assertEqual(list(sorted(set(self.data))), list(sorted(eval(repr(self.set1)))))

class Test_LinkedListSet(unittest.TestCase):
    def setUp(self):
        self.data = [10, 60, 20, 30, 30, 40, 50]
        self.set0 = set(self.data)
        self.set1 = CollectionSet(self.data, createCollection=LinkedListCollection) 
        
    def test_init(self):
        self.assertEqual(self.set1, self.set0)

    def test_len(self):
        self.assertEqual(len(self.set1), len(self.set0))

    def test_remove(self):
        self.set0.remove(10)
        self.set1.remove(10)
        self.assertEqual(self.set1, self.set0)
        self.assertRaises(KeyError, self.set0.remove, 1000)
        
    def test_discard(self):
        self.set0.discard(10)
        self.set1.discard(10)
        self.assertEqual(self.set1, self.set0)
        n = len(self.set0)
        self.set0.discard(10000)    
        self.assertEqual(n, len(self.set0))

    def test_contains(self):
        self.assertEqual(10 in self.set1, 10 in self.set0)
        self.assertEqual(1 in self.set1, 1 in self.set0)

    def test_clear(self):
        self.set1.clear()
        self.assertEqual(len(self.set1), 0)
        
    def test_iter(self):
        self.assertEqual(sorted(self.set1), sorted(self.set0))
        
    def test_add(self):
        n = len(self.set1)
        self.set1.add(5)
        self.assertEqual(len(self.set1), n+1)
        self.assertTrue(5 in self.set1)
        self.set1.add(10)
        self.assertEqual(len(self.set1), n+1)
    
    def test_add_unchecked(self):
        n = len(self.set1)
        self.set1.add_unchecked(5)
        self.assertEqual(len(self.set1), n+1)
        self.assertTrue(5 in self.set1)
    
    def test_ops(self):
        a = set([1,2,4])
        b = set([1,5,6])
        A = CollectionSet(a, createCollection=lambda: LinkedListCollection())
        B = CollectionSet(b, createCollection=lambda: LinkedListCollection())
        C = CollectionSet([2,4], createCollection=lambda: LinkedListCollection())
        self.assertEqual(tuple(sorted(a | b)), tuple(sorted(A | B)))
        self.assertEqual(tuple(sorted(a & b)), tuple(sorted(A & B)))
        self.assertEqual(tuple(sorted(a - b)), tuple(sorted(A - B)))
        self.assertEqual(tuple(sorted(a ^ b)), tuple(sorted(A ^ B)))
        self.assertTrue(C < A)
        self.assertTrue(C <= A)
        self.assertTrue(A > C)
        self.assertTrue(A|B == B|A)
        self.assertTrue(C.isdisjoint(B))
        self.assertFalse(A|B != B|A)

    def test_repr(self):
        self.assertEqual(list(sorted(set(self.data))), list(sorted(eval(repr(self.set1)))))
        
class Test_IntSet(unittest.TestCase):
    def setUp(self):
        self.data = [10, 60, 20, 30, 30, 40, 50]
        self.set0 = set(self.data)
        self.set1 = IntSet(self.data) 
        
    def test_init(self):
        self.assertEqual(self.set1, self.set0)

    def test_len(self):
        self.assertEqual(len(self.set1), len(self.set0))

    def test_remove(self):
        self.set0.remove(10)
        self.set1.remove(10)
        self.assertEqual(self.set1, self.set0)
        self.assertRaises(KeyError, self.set0.remove, 1000)
        
    def test_discard(self):
        self.set0.discard(10)
        self.set1.discard(10)
        self.assertEqual(self.set1, self.set0)
        n = len(self.set0)
        self.set0.discard(10000)    
        self.assertEqual(n, len(self.set0))
    def test_contains(self):
        self.assertEqual(10 in self.set1, 10 in self.set0)
        self.assertEqual(1 in self.set1, 1 in self.set0)

    def test_clear(self):
        self.set1.clear()
        self.assertEqual(len(self.set1), 0)

    def test_iter(self):
        self.assertEqual(sorted(self.set1), sorted(self.set0))

    def test_add(self):
        n = len(self.set1)
        self.set1.add(5)
        self.assertEqual(len(self.set1), n+1)
        self.assertTrue(5 in self.set1)
        self.set1.add(10)
        self.assertEqual(len(self.set1), n+1)
        
    def test_ops(self):
        a = set([1,2,4])
        b = set([1,5,6])
        A = IntSet(a)
        B = IntSet(b)
        C = IntSet([2,4])
        self.assertEqual(tuple(sorted(a | b)), tuple(sorted(A | B)))
        self.assertEqual(tuple(sorted(a & b)), tuple(sorted(A & B)))
        self.assertEqual(tuple(sorted(a - b)), tuple(sorted(A - B)))
        self.assertEqual(tuple(sorted(a ^ b)), tuple(sorted(A ^ B)))
        self.assertTrue(C < A)
        self.assertTrue(C <= A)
        self.assertTrue(A > C)
        self.assertTrue(A|B == B|A)
        self.assertTrue(C.isdisjoint(B))
        self.assertFalse(A|B != B|A)
        
    def test_capacity(self):
        self.assertEqual(self.set1.capacity, 61)
        self.set1.capacity = 100
        self.set1.add(99)
        self.assertEqual(self.set1.capacity, 100)
        self.assertTrue(99 in self.set1)
        self.set1.capacity = 10
        self.set1.add(9)
        self.assertEqual(self.set1.capacity, 10)
        self.assertTrue(9 in self.set1)
    
    def test_repr(self):
        self.assertEqual(list(sorted(set(self.data))), list(sorted(eval(repr(self.set1)))))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()