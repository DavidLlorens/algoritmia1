from algoritmia.utils import infinity
from algoritmia.datastructures.priorityqueues.heap import MaxHeap
from algoritmia.datastructures.sets.dummyset import DummySet
from algoritmia.schemes.branchandbound.bestfirstsearcher import Decisions

class BfoWithOptimisticPruningSolver: #[bfo
    def __init__(self, opt=min, worst=infinity, 
            createOpenQueue=lambda space: MaxHeap(),
            createVisitedSet=lambda space: DummySet()):
        self.opt = opt
        self.worst = worst
        self.createOpenQueue = createOpenQueue
        self.createVisitedSet = createVisitedSet

    def solve(self, space, f, optimistic_bound, 
              priority=lambda s: 0, createSolution=lambda i, d, f: d):
        best_f, best_solution = self.worst, None
        open = self.createOpenSet(space)
        visited = self.createVisitedSet()
        for s in space.initial_states(): 
            open.add((priority(s), s, Decisions(), s))
            visited.add(s)
        while len(open) > 0:
            (_, i, ds, s) = self.open.extract_opt()
            if space.is_final(s):
                fs = f(s)
                if self.opt(fs, best_f) != best_f:
                    best_f, best_solution = fs, createSolution(i, ds, s)
            for d in space.decisions(s):
                s_prime = space.decide(s, d)
                if s_prime not in visited:
                    open.add((priority(s_prime), s_prime, Decisions(ds, d), s))
                    visited.add(s_prime) 
        return best_f, best_solution#]bfo