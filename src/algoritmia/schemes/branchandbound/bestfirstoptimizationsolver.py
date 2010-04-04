from algoritmia.datastructures.priorityqueues.heap import MaxHeap
from algoritmia.datastructures.sets.dummyset import DummySet
from algoritmia.schemes.branchandbound.bestfirstsearcher import Decisions
from algoritmia.utils import infinity

class BestFirstOptimizationSolver: #[bfo
    def __init__(self, opt=min, worst=infinity, 
            createOpenQueue=lambda space: MaxHeap(),
            createVisitedSet=lambda space: DummySet()):
        self.opt = opt
        self.worst = worst
        self.createOpenQueue = createOpenQueue
        self.createVisitedSet = createVisitedSet

    def solve(self, space, f, priority=lambda s: 0, createSolution=lambda i, d, f: d):
        best_f, best_solution = self.worst, None
        open = self.createOpenSet(space)
        visited = self.createVisitedSet()
        
        def initialize():        
            for s in space.initial_states(): 
                open.add((priority(s), s, Decisions(), s))
                visited.add(s)

        def there_are_open_states():
            return len(open) > 0

        def try_to_update_the_best_solution():
            fs = f(s)
            if self.opt(fs, best_f) != best_f:
                best_f, best_solution = fs, createSolution(i, ds, s)
                
        while there_are_open_states():
            (_, i, ds, s) = self.open.extract_opt()
            if space.is_final(s):
                try_to_update_the_best_solution()
            for d in space.decisions(s):
                s_prime = space.decide(s, d)
                if s_prime not in visited:
                    open.add((priority(s_prime), s_prime, Decisions(ds, d), s))
                    visited.add(s_prime) 
        return best_f, best_solution#]bfo