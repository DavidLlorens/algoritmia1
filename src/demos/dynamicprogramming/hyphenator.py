#coding: latin1

#< full
from algoritmia.data.spanishhyphenation import HyphenationTable
from algoritmia.problems.textprocessing.hyphenation import Hyphenator

hyphenator = Hyphenator(HyphenationTable())
for word in 'ejemplo', 'supercalifragilísticoespialidoso', 'algorítmia',\
            'cárcel', 'no', 'pie', 'arriba', 'país', 'aislado', 'penséis',\
            'guión', 'tenía', 'disputa':
    print(hyphenator.hyphenate(word), end=' ')

#> full