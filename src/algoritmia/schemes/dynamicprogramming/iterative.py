from algoritmia.statespace import StateSpaceTopsorter
from algoritmia.semirings.interfaces import IIdempotentSemiRing

class IterativeDynamicProgrammingSolver: #[iterative
    def __init__(self, 
                 createMap: "IBackwardsStateSpace -> IMap<State, R>"=lambda space: dict(), 
                 createStateSpaceTopsorter: "IBackwardsSpaceState -> Iterable<State>" \
                    =lambda space: StateSpaceTopsorter()):
        self.createMap = createMap
        self.createStateSpaceTopsorter = StateSpaceTopsorter

    def solve(self, space: "IBackwardsStateSpace", semiring: "ISemiRing<R>", 
              w:"State, Decision -> R") -> "R":
        mem = self.createMap(space)
        topsorter = self.createStateSpaceTopsorter()
        for s in topsorter.topsorted(space):
            mem[s] = semiring.one if space.is_initial(s) else semiring.zero
            for (s_prime, d) in ((space.undo(s, d), d) for d in space.incoming_decisions(s)):
                mem[s] = semiring.plus(mem[s], semiring.times(mem[s_prime], w(s_prime, d)))
        return semiring.Sum(mem[f] for f in space.final_states()) #]iterative

class IterativeIdempotentDynamicProgrammingSolver(IterativeDynamicProgrammingSolver): #[idempotent
    def backpointers(self, space: "IBackwardsStateSpace", semiring: "ISemiRing<R>", 
            w: "State, Decision -> R") -> "Iterable<State, Decision>":
        assert isinstance(semiring, IIdempotentSemiRing)
        mem = self.createMap(space)
        topsorter = self.createStateSpaceTopsorter()
        for s in topsorter.topsorted(space):
            if space.is_initial(s):
                mem[s], back = (semiring.one, (s, None)) 
            else:
                mem[s], back = (semiring.zero, (None, None))
            for (s_prime, d) in ((space.undo(s, d), d) for d in space.incoming_decisions(s)):
                score = semiring.times(mem[s_prime], w(s_prime, d))
                if semiring.plus(mem[s], score) != mem[s]:
                    mem[s], back = score, (s_prime, d)
            yield (s, back)#]idempotent