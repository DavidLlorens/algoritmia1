#< act1
class ActivitiesSelector1:
    def select(self, C: "ISet<(Real, Real)>") -> "ISet<(Real, Real)>":
        x = []
        for (s, t) in sorted(C, key=lambda st: st[1]):
            if not any(s_prime <= s < t_prime or s_prime < t <= t_prime for (s_prime, t_prime) in x):
                x.append( (s, t) )
        return x
#> act1