#coding: latin1

#< show
from fractions import Fraction

def show_fractional_knapsack(x, v, w):
    print('Valor total: {}.'.format(sum(x[i]*v[i] for i in range(len(x)))), end= ' ')
    print('Carga total: {}.'.format(sum(x[i]*w[i] for i in range(len(x)))))
    print('Detalle: {}.'.format(', '.join('%s de producto de peso %s y valor %s' \
          % (x[i], w[i], v[i]) for i in range(len(x)) if x[i] > 0)))
#> show

#< suboptimal
def suboptimal_fractional_knapsack(w, v, W):
    W = Fraction(W)
    x = [0] * len(w)
    for i in range(len(w)):
        x[i] = min(1, W / w[i])
        W -= x[i] * w[i]
    return x
#> suboptimal

#< fk
def fractional_knapsack(w, v, W):
    W = Fraction(W)
    x = [0] * len(w)
    for i in reversed(sorted(range(len(w)), key=lambda i: v[i]/float(w[i]))):
        x[i] = min(1, W / w[i])
        W -= x[i] * w[i]
    return x
#> fk