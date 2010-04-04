from abc import ABCMeta, abstractproperty, abstractmethod

class ISemiRing(metaclass=ABCMeta):#[full
    @abstractproperty
    def zero(self) -> "R": pass

    @abstractproperty
    def one(self) -> "R": pass
    
    @abstractmethod
    def plus(self, left: "R", right: "R") -> "R": pass

    @abstractmethod
    def times(self, left: "R", right: "R") -> "R": pass
    
    def Sum(self, items: "Iterable<R>") -> "R":
        result = self.zero
        for r in items: result = self.plus(result, r)
        return result#]full
    
class IIdempotentSemiRing(ISemiRing):#[idem
    def argSum(self, items: "Iterable<T>", fn: "T -> T", ifempty=None) -> "T":
        result = self.zero
        for item in items:
            r = fn(item) 
            result = self.plus(result, r)
            if result == r:
                arg = item
        try: 
            return arg
        except NameError:
            return ifempty#]idem
    