#coding: latin1

#< full
from algoritmia.problems.parsing.nfa import NFA

Q, q0, F = range(6), 0, [4,5]
preds = {0: [],
         1: [(0,'a'),(1,'a')], 
         2: [(0,'b'),(1,'b'),(4,'b')],
         3: [(1,'b'),(4,'a')],        
         4: [(2,'a')],         
         5: [(3,'a'),(4,'b'),(5,'a')]}
nfa = NFA(Q, q0, preds, F)
for x in ['aaaaba', 'aa', 'aaababaa', 'abaaaaab']:
    print('¿Pertenece {} a L(A)?: {}.'.format(x, 'Si' if nfa.accepts(x) else 'No'))
#> full