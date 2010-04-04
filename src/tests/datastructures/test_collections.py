#coding: latin1

import unittest
from algoritmia.datastructures.collections import ListCollection, LinkedListCollection

class TestListCollection(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 3, 4, 1, 2, 3, 4]
        self.listcol = LinkedListCollection(self.a)
        
    def test_add_newItem_shouldContainIt(self):
        self.listcol.add(5)
        self.assertTrue(5 in self.listcol)

    def test_add_repeatedItems_shouldContainAllOfThem(self):
        self.assertEqual(len([i for i in self.listcol if i == 1]), 2)
        self.listcol.add(1)
        self.assertEqual(len([i for i in self.listcol if i == 1]), 3)

    def test_remove_existingItem_shouldContainItWhileThereAreCopies(self):
        self.listcol.remove(1)
        self.assertTrue(1 in self.listcol)
        self.listcol.remove(1)
        self.assertFalse(1 in self.listcol)
        
    def test_remove_nonExistingItem_shouldRaiseValueError(self):
        self.assertRaises(ValueError, self.listcol.remove, 10)
            
    def test_contains_existingItems_shouldReturnTrue(self):
        for i in range(1, 5):
            self.assertTrue(i in self.listcol)

    def test_contains_nonExistingItem_shouldReturnFalse(self):
        self.assertFalse(5 in self.listcol)

    def test_len_onNonEmptyList_shouldReturnLength(self):
        self.assertEqual(len(self.listcol), 8)
        self.assertEqual(len(ListCollection()), 0)

    def test_len_onEmptyCollection_shouldReturnZero(self):
        self.assertEqual(len(ListCollection()), 0)

    def test_clear_collection_shouldEmptyTheCollection(self):
        self.listcol.clear()
        self.assertEqual(len(self.listcol), 0)
            
    def test_iter_onCollection_shouldGetAllItsElements(self):
        a = list(self.listcol) # Llama a __iter__
        self.assertEqual(a, self.a)

    def test_iter_onEmptyCollection_yieldNothing(self):
        a = list(ListCollection())
        self.assertEqual(len(a), 0)
    
    def test_repr_onCollection_shouldReturnCodeToReconstructIt(self):
        self.assertEqual(tuple(eval(repr(self.listcol))), tuple(self.listcol))
            
class TestLinkedListCollection(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 3, 4, 1, 2, 3, 4]
        self.linkcol = ListCollection(self.a)
        
    def test_add_newItem_shouldContainIt(self):
        self.linkcol.add(5)
        self.assertTrue(5 in self.linkcol)

    def test_add_repeatedItems_shouldContainAllOfThem(self):
        self.assertEqual(len([i for i in self.linkcol if i == 1]), 2)
        self.linkcol.add(1)
        self.assertEqual(len([i for i in self.linkcol if i == 1]), 3)

    def test_remove_existingItem_shouldContainItWhileThereAreCopies(self):
        self.linkcol.remove(1)
        self.assertTrue(1 in self.linkcol)
        self.linkcol.remove(1)
        self.assertFalse(1 in self.linkcol)
        
    def test_remove_nonExistingItem_shouldRaiseValueError(self):
        self.assertRaises(ValueError, self.linkcol.remove, 10)
            
    def test_contains_existingItems_shouldReturnTrue(self):
        for i in range(1, 5):
            self.assertTrue(i in self.linkcol)

    def test_contains_nonExistingItem_shouldReturnFalse(self):
        self.assertFalse(5 in self.linkcol)

    def test_len_onNonEmptyList_shouldReturnLength(self):
        self.assertEqual(len(self.linkcol), 8)
        self.assertEqual(len(LinkedListCollection()), 0)

    def test_len_onEmptyCollection_shouldReturnZero(self):
        self.assertEqual(len(LinkedListCollection()), 0)

    def test_clear_collection_shouldEmptyTheCollection(self):
        self.linkcol.clear()
        self.assertEqual(len(self.linkcol), 0)
            
    def test_iter_onCollection_shouldGetAllItsElements(self):
        a = list(self.linkcol) # Llama a __iter__
        self.assertEqual(a, self.a)

    def test_iter_onEmptyCollection_yieldNothing(self):
        a = list(LinkedListCollection())
        self.assertEqual(len(a), 0)
    
    def test_repr_onCollection_shouldReturnCodeToReconstructIt(self):
        self.assertEqual(tuple(eval(repr(self.linkcol))), tuple(self.linkcol))
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()