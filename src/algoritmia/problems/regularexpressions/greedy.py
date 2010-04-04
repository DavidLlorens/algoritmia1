from algoritmia.problems.regularexpressions.compiler import RegularExpressionParser, ThompsonAutomatonBuilder,\
    DFA
from algoritmia.statespace import IForwardStateSpace
from algoritmia.schemes.greedy import GreedySolver

class RegularExpressionMatchingStateSpace(IForwardStateSpace): #[space
    def __init__(self, dfa: "Dfa<Q>", x: "str"):
        self.x = x
        self.dfa = dfa
                    
    def initial_states(self) -> "Iterable<(int, int)>":
        yield (0, self.dfa.s)
    
    def is_final(self, s: "(int, Q)") -> "bool":
        (i, q) = s
        return i == len(self.x) and q in self.dfa.F
    
    def decisions(self, s: "(int, Q)") -> "Iterable<(int, Q)>":
        (i, q) = s
        if i < len(self.x):
            q_prime = self.dfa.destination(q, self.x[i])
            if q_prime != None: 
                yield (i+1, q_prime)
            
    def decide(self, s: "(int, Q)", d: "(int, Q)"):
        return d#]space

class RegularExpressionMatcher:#[match
    def __init__(self, expression: "str"):
        t = RegularExpressionParser().parse(expression)
        self.dfa = DFA.build_from_NFA(ThompsonAutomatonBuilder().build(t))
    
    def match(self, x: "str") -> "bool":
        space = RegularExpressionMatchingStateSpace(self.dfa, x)
        return GreedySolver().solve(space) != None #]match

