#coding: latin1

#< full
from algoritmia.problems.textprocessing.paragraphformatting import ParagraphFormatter

L = 30
t = "ésta es la frase de ejemplo que contiene veintiocho palabras y usamos "+\
    "al ilustrar el resultado de un algoritmo de división en líneas "+\
    "justificadas y de anchura fija"
print('Penalización mínima para {!r} y {} columnas:'.format(t, L), end=' ')
print(ParagraphFormatter().penalty(t.split(), L))
#> full