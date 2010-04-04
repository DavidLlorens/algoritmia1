#coding: latin1

#< full
from algoritmia.data.spanishhyphenation import HyphenationTable
from algoritmia.problems.textprocessing.hyphenation import Hyphenator

hyphenator = Hyphenator(HyphenationTable())
for word in 'ejemplo', 'supercalifragil�sticoespialidoso', 'algor�tmia',\
            'c�rcel', 'no', 'pie', 'arriba', 'pa�s', 'aislado', 'pens�is',\
            'gui�n', 'ten�a', 'disputa':
    print(hyphenator.hyphenate(word), end=' ')

#> full