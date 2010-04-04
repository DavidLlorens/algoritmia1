#coding: latin1

class TextSegmenter: #[prob #[]seg
    def __init__(self, Pr: "IMap<str, Real>"):
        self.Pr = Pr
        
    def probability(self, t: "str") -> "Real":
        P = [1.0] + [None] * (len(t))
        for j in range(1,len(t)+1):
            P[j] = max(P[i] * self.Pr[t[i:j]] for i in range(j))
        return P[len(t)] #]prob
        
    def segment(self, t: "str") -> "str":#[seg
        P = [1.0] + [None] * (len(t))
        back = [None] * (len(t)+1)
        for j in range(1,len(t)+1):
            P[j], back[j] = max( (P[i] * self.Pr.get(t[i:j], 0.0), i) for i in range(j) )
        sentence = []
        j = len(t)
        while back[j] != None:
            sentence.append( t[back[j]:j] )
            j = back[j]
        sentence.reverse()
        return ' '.join(sentence) #]seg