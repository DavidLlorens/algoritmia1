from algoritmia.problems.regularexpressions.greedy import RegularExpressionMatcher#[full

regexes = ("a*", "(ab)*", "ab*", "a|b*", "(a|b)*", "(a|b)a", "ab*a|bbba*")
strings = ("aa", "abab", "bbb", "bba", "bbbaa", "aaaaa", "a", "")
firstw = max(len(r) for r in regexes)+1
otherw = max(len(r) for r in strings)+3 
print(" " * firstw, end="")
for s in strings:
    print("{{!r:{}}}".format(max(otherw, len(s)+1)).format(s), end="")
print()
for re in regexes:
    matcher = RegularExpressionMatcher(re)
    print("{{:{}}}".format(firstw).format(re), end="")
    for x in strings:
        m = matcher.match(x)
        print("{{!r:{}}}".format(max(otherw, len(s)+1)).format(m), end="")
    print()#]full
