#coding: latin1

#< full
from algoritmia.problems.closures import WarshallMatrixTransitiveClosureFinder2

M = [[ False, True,  False, True,  False, False],  #?[[?[¶[? #?F?¶? #?T?¶T?
     [ False, False, False, False, True,  False],  #?[?»[? #?F?»? #?T?»T?
     [ False, False, False, False, True,  True],   #?[?»[? #?F?»? #?T?»T?
     [ True,  True,  False, False, False, False],  #?[?»[? #?F?»? #?T?»T?
     [ False, False, False, True,  False, False],  #?[?»[? #?F?»? #?T?»T?
     [ False, False, False, False, False, True]]   #?[?»[? #?F?»? #?T?»T?

for row in WarshallMatrixTransitiveClosureFinder2().transitive_closure(M):
    for value in row: print('{!s:<5}'.format(value), end= " ")
    print()
#< full