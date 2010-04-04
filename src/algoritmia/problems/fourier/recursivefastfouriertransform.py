from algoritmia.problems.fourier import IDiscreteFourierTransform
from cmath import exp, pi

class RecursiveFastFourierTransform(IDiscreteFourierTransform): #[full
    def __init__(self, N: "int"):
        self.w = [0] * (N+1)
        i = 1
        while i <= N:
            self.w[i] = exp(complex(0,2*pi) / i)
            i *= 2

    def transform(self, x: "IList<complex>") -> "IList<complex>":
        n = len(x)
        if n == 1: return x
        even, odd = self.transform(x[::2]), self.transform(x[1::2])
        return [even[k%(n//2)] + self.w[n]**(-k)*odd[k%(n//2)] for k in range(n)] #]full
