#coding: latin1
from algoritmia.datastructures.maps.hashmap import HashMap

import unittest
from algoritmia.datastructures.maps import IntKeyMap, LeftLeaningRedBlackTreeMap

class TestIntKeyMapping(unittest.TestCase):
    def setUp(self):
        self.a = IntKeyMap( ((i, i+1) for i in range(10)) )
        
    def test_ctor_withoutArgs_returnsEmptyMap(self):
        b = IntKeyMap()
        self.assertEqual(len(b), 0)

    def test_ctor_fromOtherMap_returnsIdenticalMap(self):
        b = IntKeyMap(self.a)
        self.assertEqual(len(self.a), len(b))
        for k in self.a:
            self.assertTrue(k in b)
            self.assertEquals(self.a[k], b[k])

    def test_ctor_fromIterableOfKeyValuePairs_returnsMapWithAllKeyValuePairs(self):
        b = IntKeyMap(self.a.items())
        self.assertEqual(len(self.a), len(b))
        self.assertEqual(len(self.a), len(b))
        for k in self.a:
            self.assertTrue(k in b)
            self.assertEquals(self.a[k], b[k])

    def test_ctor_withCapacity_returnsValidMap(self):
        b = IntKeyMap(capacity=10)
        b[9] = 1
        self.assertEqual(1, len(b))
        self.assertRaises(KeyError, b.__setitem__, 10, 0)        
        self.assertRaises(KeyError, b.__setitem__, -1, 0)
        
    def test_capacity(self):
        self.a.capacity = 100
        self.assertEqual(self.a[0], 1)
        self.assertEqual(self.a[9], 10)
        self.a[99] = 1
        self.assertEqual(self.a[99], 1)
        self.assertRaises(KeyError, self.a.__setitem__, 100, 0)        
        self.assertRaises(KeyError, self.a.__setitem__, -1, 0)
        self.a.capacity = 3
        self.assertRaises(KeyError, self.a.__setitem__, 3, 0)        
        self.assertRaises(KeyError, self.a.__setitem__, -1, 0)
        self.assertEqual(self.a[0], 1)
        self.a[2] = 2
        self.assertEqual(self.a[2], 2)
        
    def test_setitemAndGetitem_onMap_recoversData(self):
        a = IntKeyMap(capacity=100)
        for i in range(0, 100, 2):
            a[i] = "*" * i
        for i in range(0, 100, 2):
            self.assertEqual(a[i], "*" * i)

    def test_setitem_onIntKeyMapOutOfRange_raisesException(self):
        self.assertRaises(KeyError, self.a.__setitem__, 100, 0)        
        self.assertRaises(KeyError, self.a.__setitem__, -1, 0)

    def test_getitem_onIntKeyMapOutOfRange_raisesException(self):
        self.assertRaises(KeyError, self.a.__getitem__, 100)        
        self.assertRaises(KeyError, self.a.__getitem__, -1)

    def test_getitem_nonExistingKeyOnMap_raisesException(self):
        self.assertRaises(KeyError, self.a.__getitem__, 55)
        
    def test_delitem_onMap_shrinksMap(self):
        n = len(self.a)
        del self.a[0]
        self.assertEqual(len(self.a), n-1)

    def test_delitem_onMap_raisesException(self):
        del self.a[0]
        self.assertRaises(KeyError, self.a.__getitem__, 0)

    def test_delitem_nonExistingKey_raisesException(self):
        del self.a[0]
        self.assertRaises(KeyError, self.a.__delitem__, 0)
        
    def test_contains_existingKeys_returnsTrue(self):
        for i in range(10):
            self.assertTrue(i in self.a)

    def test_contains_nonExistingKeys_returnsFalse(self):
        self.assertFalse(10 in self.a)
        self.assertFalse(-1 in self.a)
        
    def test_iter_onIntKeyMap_returnsAllKeys(self):
        for i, k in enumerate(sorted(self.a)):
            self.assertEqual(i, k)
            
    def test_len_onIntKeyMap_returnSize(self):
        self.assertEqual(len(self.a), 10)

    def test_len_onEmptyIntKeyMap_returnZero(self):
        self.assertEqual(len(IntKeyMap()), 0)
        
    def test_repr_onIntKeyMap_returnsEvaluableString(self):
        self.assertEqual(dict(self.a), dict(eval(repr(self.a))))


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.a = HashMap( ((i, i+1) for i in range(10)) )
        
    def test_ctor(self):
        b = HashMap()
        self.assertEqual(len(b), 0)
        b = HashMap(self.a)
        self.assertEqual(len(self.a), len(b))
        b = HashMap(self.a.items())
        self.assertEqual(len(self.a), len(b))
        b = HashMap(capacity=10)
        b[9] = 1
        self.assertEqual(1, len(b))
        
    def test_set_and_getitem(self):
        a = HashMap(capacity=100)
        for i in range(0, 100, 2):
            a[i] = "*" * i
        for i in range(0, 100, 2):
            self.assertEqual(a[i], "*" * i)
        self.assertRaises(KeyError, self.a.__getitem__, 100)        
        self.assertRaises(KeyError, self.a.__getitem__, -1)
        self.assertRaises(KeyError, self.a.__getitem__, 55)
        
    def test_delitem(self):
        n = len(self.a)
        del self.a[0]
        self.assertEqual(len(self.a), n-1)
        self.assertRaises(KeyError, self.a.__getitem__, 0)
        self.assertRaises(KeyError, self.a.__delitem__, 0)
        
    def test_contains(self):
        for i in range(10):
            self.assertTrue(i in self.a)
        self.assertFalse(10 in self.a)
        self.assertFalse(-1 in self.a)
        
    def test_iter(self):
        for i, k in enumerate(self.a):
            self.assertEqual(i, k)
            
    def test_len(self):
        self.assertEqual(len(self.a), 10)
        self.assertEqual(len(IntKeyMap()), 0)
        
    def test_repr(self):
        self.assertEqual(dict(self.a), dict(eval(repr(self.a))))



class TestLeftLeaningRedBlackTree(unittest.TestCase):
    def setUp(self):
        self.t = LeftLeaningRedBlackTreeMap()
        self.things = dict([("a",1), ("b",10),("c",3),("d",2),("e",11),("f",2),("g",0)])
        for k, v in self.things.items(): 
            self.t[k] = v
        self.assertEqual(list(self.t), list(sorted(self.things)))
    
    def test_len(self):
        self.assertEqual(len(self.t), 7)
        t = LeftLeaningRedBlackTreeMap()
        self.assertEqual(len(t), 0)
        
    def test_getitem(self):
        for k, v in self.things.items():
            self.assertEqual(self.t[k], v)
        self.assertRaises(KeyError, self.t.__getitem__, "xx")

    def test_delitem(self):
        x = list(self.things.items())
        del self.t[x[0][0]]
        self.assertEqual(len(self.t), 6)
        del self.t[x[1][0]]
        self.assertEqual(len(self.t), 5)
        self.assertRaises(KeyError, self.t.__getitem__, x[0][0])
        self.assertRaises(KeyError, self.t.__getitem__, x[1][0])
        for k, v in x[2:]: 
            self.assertEqual(self.t[k], v)
            
    def test_keys(self):
        self.assertEqual(list(self.t.keys()), list(sorted(self.things)))

    def test_items(self):
        self.assertEqual(list(self.t.items()), list(sorted(self.things.items())))

    def test_values(self):
        self.assertEqual(sorted(list(self.t.values())), list(sorted(self.things.values())))
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()