#coding: latin1

#< full
from algoritmia.problems.perfecthash.improved import PerfectHashFinder

words = ('break case continue default do else ' + #?('?¶('?
         'for goto if return struct switch while').split() #?'f?»'f?
h = PerfectHashFinder().find(words, 20)
print([(w, h(w)) for w in words])
#> full