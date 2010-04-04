from algoritmia.problems.regularexpressions.compiler import RegularExpressionParser#[full

parser = RegularExpressionParser() 
for re in "a*", "(ab)*", "ab*", "a|b*", "(a|b)*", "ab*a|bbba*":
    print("{} -> {}".format(re, parser.parse(re)))#]full
    
