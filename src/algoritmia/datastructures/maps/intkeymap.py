#coding: latin1
from algoritmia.datastructures.maps import IMap
from collections.abc import Sequence, Iterable, Sized

class IntKeyMap(IMap): #[intkey
    def __init__(self, data: "Iterable<(int, T)> or IMap<(int, T)>"=[], #?data?¶data? 
                       capacity: "int"=0): #?cap?»cap?
        if isinstance(data, IMap): data = tuple(data.items())
        elif not isinstance(data, Sequence): data = tuple(data)
        if data: capacity = max(capacity, max(k for (k, v) in data)+1)
        self._has_key, self._value = [False] * capacity, [None] * capacity
        for (k,v) in data: self._has_key[k], self._value[k] = True, v

    def get_capacity(self) -> "int":
        return len(self._has_key)

    def set_capacity(self, capacity: "int"):
        if capacity < len(self._has_key):
            self._has_key, self._value = self._has_key[:capacity], self._value[:capacity]
        elif capacity > len(self._has_key):
            newcells = capacity - len(self._has_key)
            self._has_key.extend([False] * newcells)
            self._value.extend([None] * newcells)

    capacity = property(get_capacity,set_capacity)

    def __getitem__(self, key: "int") -> "T":
        if not ((0 <= key < len(self._value)) and self._has_key[key]): raise KeyError(key)
        return self._value[key]

    def __setitem__(self, key: "int", value: "T") -> "T":
        if not (0 <= key < len(self._value)): raise KeyError(key)
        self._has_key[key], self._value[key] = True, value
        return value
        
    def __delitem__(self, key: "int"):
        if not (0 <= key < len(self._value)) or not self._has_key[key]: raise KeyError(key)
        self._has_key[key], self._value[key] = False, None

    def __contains__(self, key: "int") -> "bool":
        return (0 <= key < len(self._value)) and self._has_key[key]
        
    def __iter__(self) -> "Iterable<int>":
        for i in range(len(self._has_key)):
            if self._has_key[i]: yield i

    def __len__(self) -> "int":
        return sum(1 for k in self)

    def get(self, key: "K", default: "T") -> "T":
        if key in self: return self._value[key]
        return default

    def setdefault(self, key: "K", default: "T") -> "T":
        if key in self: return self._value[key]
        self[key] = default
        return default
    
    class ItemsView(Sized, Iterable):
        def __init__(self, this):
            self.this = this
            
        def __len__(self) -> "int":
            return len(self.this)

        def __iter__(self) -> "Iterable<(K, T)>":
            for i in range(len(self.this._has_key)):
                if self.this._has_key[i]: yield (i, self.this._value[i])

    class KeysView(ItemsView):
        def __iter__(self) -> "Iterable<K>":
            for item in super().__iter__(): yield item[0]

    class ValuesView(ItemsView):
        def __iter__(self) -> "Iterable<T>":
            for item in super().__iter__(): yield item[1]
    
    def keys(self) -> "Iterable<K> and Sized":
        return IntKeyMap.KeysView(self)

    def values(self) -> "Iterable<T> and Sized":
        return IntKeyMap.ValuesView(self)

    def items(self) -> "Iterable<(K, T)> and Sized":
        return IntKeyMap.ItemsView(self)

    def __repr__(self) -> "str":
        return '{}({!r})'.format(self.__class__.__name__, list(self.items())) #]intkey