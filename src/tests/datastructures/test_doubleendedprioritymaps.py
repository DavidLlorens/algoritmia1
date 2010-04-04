import unittest
from random import seed, shuffle
from algoritmia.datastructures.prioritymaps import FibonacciHeap, HeapMap, MaxHeapMap, MinHeapMap

class TestHeapMap(unittest.TestCase):
    def setUp(self):
        seed(0)
        self.l = [(chr(ord('a')+i), i) for i in range(26)]
        shuffle(self.l)
        self.minpd = HeapMap(opt=min, data=self.l)
        self.maxpd = HeapMap(opt=max, data=self.l)

    def test_opt_onNonEmptyPriorityDict_getsOptimumKey(self):
        self.assertEquals(self.minpd.opt(), 'a')
        self.assertEquals(self.maxpd.opt(), 'z')

    def test_opt_item_onNonEmptyPriorityDict_getsOptimumItem(self):
        self.assertEquals(self.minpd.opt_item(), ('a', 0))
        self.assertEquals(self.maxpd.opt_item(), ('z', 25))

    def test_opt_value_onNonEmptyPriorityDict_getsOptimumValue(self):
        self.assertEquals(self.minpd.opt_value(), 0)
        self.assertEquals(self.maxpd.opt_value(), 25)

    def test_extract_opt_onNonEmptyPriorityDict_extractsOptimumAndGetsKey(self):
        self.assertEquals(self.minpd.extract_opt(), 'a')
        self.assertEquals(self.minpd.opt(), 'b')
        self.assertEquals(self.maxpd.extract_opt(), 'z')
        self.assertEquals(self.maxpd.opt(), 'y')

    def test_extract_opt_onNonEmptyPriorityDict_extractsOptimumAndGetsItem(self):
        self.assertEquals(self.minpd.extract_opt_item(), ('a', 0))
        self.assertEquals(self.minpd.opt(), 'b')
        self.assertEquals(self.maxpd.extract_opt_item(), ('z', 25))
        self.assertEquals(self.maxpd.opt(), 'y')

    def test_contains_KeyInDict_returnsTrue(self):
        for i in range(26):
            self.assertTrue(chr(ord('a')+i) in self.minpd)
            self.assertTrue(chr(ord('a')+i) in self.maxpd)

    def test_contains_KeyNotInDict_returnsFalse(self):
        for c in 'A', '1':
            self.assertFalse(c in self.minpd)
            self.assertFalse(c in self.maxpd)

    def test_getItem_KeyInDict_returnsAssociateValue(self):
        for i in range(26):
            self.assertEquals(self.minpd[chr(ord('a')+i)], i)
            self.assertEquals(self.maxpd[chr(ord('a')+i)], i)

    def test_getItem_KeyNotInDict_raisesException(self):
        for c in 'A', '1':
            self.assertRaises(KeyError, self.minpd.__getitem__, c)
            self.assertRaises(KeyError, self.maxpd.__getitem__, c)

    def test_setItem_KeyNotInDict_createsNewItem(self):
        self.minpd['A'] = -1
        self.assertEquals(self.minpd['A'], -1)
        self.minpd['1'] = 100
        self.assertEquals(self.minpd['1'], 100)

    def test_setItem_KeyInDict_changesItem(self):
        self.minpd['a'] = -1
        self.assertEquals(self.minpd['a'], -1)
        self.minpd['z'] = 100
        self.assertEquals(self.minpd['z'], 100)

    def test_setItem_definingNewOpt_changesOpt(self):
        self.minpd['m'] = -1
        self.assertEquals(self.minpd.opt(), 'm')
        self.maxpd['m'] = 100
        self.assertEquals(self.maxpd.opt(), 'm')

    def test_delItem_existingKey_removesItem(self):
        del self.minpd['m']
        self.assertRaises(KeyError, self.minpd.__getitem__, 'm')
        del self.maxpd['m']
        self.assertRaises(KeyError, self.maxpd.__getitem__, 'm')

    def test_delItem_nonExistingKey_raisesException(self):
        self.assertRaises(KeyError, self.minpd.__delitem__, 'A')
        self.assertRaises(KeyError, self.maxpd.__delitem__, 'A')

    def test_keys_onPriorityDict_iteratesAllKeys(self):
        self.assertEquals(set(self.minpd.keys()), set((a for (a, b) in self.l)))
        self.assertEquals(set(self.maxpd.keys()), set((a for (a, b) in self.l)))

    def test_values_onPriorityDict_iteratesAllValues(self):
        self.assertEquals(set(self.minpd.values()), set((b for (a, b) in self.l)))
        self.assertEquals(set(self.maxpd.values()), set((b for (a, b) in self.l)))

    def test_items_onPriorityDict_iteratesAllItems(self):
        self.assertEquals(set(self.minpd.items()), set(self.l))
        self.assertEquals(set(self.maxpd.items()), set(self.l))

    def test_get_onExistingKey_returnsValue(self):
        self.assertEquals(self.minpd.get('a', 100), 0)
        self.assertEquals(self.maxpd.get('a', 100), 0)

    def test_get_onNonExistingKey_returnsDefaultValue(self):
        self.assertEquals(self.minpd.get('A', 100), 100)
        self.assertEquals(self.maxpd.get('A', 100), 100)

    def test_setdefault_onExistingKey_returnsValue(self):
        self.assertEquals(self.minpd.setdefault('a', 100), 0)
        self.assertEquals(self.maxpd.setdefault('a', 100), 0)

    def test_setdefault_onNonExistingKey_returnsNewValue(self):
        self.assertEquals(self.minpd.setdefault('A', 100), 100)
        self.assertEquals(self.maxpd.setdefault('A', 100), 100)

    def test_iter_onPriorityMap_returnsKeys(self):
        self.assertEquals(set(self.minpd), set((a for (a, b) in self.l)))
        self.assertEquals(set(self.maxpd), set((a for (a, b) in self.l)))

    def test_len_onPriorityMap_returnsSize(self):
        self.assertEquals(len(self.minpd), 26)
        self.assertEquals(len(self.maxpd), 26)

    def test_repr_onPriorityMap_shouldReturnEvaluableExpression(self):
        self.assertEqual(list(sorted(self.minpd)), list(sorted(eval(repr(self.minpd)))))
        self.assertEqual(list(sorted(self.maxpd)), list(sorted(eval(repr(self.maxpd)))))


class TestFibonacciHeap(unittest.TestCase):
    def setUp(self):
        seed(0)
        self.l = [(chr(ord('a')+i), i) for i in range(26)]
        shuffle(self.l)
        self.minpd = FibonacciHeap(opt=min, data=self.l)
        self.maxpd = FibonacciHeap(opt=max, data=self.l)

    def test_opt_onNonEmptyPriorityDict_getsOptimumKey(self):
        self.assertEquals(self.minpd.opt(), 'a')
        self.assertEquals(self.maxpd.opt(), 'z')

    def test_opt_item_onNonEmptyPriorityDict_getsOptimumItem(self):
        self.assertEquals(self.minpd.opt_item(), ('a', 0))
        self.assertEquals(self.maxpd.opt_item(), ('z', 25))

    def test_opt_value_onNonEmptyPriorityDict_getsOptimumValue(self):
        self.assertEquals(self.minpd.opt_value(), 0)
        self.assertEquals(self.maxpd.opt_value(), 25)

    def test_extract_opt_onNonEmptyPriorityDict_extractsOptimumAndGetsKey(self):
        self.assertEquals(self.minpd.extract_opt(), 'a')
        self.assertEquals(self.minpd.opt(), 'b')
        self.assertEquals(self.maxpd.extract_opt(), 'z')
        self.assertEquals(self.maxpd.opt(), 'y')

    def test_extract_opt_onNonEmptyPriorityDict_extractsOptimumAndGetsItem(self):
        self.assertEquals(self.minpd.extract_opt_item(), ('a', 0))
        self.assertEquals(self.minpd.opt(), 'b')
        self.assertEquals(self.maxpd.extract_opt_item(), ('z', 25))
        self.assertEquals(self.maxpd.opt(), 'y')

    def test_contains_KeyInDict_returnsTrue(self):
        for i in range(26):
            self.assertTrue(chr(ord('a')+i) in self.minpd)
            self.assertTrue(chr(ord('a')+i) in self.maxpd)

    def test_contains_KeyNotInDict_returnsFalse(self):
        for c in 'A', '1':
            self.assertFalse(c in self.minpd)
            self.assertFalse(c in self.maxpd)

    def test_getItem_KeyInDict_returnsAssociateValue(self):
        for i in range(26):
            self.assertEquals(self.minpd[chr(ord('a')+i)], i)
            self.assertEquals(self.maxpd[chr(ord('a')+i)], i)

    def test_getItem_KeyNotInDict_raisesException(self):
        for c in 'A', '1':
            self.assertRaises(KeyError, self.minpd.__getitem__, c)
            self.assertRaises(KeyError, self.maxpd.__getitem__, c)

    def test_setItem_KeyNotInDict_createsNewItem(self):
        self.minpd['A'] = -1
        self.assertEquals(self.minpd['A'], -1)
        self.minpd['1'] = 100
        self.assertEquals(self.minpd['1'], 100)

    def test_setItem_KeyInDict_changesItem(self):
        self.minpd['a'] = -1
        self.assertEquals(self.minpd['a'], -1)
        self.maxpd['z'] = 100
        self.assertEquals(self.maxpd['z'], 100)

    def test_setItem_KeyInDictButNotImproving_raisesException(self):
        self.assertRaises(ValueError, self.minpd.__setitem__, 'a', 100)
        self.assertRaises(ValueError, self.maxpd.__setitem__, 'a', -1)

    def test_setItem_definingNewOpt_changesOpt(self):
        self.minpd['m'] = -1
        self.assertEquals(self.minpd.opt(), 'm')
        self.maxpd['m'] = 100
        self.assertEquals(self.maxpd.opt(), 'm')

    def test_delItem_existingKey_removesItem(self):
        del self.minpd['m']
        self.assertRaises(KeyError, self.minpd.__getitem__, 'm')
        del self.maxpd['m']
        self.assertRaises(KeyError, self.maxpd.__getitem__, 'm')

    def test_delItem_nonExistingKey_raisesException(self):
        self.assertRaises(KeyError, self.minpd.__delitem__, 'A')
        self.assertRaises(KeyError, self.maxpd.__delitem__, 'A')

    def test_keys_onPriorityDict_iteratesAllKeys(self):
        self.assertEquals(set(self.minpd.keys()), set((a for (a, b) in self.l)))
        self.assertEquals(set(self.maxpd.keys()), set((a for (a, b) in self.l)))

    def test_values_onPriorityDict_iteratesAllValues(self):
        self.assertEquals(set(self.minpd.values()), set((b for (a, b) in self.l)))
        self.assertEquals(set(self.maxpd.values()), set((b for (a, b) in self.l)))

    def test_items_onPriorityDict_iteratesAllItems(self):
        self.assertEquals(set(self.minpd.items()), set(self.l))
        self.assertEquals(set(self.maxpd.items()), set(self.l))

    def test_get_onExistingKey_returnsValue(self):
        self.assertEquals(self.minpd.get('a', 100), 0)
        self.assertEquals(self.maxpd.get('a', 100), 0)

    def test_get_onNonExistingKey_returnsDefaultValue(self):
        self.assertEquals(self.minpd.get('A', 100), 100)
        self.assertEquals(self.maxpd.get('A', 100), 100)

    def test_setdefault_onExistingKey_returnsValue(self):
        self.assertEquals(self.minpd.setdefault('a', 100), 0)
        self.assertEquals(self.maxpd.setdefault('a', 100), 0)

    def test_setdefault_onNonExistingKey_returnsNewValue(self):
        self.assertEquals(self.minpd.setdefault('A', 100), 100)
        self.assertEquals(self.maxpd.setdefault('A', 100), 100)

    def test_iter_onPriorityMap_returnsKeys(self):
        self.assertEquals(set(self.minpd), set((a for (a, b) in self.l)))
        self.assertEquals(set(self.maxpd), set((a for (a, b) in self.l)))

    def test_len_onPriorityMap_returnsSize(self):
        self.assertEquals(len(self.minpd), 26)
        self.assertEquals(len(self.maxpd), 26)

    def test_repr_onPriorityMap_shouldReturnEvaluableExpression(self):
        self.assertEqual(list(sorted(self.minpd)), list(sorted(eval(repr(self.minpd)))))
        self.assertEqual(list(sorted(self.maxpd)), list(sorted(eval(repr(self.maxpd)))))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()