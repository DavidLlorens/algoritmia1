from algoritmia.problems.fourier import IDiscreteFourierTransform
from cmath import exp, pi #[full

class DiscreteFourierTransform(IDiscreteFourierTransform):
    def __init__(self, N: "int"):
        self.n = N
        self.wn = exp(complex(0,2*pi)/N)
        
    def transform(self, x: "IList<complex>") -> "IList<complex>":
        return [sum(x[j] * self.wn**(-j*k) for j in range(self.n)) for k in range(self.n)] #]full
