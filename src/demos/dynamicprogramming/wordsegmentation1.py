#coding: latin1

#< full
from algoritmia.problems.textprocessing.wordsegmentation import TextSegmenter

class SparseDict(dict):
    def __missing__(self, key): return 0.0

Pr = SparseDict({'a': 0.05,       'aca': 0.01,      'acas': 0.01,   'ad': 0.01,  #?'a?¶'a? 
                 'asa': 0.02,     'as': 0.03,      'la': 0.12,      'laca': 0.05, #?'a?»'a? #?'l?»'l?
                 'lacas': 0.05,   'ca': 0.01,      'cadena': 0.06,  'cas': 0.05, #?'l?»'l? #?'c?»'c?
                 'casa': 0.08,    'casaca': 0.05,  'da': 0.05,      'de': 0.05, #?'c?»'c? #?'d?»'d?
                 'den': 0.02,     'e': 0.02,       'en': 0.11,      'na': 0.01, #?'d?»'d? #?'e?»'e? #?'n?»'n?
                 'nada': 0.07,    'saca': 0.05,    'sacad': 0.02}) #?'n?»'n? #?'s?»'s?
t = 'lacasacadenada'
print('Probabilidad de la mejor segmentación de {!r}: {:10.8f}.'.format(t, 
        TextSegmenter(Pr).probability(t)))
#> full