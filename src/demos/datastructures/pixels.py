#coding: latin1

#< full
from algoritmia.datastructures.mergefindsets import NaiveMergeFindSet

bitmap = [[1, 0, 1, 0, 1, 1, 1], #?[[?[¶[?
          [1, 0, 1, 0, 0, 0, 0], #?[?»[?
          [1, 1, 1, 0, 1, 1, 0]] #?[?»[?    
n, m = len(bitmap), len(bitmap[0])
S = NaiveMergeFindSet(((i,j),) for i in range(n) for j in range(m) if bitmap[i][j])

for i in range(len(bitmap)):
    for j in range(len(bitmap[i])):
        if bitmap[i][j] == 1:
            if i > 0 and bitmap[i-1][j] == 1: S.merge( (i,j), (i-1,j) )      
            if j > 0 and bitmap[i][j-1] == 1: S.merge( (i,j), (i,j-1) )

print('pixel    parent\n---------------')
for pixel in sorted(S._parent): print(pixel, ' ', S._parent[pixel])
print('Conjuntos:', tuple(S))

#> full