#coding: latin1

#< full
from algoritmia.problems.textprocessing.paragraphformatting import ParagraphFormatter

L = 30
t = "�sta es la frase de ejemplo que contiene veintiocho palabras y usamos "+\
    "al ilustrar el resultado de un algoritmo de divisi�n en l�neas "+\
    "justificadas y de anchura fija"
print('Penalizaci�n m�nima para {!r} y {} columnas:'.format(t, L), end=' ')
print(ParagraphFormatter().penalty(t.split(), L))
#> full