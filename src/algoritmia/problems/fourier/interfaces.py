from abc import ABCMeta, abstractmethod

class IDiscreteFourierTransform(metaclass=ABCMeta): #[full
    @abstractmethod
    def transform(self, x: "IList<complex>") -> "IList<complex>": pass
    
    def inverse_transform(self, x: "IList<complex>") -> "IList<complex>":
        X = self.transform(x)
        N = len(x)
        for i in range(N): X[i] /= N
        return X #]full