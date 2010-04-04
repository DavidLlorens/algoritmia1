from algoritmia.datastructures.maps import IMap
from algoritmia.datastructures.lists import LinkedList

class LinkedListMap(IMap):
    class KeyValue:
        __slots__ = ("key", "value")
        
        def __init__(self, key, value):
            self.key, self.value = key, value
        
        def __eq__(self, other: "KeyValue<K, T>") -> "bool":
            return self.key == other.key
        
    def __init__(self, data: "Iterable<(K, T)> or IMap<K, T>"=[]):
        if isinstance(data, IMap): data = tuple(data.items())
        self._linkedlist = LinkedList(data)
        
    def _get_keyvalue_by_key(self, key: "K") -> "KeyValue<K, T>":
        for item in self._linkedlist:
            if item.key == key:
                return item
        return None
    
    def __contains__(self, key: "K") -> "bool":
        return self._get_keyvalue_by_key(key) != None
    
    def __getitem__(self, key: "K") -> "T":
        kv = self._get_keyvalue_by_key(key)
        if kv == None: raise KeyError("")
        return kv.value

    def __setitem__(self, key: "K", value: "T") -> "T":
        kv = self._get_keyvalue_by_key(key)
        if kv == None:
            kv = LinkedListMap.KeyValue(key, value)
            self._linkedlist.append(kv)
        else:
            kv.value = value
        return kv.value
    
    def __delitem__(self, key: "K", value: "T"):
        self._linkedlist.remove(LinkedListMap.KeyValue(key, value))
        
    def __len__(self) -> "int":
        return len(self._linkedlist)