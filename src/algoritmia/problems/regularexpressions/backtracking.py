from algoritmia.problems.regularexpressions.compiler import RegularExpressionParser, ThompsonAutomatonBuilder
from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.statespace import IForwardStateSpace

class RegularExpressionMatchingStateSpace(IForwardStateSpace): #[space
    def __init__(self, nfa: "Nfa", x: "str"):
        self.x = x
        self.nfa = nfa
                    
    def initial_states(self) -> "Iterable<(int, int)>":
        yield (0, self.nfa.start)
    
    def is_final(self, s: "(int, int)") -> "bool":
        (i, q) = s
        return i == len(self.x) and q == self.nfa.end
    
    def decisions(self, s: "(int, int)") -> "Iterable<(int, int)>":
        (i, q) = s
        if i < len(self.x):
            for r in self.nfa.destinations(q, self.x[i]):
                yield (i+1, r)
        for r in self.nfa.destinations(q, None):
            yield (i, r)
            
    def decide(self, s: "(int, int)", d: "(int, int)"):
        return d#]space

class RegularExpressionMatcher:#[match
    def __init__(self, expression: "str"):
        t = RegularExpressionParser().parse(expression)
        self.nfa = ThompsonAutomatonBuilder().build(t)
    
    def match(self, x: "str") -> "bool":
        space = RegularExpressionMatchingStateSpace(self.nfa, x)
        return BacktrackingEnumerator().first(space) != None #]match

        