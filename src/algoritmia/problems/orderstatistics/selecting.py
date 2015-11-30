#coding: latin1
from algoritmia.problems.sorting import BasicInPlaceQuickSorter #[]select1
from abc import ABCMeta, abstractmethod

class ISelector(metaclass=ABCMeta): #[interface
    @abstractmethod
    def select(self, a: "IList<T>", k: "int") -> "T": pass #]interface

class QuickSelector(ISelector): #[select1
    _partition = BasicInPlaceQuickSorter._partition

    def _quickselect(self, a: "IList<T>", k:"int", p: "int", r: "int") -> "T":
        if r - p == 1:
            return a[p]
        else:
            q = self._partition(a, p, r)
            if k == q: return a[q]
            elif k < q: return self._quickselect(a, k, p, q)
            else: return self._quickselect(a, k, q+1, r)

    def select(self, a: "IList<T>", k: "int") -> "T":
        if not (0 <= k < len(a)): raise IndexError(repr(k))
        return self._quickselect(a, k, 0, len(a)) #]select1

class MedianOf5Selector(object): #[select2
    def __init__(self, threshold: "int"=10):
        self.threshold = threshold
           
    def _median_of_5(self, v: "IList<T>", i: "int") -> "T": # utiliza 6 comparaciones
        # Asignamos etiquetas a los 4 primeros
        a, b, c, d = v[i], v[i+1], v[i+2], v[i+3]
        # Nos aseguramos de que a<=b y c<=d
        if a > b: 
            a, b = b, a
        if c > d: 
            c, d = d, c
        
        # Descartamos el menor de los 4 (será a o c)
        # El mayor de a y c se guarda en c, si se intercambian, se intercambian tambien b y d
        # a queda libre
        if a > c:
            b, d = d, b  # se intercambian si a>c
            c = a        # en c se guarda a (a queda libre), si a>c
        
        # Sobreescribimos el descartado, a, con el quinto número
        a = v[i+4]
        
        # Nos aseguramos, otra vez, que a<=b 
        if a > b: 
            a, b = b, a
            
        # Descartamos, otra vez, el menor de los nuevos 4 (será a o c). 
        # De los tres que quedarán, el siguiente mínimo será la mediana   
        if a > c:
            # descartamos c
            # la mediana será el menor de a, b y d, dado que a<=b, será el menor de a y d
            return min(a,d)
        else:
            # descartamos a
            # la mediana será el menor de c, b y d, dado que c<=d, será el menor de c y b
            return min(c,b)
        
    def select(self, a: "IList<T>", k: "int"):  
        if not (0 <= k < len(a)): raise IndexError(repr(k))
        if len(a) <= self.threshold:
            return sorted(a)[k]
        else:
            m = [self._median_of_5(a, i) for i in range(0, len(a), 5) if len(a)-i >= 5]
            pivot = self.select(m, len(m)//2)
            lessthan, equal = 0, 0
            for v in a:
                if v < pivot: lessthan += 1
                elif v == pivot: equal += 1
            if k < lessthan:
                return self.select([v for v in a if v < pivot], k)
            elif k >= lessthan+equal:
                return self.select([v for v in a if v > pivot], k-lessthan-equal)
            else:
                return pivot #]select2