#coding: latin1

#< full
from algoritmia.problems.textprocessing.paragraphformatting import ParagraphFormatter

t = "�sta es la frase de ejemplo que contiene veintiocho palabras y usamos "+\
    "al ilustrar el resultado de un algoritmo de divisi�n en l�neas "+\
    "justificadas y de anchura fija"
for L in [60, 40, 30, 20]:
    print('Formateado con {} columnas. Penalizaci�n:'.format(L), end=' ')
    print(ParagraphFormatter().penalty(t.split(), L))
    print('-' * L)
    print(ParagraphFormatter().justify(t.split(), L))
    print()
#> full
