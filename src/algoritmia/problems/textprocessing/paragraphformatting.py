#coding: latin1
from algoritmia.utils import infinity 

#< full
class ParagraphFormatter:
    def __init__(self, penaltyFunction: "int, int -> int"
                    =lambda c, L: (L-c)**3 if c <= L else infinity):
        self.p = penaltyFunction
        
    def penalty(self, w: "IList<str>", L: "int") -> "int":
        P = [0] * (len(w)+1)
        for j in range(1, len(w)+1):
            chars = len(w[j-1])
            P[j] = P[j-1] + self.p(chars,L)
            for i in range(j-2, -1, -1):
                chars += len(w[i])
                if chars+j-i-1 > L: break
                P[j] = min(P[j], P[i] + self.p(chars+j-i-1,L))
        return P[len(w)]
    #> full
    
    #< just
    def justify(self, w: "IList<str>", L: "int") -> "str":
        P = [0] * (len(w)+1)
        back = [None] * (len(w)+1)
        for j in range(1, len(w)+1):
            chars = len(w[j-1])
            P[j], back[j] = P[j-1] + self.p(chars,L), j-1
            for i in range(j-2, -1, -1):
                chars += len(w[i])
                if chars+j-i-1 > L: break
                P[j], back[j] = min((P[j],back[j]), (P[i] + self.p(chars+j-i-1,L), i))
        par = []
        j = len(w)
        while back[j] != None:
            par.append( w[back[j]:j] )
            j = back[j]
        par.reverse()
        fmt_lines = []
        for line in par:
            linechars = len(''.join(line))
            blanks = L-linechars
            if len(line) > 1: sep, extra =  blanks // (len(line)-1), blanks % (len(line)-1)
            else: sep, extra = 1, 0
            if extra:
                fmt_lines.append((' '*(sep+1)).join(line[:extra]) + \
                                 ' '*(sep+1)+(' '*sep).join(line[extra:])) 
            else:
                fmt_lines.append( (' '*sep).join(line[extra:]) )
        return '\n'.join(fmt_lines)
#> just