from algoritmia.problems.regularexpressions.compiler import RegularExpressionParser,\
    ThompsonAutomatonBuilder, DFA

parser = RegularExpressionParser() 
for re in "a*", "(ab)*", "ab*", "a|b*", "(a|b)*", "ab*a|bbba*":
    t = parser.parse(re)
    dfa = DFA.build_from_NFA(ThompsonAutomatonBuilder().build(t))
    print(dfa)
    
    
