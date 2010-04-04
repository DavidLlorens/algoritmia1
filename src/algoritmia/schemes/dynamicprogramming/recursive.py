class RecursiveDynamicProgrammingSolver: #[recursive
    def solve(self, space: "IBackwardsStateSpace", semiring: "ISemiring<R>", 
              w:"State, Decision -> R") -> "R":
        def _solve(s: "State") -> "R":
            r = semiring.Sum(semiring.times(_solve(s_prime), w(s_prime, d)) \
                            for (s_prime, d) in ((space.undo(s, d), d) for d in space.incoming_decisions(s))) 
            if space.is_initial(s): r = semiring.plus(r, semiring.one)
            return r
        return semiring.Sum(_solve(f) for f in space.final_states()) #]recursive