#coding: latin1

#< full
from algoritmia.problems.arithmetics.bigint import BigInt

a, b = BigInt(1345), BigInt(2965)
print('{} + {} = {} ({})'.format(a, b, a+b, 1345+2965))
print('{} * {} = {} ({})'.format(a, b, a*b, 1345*2965))
#> full