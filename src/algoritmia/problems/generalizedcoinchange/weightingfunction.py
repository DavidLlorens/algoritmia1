from algoritmia.semirings.backpointer import ValueWithDecisionAndBackPointer

class Weight:#[weight
    def __init__(self, v, w):
        self.weight_table = dict((v[i], w[i]) for i in range(len(v)))
    def __call__(self, s, d):
        return self.weight_table[d]#]weight
    
class WeightAndDecision:#[weight2
    def __init__(self, v, w):
        self.weight_table = dict((v[i], w[i]) for i in range(len(v)))
    def __call__(self, s, d):
        return ValueWithDecisionAndBackPointer(self.weight_table[d], d)#]weight2