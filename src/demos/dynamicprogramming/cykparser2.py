#coding: latin1

#< full
from algoritmia.problems.parsing.cykparser import CYKParser

P = {'S': [['A','B'], ['A','C']],  'C': [['S','B']], 'A': [['a']], 'B': [['b']]}
parser = CYKParser(P, 'S')
for x in ['aaabbb', 'aabbb', 'ab', 'aaaa']:
    belongs = parser.accepts(x)
    print('¿Pertenece {} a L(G)? {}.'.format(x, 'Si' if belongs else 'No'))
    if belongs: print('Árbol de análisis:', parser.parse_tree(x))
#> full