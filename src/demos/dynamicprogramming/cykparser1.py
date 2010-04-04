#coding: latin1

#< full
from algoritmia.problems.parsing.cykparser import CYKParser

P = {'S': [('A','B'), ('A','C')],  'C': [('S','B')], 'A': [('a',)], 'B': [('b',)]}
for x in 'aaabbb', 'aabbb', 'ab', 'aaaa':
    print('¿Pertenece {} a L(G)? {}.'.format(x, 'Si' if CYKParser(P, 'S').accepts(x) else 'No'))
#> full