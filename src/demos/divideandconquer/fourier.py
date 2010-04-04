#coding: latin1

#< full
from algoritmia.problems.fourier.discretefouriertransform import DiscreteFourierTransform
from algoritmia.problems.fourier.recursivefastfouriertransform import RecursiveFastFourierTransform
from math import cos, pi

N= 16
x = [ complex(0.7*cos(2*pi*i/float(N)) + 0.3*cos(2*pi*i*4/float(N))) for i in range(N) ]
dft = DiscreteFourierTransform(n).transform(x)
fft_transformer = RecursiveFastFourierTransform(N)
fft = fft_transformer.transform(x)
inv = fft_transformer.inverse_transform(fft)
for i in range(N):
    print('{:+.2f}{:+.2f}j {:+.1f}{:+.1f}j  {:+.1f}{:+.1f}j {:+.2f}{:+.2f}j'.format(
        x[i].real, x[i].imag, dft[i].real, dft[i].imag, 
        fft[i].real, fft[i].imag, inv[i].real, inv[i].imag))
#> full