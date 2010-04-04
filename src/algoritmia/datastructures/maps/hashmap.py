from algoritmia.datastructures.maps.interfaces import IMap
from _abcoll import Sized, Iterable
from algoritmia.datastructures.lists.linkedlist import LinkedList

class HashMap(IMap): #[hashmap
    class KeyValue:
        __slots__ = ("key", "value")
        
        def __init__(self, key, value):
            self.key, self.value = key, value
        
        def __eq__(self, other: "KeyValue<K, T>") -> "bool":
            return self.key == other.key

    def __init__(self, data: "Iterable<K, T>"=[], capacity=16, 
                 createList: "-> IList<T>"=lambda: LinkedList()):
        self.createList = createList
        if isinstance(data, IMap): data = tuple(data.items())
        elif not isinstance(data, Sized): data = tuple(data)
        if len(data) > capacity: capacity = len(data)
        self._list = list([None] * capacity)
        self._length = 0
        for (k, v) in data: self[k] = v

    def __getitem__(self, key: "K") -> "T": 
        h = hash(key) % len(self._list)
        if self._list[h] != None: 
            for keyvalue in self._list[h]:
                if keyvalue.key == key:
                    return keyvalue.value
        raise KeyError("Key {} not found".format(key))

    def __setitem__(self, key: "K", value: "T") -> "T":
        h = hash(key) % len(self._list)
        if self._list[h] == None: self._list[h] = self.createList()
        for keyvalue in self._list[h]:
            if keyvalue.key == key:
                keyvalue .value = value
                return value
        self._list[h].append(HashMap.KeyValue(key, value))
        self._length += 1
        return value

    def __delitem__(self, key: "K"):
        h = hash(key) % len(self._list)
        found = False
        if self._list[h] != None:
            for i, keyvalue in enumerate(self._list[h]):
                if keyvalue.key == key:
                    found = True
                    break
        if found:
            del self._list[h][i]
            self._length -= 1
        else:
            raise KeyError("Key {} not found".format(key))
    
    def get(self, key: "K", default: "T"):
        try:
            return self[key]
        except KeyError:
            return default    

    def setdefault(self, key: "K", default: "T") -> "T": 
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default
    
    class ItemsView(Sized, Iterable):
        def __init__(self, this):
            self.this = this
            
        def __len__(self):
            return self.this._length

        def __iter__(self):
            for lst in self.this._list:
                if lst != None:
                    for keyvalue in lst:
                        yield (keyvalue.key, keyvalue.value)

    class KeysView(ItemsView):
        def __iter__(self):
            for item in super().__iter__(): yield item[0]

    class ValuesView(ItemsView):
        def __iter__(self):
            for item in super().__iter__(): yield item[1]
    
    def keys(self) -> "Iterable<K> and Sized":
        return HashMap.KeysView(self)

    def values(self) -> "Iterable<T> and Sized":
        return HashMap.ValuesView(self)

    def items(self) -> "Iterable<(K, T) and Sized>":  
        return HashMap.ItemsView(self)#]hashmap
        
    def __contains__(self, key):
        for lst in self._list:
            if lst != None:
                for keyvalue in lst:
                    if keyvalue.key == key: return True
        return False
    
    def __iter__(self):
        return iter(self.keys())
    
    def __len__(self):
        return self._length
    
    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self.items())) #]intkey
    
