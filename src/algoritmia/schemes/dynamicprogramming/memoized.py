class MemoizedRecursiveDynamicProgrammingSolver: #[memoization
    def __init__(self, 
                 createMap: "IForwardStateSpace -> IMap<State, R>"=lambda space: dict()):
        self.createMap = createMap

    def solve(self, space: "IBackwardsStateSpace", 
              semiring: "ISemiRing<R>", w:"State, Decision -> R") -> "R":
        def _solve(s: "State"):
            for d in space.incoming_decisions(s):
                s_prime = space.undo(s, d)
                if s_prime not in mem: _solve(s_prime)
            r = semiring.one if space.is_initial(s) else semiring.zero
            for (s_prime, d) in ((space.undo(s, d), d) for d in space.incoming_decisions(s)):
                r = semiring.plus(r, semiring.times(mem[s_prime], w(s_prime, d)))
            mem[s] = r
        mem = self.createMap(space)
        for f in space.final_states():
            if f not in mem: _solve(f)
        return semiring.Sum(mem[f] for f in space.final_states()) #]memoization
    
    def states_results_and_decisions(self, space: "IBackwardsStateSpace", 
                semiring: "ISemiRing<R>", w: "State, Decision -> R") -> "State, R, Decision":
        def _backpointers(s: "State") -> "Iterable<(State, Decision)>":
            for d in space.incoming_decisions(s):
                s_prime = space.undo(s, d)
                if s_prime not in mem: 
                    for state_and_decision in _backpointers(s_prime):
                        yield state_and_decision
            r = semiring.one if space.is_initial(s) else semiring.zero
            for (s_prime, d) in ((space.undo(s, d), d) for d in space.incoming_decisions(s)):
                s_prime = space.undo(s, d)
                r_prime = semiring.plus(r, semiring.times(mem[s_prime], w(s_prime, d))) 
                if r_prime != r:
                    r, decision = r_prime, d
            mem[s] = r
            try:
                yield (s, decision)
            except NameError:
                pass
        mem = self.createMap(space)
        for f in space.final_states():
            if f not in mem:
                for (s, d) in _backpointers(f):
                    yield (s, mem[s], d)
    
    def decisions(self, space: "IBackwardsStateSpace", 
                semiring: "ISemiRing<R>", w: "State, Decision -> R") -> "IList<Decision>":
        back = self.createMap(space)
        result = semiring.zero
        for (s, r, d) in self.states_results_and_decisions(space, semiring, w):
            if semiring.plus(result, r) == r: f = s
            back[s] = d
        ds = []
        s = f
        while s in back:
            ds.append(back[s])
            s = space.undo(s, back[s])
        ds.reverse()
        return ds