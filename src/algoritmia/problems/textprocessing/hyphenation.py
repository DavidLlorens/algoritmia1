#coding: latin1

#< full
class Hyphenator:
    def __init__(self, table: "HyphenationTable"):
        self.table = table

    def hyphenate(self, word: "str") -> "str":
        mark = '.'+word+'.'
        value = [0] * (len(word)+2)
        for i in range(len(mark)+1):
            for j in range(i+2, len(mark)+1):
                if j-i in self.table and mark[i:j] in self.table[j-i]:
                    for v in range(len(self.table[j-i][mark[i:j]])):
                        value[i-1+v] = max(value[i-1+v], self.table[j-i][mark[i:j]][v])
        return ''.join(mark[i]+('-' if value[i]%2==1 else '') for i in range(1,len(value)-1))
#> full