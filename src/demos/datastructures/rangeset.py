#coding: latin1
from algoritmia.datastructures.misc import RangeSet #[full

r = RangeSet(10, 20)
print("Talla:", len(r))
print("¿Contiene a 5?", 5 in r, "¿Y a 12?", 12 in r)
print("Elementos:", end=" ") 
for e in r: print(e, end=" ") 
print()
print("Como lista (vía __iter__):", list(r))
print("Representación como cadena:", r)#]full 
