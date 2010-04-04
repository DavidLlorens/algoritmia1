#< act2
class ActivitiesSelector:
    def select(self, C: "ISet<(Real, Real)>") -> "ISet<(Real, Real)>":
        x = []
        t_prime = min(s for (s,t) in C)
        for (s, t) in sorted(C, key=lambda st: st[1]):
            if t_prime <= s:
                x.append( (s, t) )
                t_prime = t
        return x
#> act2
