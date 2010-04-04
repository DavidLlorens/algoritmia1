from algoritmia.schemes.dynamicprogramming.iterative import IterativeDynamicProgrammingSolver
from algoritmia.statespace import StateSpaceTopsorter
from algoritmia.datastructures.prioritymaps.heapmap import HeapMap

class ForwardDynamicProgrammingSolver(IterativeDynamicProgrammingSolver): #[forward
    def __init__(self, 
                 createMap: "IBackwardsStateSpace -> IMap<State, R>"=lambda space: dict(), 
                 createStateSpaceTopsorter: "IBackwardsSpaceState -> Iterable<State>"\
                    =lambda space: StateSpaceTopsorter()):
        self.createMap = createMap
        self.createStateSpaceTopsorter = StateSpaceTopsorter

    def solve(self, space: "IBackwardsStateSpace", 
              semiring: "ISemiRing<R>", w:"State, Decision -> R") -> "R":
        mem = self.createMap(space)
        for s in space.initial_states(): mem[s] = semiring.one
        topsorter = self.createStateSpaceTopsorter()
        best = semiring.zero
        for s in topsorter.topsorted(space):
            if s not in mem: mem[s] = semiring.zero
            for (s_prime, d) in ((space.decide(s, d), d) for d in space.decisions(s)):
                if s_prime not in mem: mem[s_prime] = semiring.zero
                mem[s_prime] = semiring.plus(mem[s_prime], semiring.times(mem[s], w(s, d)))
            if space.is_final(s): best = semiring.plus(best, mem[s])
            del mem[s]
        return best #]forward
    
class ForwardWithPriorityQueueDynamicProgrammingSolver(ForwardDynamicProgrammingSolver): #[forwardpq
    def __init__(self, createPriorityMap: "-> IPriorityMap<State, R>"=HeapMap): 
        self.createPriorityMap = createPriorityMap
        
    def solve(self, space: "IBackwardsStateSpace", 
              semiring: "ISemiRing<R>", w:"State, Decision -> R") -> "R":
        mem = self.createPriorityMap((s, semiring.one) for s in space.initial_states())
        best_final_score = semiring.one
        while len(mem) > 0:
            (s, score) = mem.extract_opt_item()
            for d in space.decisions(s):
                s_prime = space.decide(s, d)
                if s_prime not in mem: 
                    mem[s_prime] = semiring.one
                mem[s_prime] = semiring.plus(mem[s_prime], semiring.times(score, w(s, d)))
            if space.is_final(s):
                best_final_score = semiring.plus(best_final_score, mem[s])
        return best_final_score #]forwardpq

class ForwardBellmanFordDynamicProgrammingSolver(ForwardDynamicProgrammingSolver): #[bellmanford
    def __init__(self, createMap=lambda space: dict(),
                       createStateSpaceTopsorter=lambda space: StateSpaceTopsorter()): 
        self.createMap = createMap
        
    def solve(self, space: "IBackwardsStateSpace", 
              semiring: "ISemiRing<R>", w:"State, Decision -> R") -> "R":
        current = self.createMap(space)
        previous = self.createMap(space)
        topsorter = self.createStateSpaceTopsorter()

        states = list(topsorter.topsorted(space))
        for s in states:
            current[s] = semiring.zero if space.is_initial(s) else semiring.one
        for _ in range(len(states)): 
            current, previous = previous, current
            for s in states:
                current[s] = semiring.zero if space.is_initial(s) else semiring.one
                for (s_prime, d) in ((space.decide(s, d), d) for d in space.decisions(s)):
                    current[s] = semiring.sum(current[s], semiring.times(previous[s_prime], w(s_prime, d)))
        return semiring.Sum(current[f] for f in space.final_states())#]bellmanford