#coding: latin1
from algoritmia.datastructures.maps.interfaces import IMap
from collections.abc import Callable

class WeightingFunction(IMap, Callable): #[weighting
    def __init__(self, data: "Iterable<((T, T), K)> or IMap<(T, T), K>" =[], #?data?¶data?
                       symmetrical: "bool"=False, 
                       createMap: "Iterable<((T, T), K)> -> IMap<(T, T), K>"
                            =lambda keyvalues: dict(keyvalues)): #?symm?»symm?
        self.createMap = createMap
        self._map = self.createMap(data)
        self.symmetrical = symmetrical
        if symmetrical:
            for (u, v) in self._map.keys():
                if (v, u) in self._map:
                    if self._map[u, v] != self._map[v, u]:
                        raise ValueError("{!r} is different from {!r}".format((u,v), (v,u)))
                    if v != u: del self._map[v, u]

    def __contains__(self, key: "(T, T)") -> "bool":
        return key in self._map

    def __delitem__(self, key: "(T, T)"):
        del self._map[key]

    def __setitem__(self, key: "(T, T)", value: "K") -> "K":
        self._map[key] = value
        return value
    
    def get(self, key: "(T, T)", default: "K") -> "K":
        return self._map.get(key, default)

    def setdefault(self, key: "(T, T)", default: "K") -> "K":
        return self._map.setdefault(key, default)

    def keys(self) -> "Iterable<(T, T)>":
        return self._map.keys()

    def values(self) -> "Iterable<K>":
        return self._map.values()

    def items(self) -> "Iterable<K>":
        return self._map.items()

    def __getitem__(self, key: "(T, T)") -> "K":
        return self._map[key]
    
    def __iter__(self) -> "Iterable<(T, T)>":
        return iter(self._map)
    
    def __len__(self) -> "int":
        return len(self._map)
    
    def __call__(self, u: "T or (T, T)", v: "T or None"=None) -> "K":
        if v == None: u, v = u
        if (u,v) in self._map: return self._map[u,v]
        elif self.symmetrical: return self._map[v,u]
        raise KeyError(repr((u,v))) #]weighting