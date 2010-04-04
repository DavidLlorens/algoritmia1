#coding: latin1
import unittest
from algoritmia.datastructures.lists import LinkedList, ArrayList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.seq = list(list(range(100))*2)
        self.ll = LinkedList(self.seq)
        
    def test_len_onLinkedList_shouldReturnNumberOfItems(self):
        self.assertEqual(len(self.seq), len(self.ll))

    def test_len_onEmptyLinkedList_shouldReturnZero(self):
        self.assertEqual(len(LinkedList()), 0)

    def test_append_newItem_shouldEnlargeIt(self):
        self.seq.append(1000)
        self.ll.append(1000)
        self.assertEqual(len(self.seq), len(self.ll))
    
    def test_append_newItem_shouldPlaceItInLastPos(self):
        self.seq.append(1000)
        self.ll.append(1000)
        self.assertEqual(self.seq[len(self.seq)-1], self.ll[len(self.ll)-1])
        self.assertEqual(self.seq[-1], self.ll[-1])
    
    def test_insert_itemAtZeroIndex_shouldEnlargeIt(self):
        self.seq[:0] = [1000]
        self.ll.insert(0, 1000)
        self.assertEqual(len(self.seq), len(self.ll))

    def test_insert_itemAtZeroIndex_shouldPlaceItInFirstPos(self):
        self.seq[:0] = [1000]
        self.ll.insert(0, 1000)
        self.assertEqual(self.seq[0], self.ll[0])

    def test_pop_onList_shouldShrinkIt(self):
        self.seq.pop()
        self.ll.pop()
        self.assertEqual(list(self.ll), self.seq)

    def test_pop_onList_shouldShrinkReturnLastItem(self):
        x = self.seq.pop()
        y = self.ll.pop()
        self.assertEqual(x, y)

    def test_pop_onEmptyList_shouldRaiseException(self):
        ll = LinkedList()
        self.assertRaises(IndexError, ll.pop)
        
    def test_del_firstElementOfList_shouldShrinkIt(self):
        del self.seq[0]
        del self.ll[0]
        self.assertEqual(list(self.ll), self.seq)

    def test_del_firstElementOfEmptyList_shouldShrinkIt(self):
        ll = LinkedList()
        self.assertRaises(IndexError, ll.__delitem__, 0)
        
    def test_remove_anItemFromList_shouldShrinkIt(self):
        self.ll.remove(10)
        self.seq.remove(10)
        self.assertEqual(list(self.ll), self.seq)

    def test_remove_severalItemsFromList_shouldShrinkIt(self):
        for i in range(5,20):
            self.ll.remove(i)
            self.seq.remove(i)
            self.assertEqual(list(self.ll), self.seq)

    def test_remove_repeatedItemFromList_shouldEliminateIt(self):
        for i in 10, 19:
            self.ll.remove(i)
            self.seq.remove(i)
            self.ll.remove(i)
            self.seq.remove(i)
        self.assertFalse(19 in self.ll)
        self.assertFalse(10 in self.ll)

    def test_remove_fromEmptyList_shouldRaiseException(self):
        ll = LinkedList()
        self.assertRaises(ValueError, ll.remove, 0)

    def test_remove_aNonExistingItem_shouldRaiseError(self):
        ll = LinkedList()
        self.assertRaises(ValueError, ll.remove, 0)
    
    def test_iter_shouldYieldAllItsContents(self):
        for i, v in enumerate(self.ll):
            self.assertEqual(v, self.seq[i])
            
    def test_contains_existingItem_shouldReturnTrue(self):
        self.assertTrue(0 in self.ll)
        self.assertTrue(99 in self.ll)

    def test_contains_nonExistingItem_shouldReturnFalse(self):
        self.assertFalse(1000 in self.ll)
        self.assertFalse(-1 in self.ll)
        
    def test_getitem_atValidIndex_shouldReturnItsValue(self):
        for i in range(99, -1, -1):
            self.assertEqual(self.ll[i], i)
        for i in range(100):
            self.assertEqual(self.ll[i], i)
        for i in range(len(self.ll)):
            self.assertEqual(self.seq[i], self.ll[i])
            
    def test_getitem_atValidNegativeIndex_shouldReturnItsValue(self):
        for i in range(-1, -100, -1):
            self.assertEqual(self.ll[i], 100+i)
            
        for i in range(len(self.ll)):
            self.assertEqual(self.seq[i], self.ll[i])
        self.assertEqual(self.ll[-len(self.ll)], self.ll[0])

    def test_getitem_atNegativeOrEquivalentPositiveIndex_shouldReturnSameValue(self):
        self.assertEqual(self.ll[-len(self.ll)], self.ll[0])

    def test_setitem_atAnyPosition_shouldSetValue(self):
        for i in range(100):
            self.ll[i]= -i
        for i in range(100):
            self.assertEqual(self.ll[i], -i)

    def test_delitem_atSeveralPlaces_shouldRemoveItems(self):
        for i in range(199, -1, -2):
            del self.ll[i]
        for i in range(100):
            if i % 2 == 1:
                self.assertFalse(i in self.ll)
            else:
                self.assertTrue(i in self.ll)

    def test_delitem_oneByOne_shouldReturnEmptyList(self):
        while len(self.ll)>0:
            del self.ll[0]
        self.assertRaises(IndexError, self.ll.__delitem__, 0)

    def test_delitem_onEmptyList_shouldRaiseException(self):
        self.assertRaises(IndexError, LinkedList().__delitem__, 0)
        
    def test_insert_atFirstPos_shouldCreateANewFirstElement(self):
        self.ll.insert(0, 1000)
        self.assertTrue(self.ll[0], 1000)
        
    def test_insert_atLastPos_shouldCreateANewLastElement(self):
        self.ll.insert(len(self.ll)-1, 2000)
        self.assertTrue(len(self.ll)-1, 2000)

    def test_insert_atMidPos_shouldCreateANewMidElement(self):
        self.ll.insert(len(self.ll)//2, 3000)
        self.assertTrue(len(self.ll)//2, 3000)

    def test_insert_atInvalidPos_shouldRaiseException(self):
        self.assertRaises(IndexError, self.ll.insert, 10000, 0)

    def test_insert_atNegativePos_shouldCreateANewItemThere(self):
        self.ll.insert(len(self.ll), -10)
        self.assertEquals(self.ll[len(self.ll)-1], -10)
        
    def test_len_onList_shouldReturnItsLength(self):
        self.assertEqual(len(self.ll), 200)

    def test_len_onEmptyList_shouldReturnZero(self):
        self.assertEqual(len(LinkedList()), 0)
        
    def test_repr_ofList_shouldCreateEvaluableString(self):
        self.assertEqual(list(self.ll), list(eval(repr(self.ll))))

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.seq = list(list(range(100))*2)
        self.al = ArrayList('i', self.seq)
        
    def test_len_onList_shouldReturnNumberOfItems(self):
        self.assertEqual(len(self.seq), len(self.al))

    def test_len_onEmptyList_shouldReturnZero(self):
        self.assertEqual(len(ArrayList('i')), 0)

    def test_append_newItem_shouldEnlargeIt(self):
        self.seq.append(1000)
        self.al.append(1000)
        self.assertEqual(len(self.seq), len(self.al))
    
    def test_append_newItem_shouldPlaceItInLastPos(self):
        self.seq.append(1000)
        self.al.append(1000)
        self.assertEqual(self.seq[len(self.seq)-1], self.al[len(self.al)-1])
        self.assertEqual(self.seq[-1], self.al[-1])
    
    def test_insert_itemAtZeroIndex_shouldEnlargeIt(self):
        self.seq[:0] = [1000]
        self.al.insert(0, 1000)
        self.assertEqual(len(self.seq), len(self.al))

    def test_insert_itemAtZeroIndex_shouldPlaceItInFirstPos(self):
        self.seq[:0] = [1000]
        self.al.insert(0, 1000)
        self.assertEqual(self.seq[0], self.al[0])

    def test_pop_onList_shouldShrinkIt(self):
        self.seq.pop()
        self.al.pop()
        self.assertEqual(list(self.al), self.seq)

    def test_pop_onList_shouldShrinkReturnLastItem(self):
        x = self.seq.pop()
        z = self.al.pop()
        self.assertEqual(x, z)

    def test_pop_onEmptyList_shouldRaiseException(self):
        al = ArrayList('i')
        self.assertRaises(IndexError, al.pop)
        
    def test_del_firstElementOfList_shouldShrinkIt(self):
        del self.seq[0]
        del self.al[0]
        self.assertEqual(list(self.al), self.seq)

    def test_del_firstElementOfEmptyList_shouldShrinkIt(self):
        al = ArrayList('i')
        self.assertRaises(IndexError, al.__delitem__, 0)
        
    def test_remove_anItemFromList_shouldShrinkIt(self):
        self.al.remove(10)
        self.seq.remove(10)
        self.assertEqual(list(self.al), self.seq)

    def test_remove_severalItemsFromList_shouldShrinkIt(self):
        for i in range(5,20):
            self.al.remove(i)
            self.seq.remove(i)
            self.assertEqual(list(self.al), self.seq)

    def test_remove_repeatedItemFromList_shouldEliminateIt(self):
        for i in 10, 19:
            self.al.remove(i)
            self.seq.remove(i)
            self.al.remove(i)
            self.seq.remove(i)
        self.assertFalse(19 in self.al)
        self.assertFalse(10 in self.al)

    def test_remove_fromEmptyList_shouldRaiseException(self):
        al = ArrayList('i')
        self.assertRaises(ValueError, al.remove, 0)

    def test_remove_aNonExistingItem_shouldRaiseError(self):
        al = ArrayList('i')
        self.assertRaises(ValueError, al.remove, 0)
    
    def test_iter_shouldYieldAllItsContents(self):
        for i, v in enumerate(self.al):
            self.assertEqual(v, self.seq[i])
            
    def test_contains_existingItem_shouldReturnTrue(self):
        self.assertTrue(0 in self.al)
        self.assertTrue(99 in self.al)

    def test_contains_nonExistingItem_shouldReturnFalse(self):
        self.assertFalse(1000 in self.al)
        self.assertFalse(-1 in self.al)
        
    def test_getitem_atValidIndex_shouldReturnItsValue(self):
        for i in range(99, -1, -1):
            self.assertEqual(self.al[i], i)
        for i in range(100):
            self.assertEqual(self.al[i], i)
        for i in range(len(self.al)):
            self.assertEqual(self.seq[i], self.al[i])
            
    def test_getitem_atValidNegativeIndex_shouldReturnItsValue(self):
        for i in range(-1, -100, -1):
            self.assertEqual(self.al[i], 100+i)
            
        for i in range(len(self.al)):
            self.assertEqual(self.seq[i], self.al[i])
        self.assertEqual(self.al[-len(self.al)], self.al[0])

    def test_getitem_atNegativeOrEquivalentPositiveIndex_shouldReturnSameValue(self):
        self.assertEqual(self.al[-len(self.al)], self.al[0])

    def test_setitem_atAnyPosition_shouldSetValue(self):
        for i in range(100):
            self.al[i]= -i
        for i in range(100):
            self.assertEqual(self.al[i], -i)

    def test_delitem_atSeveralPlaces_shouldRemoveItems(self):
        for i in range(199, -1, -2):
            del self.al[i]
        for i in range(100):
            if i % 2 == 1:
                self.assertFalse(i in self.al)
            else:
                self.assertTrue(i in self.al)

    def test_delitem_oneByOne_shouldReturnEmptyList(self):
        while len(self.al)>0:
            del self.al[0]
        self.assertRaises(IndexError, self.al.__delitem__, 0)

    def test_delitem_onEmptyList_shouldRaiseException(self):
        self.assertRaises(IndexError, ArrayList('i').__delitem__, 0)
        
    def test_insert_atFirstPos_shouldCreateANewFirstElement(self):
        self.al.insert(0, 1000)
        self.assertTrue(self.al[0], 1000)
        
    def test_insert_atLastPos_shouldCreateANewLastElement(self):
        self.al.insert(len(self.al)-1, 2000)
        self.assertTrue(len(self.al)-1, 2000)

    def test_insert_atMidPos_shouldCreateANewMidElement(self):
        self.al.insert(len(self.al)//2, 3000)
        self.assertTrue(len(self.al)//2, 3000)

    def test_insert_atInvalidPos_shouldRaiseException(self):
        self.assertRaises(IndexError, self.al.insert, 10000, 0)

    def test_insert_atNegativePos_shouldCreateANewItemThere(self):
        self.al.insert(len(self.al), -10)
        self.assertEquals(self.al[len(self.al)-1], -10)
        
    def test_len_onList_shouldReturnItsLength(self):
        self.assertEqual(len(self.al), 200)

    def test_repr_ofList_shouldCreateEvaluableString(self):
        self.assertEqual(list(self.al), list(eval(repr(self.al))))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_LinkedList']
    unittest.main()