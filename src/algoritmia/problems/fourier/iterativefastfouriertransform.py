from algoritmia.problems.fourier import IDiscreteFourierTransform
from cmath import exp, pi

class IterativeFastFourierTransform(IDiscreteFourierTransform): #[full
    def __init__(self, N: "int"):
        self.n = N
        self.w = [0] * (N+1)
        i = 1
        while i <= N:
            self.w[i] = exp(complex(0,2*pi) / i)
            i *= 2
        rev = 0
        self.bitrev= [0] * N
        for i in range(N-1): 
            mask = N//2
            self.bitrev[i] = rev
            while rev >= mask: 
                rev -= mask 
                mask >>= 1 
            rev += mask 
        self.bitrev[N-1] = N-1

    def transform(self, x: "IList<complex>") -> "IList<complex>":
        X = [ x[self.bitrev[k]] for k in range(self.n) ]
        m = 2
        while m <= self.n:
            for j in range(0, self.n, m):
                for k in range(m//2):
                    w = self.w[m]**(-k)
                    X[j+k], X[j+k+m//2] = X[j+k] + w * X[j+k+m//2], X[j+k] - w * X[j+k+m//2]
            m <<= 1
        return X #]full
