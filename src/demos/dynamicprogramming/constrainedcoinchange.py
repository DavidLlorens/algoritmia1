#coding: latin1

#< full
from algoritmia.problems.constrainedcoinchange.constrainedcoinchange import CoinChanger

Q = 24
v, w, m = [1, 2, 5, 10], [1, 1, 4, 6], [3, 1, 4, 1]
print("Peso al desglosar la cantidad {} con {}".format(Q, v), end=' ')
print("y limitación de monedas a {}: {}".format(m, CoinChanger(v, w, m).weight(Q)))
#> full