#coding: latin1

#< full
from algoritmia.problems.arithmetics.bigint import BigIntBase

a, b = BigIntBase(1345), BigIntBase(2965)
print('{} + {} = {} ({})'.format(a, b, a+b, 1345+2965))
print('{} * {} = {} ({})'.format(a, b, a*b, 1345*2965))
#> full