from algoritmia.semirings.interfaces import ISemiRing
from algoritmia.utils import infinity

class ValueWithDecisionAndBackPointer: #[back
    def __init__(self, value, decision, backpointer=None):
        self.value = value
        self.decision = decision
        self.backpointer = backpointer

    def __repr__(self):
        return "{} {}".format(self.decisions(), self.value)

    def decisions(self):
        d = []
        self._to_decision_list(d)
        d.reverse()
        return d

    def _to_decision_list(self, d):
        if self.backpointer != None:
            d.append(self.decision)
            self.backpointer._to_decision_list(d) #]back

class _MinTropicalBackPointerSemiRing(ISemiRing): #[back2
    _zero = ValueWithDecisionAndBackPointer(infinity, None)
    _one = ValueWithDecisionAndBackPointer(0, None)
    zero = property(lambda self: MinTropicalBackPointerSemiRing._zero)
    one = property(lambda self: MinTropicalBackPointerSemiRing._one)

    def plus(self, left, right): 
        return left if left.value <= right.value else right

    def times(self, left, right): 
        return ValueWithDecisionAndBackPointer(left.value+right.value, right.decision, left) 

MinTropicalBackPointerSemiRing = _MinTropicalBackPointerSemiRing()#]back2
