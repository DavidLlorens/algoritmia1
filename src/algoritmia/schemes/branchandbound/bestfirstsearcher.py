from algoritmia.datastructures.priorityqueues.heap import MaxHeap
from algoritmia.datastructures.sets.dummyset import DummySet

class Decisions:
    def __init__(self, prev=None, d=None):
        self.d, self.prev = d, prev
    
    def as_list(self):
        prev_list = [] if self.prev == None else self.prev._list()
        prev_list.append(self.d)
        return prev_list
        
class BestFirstSearcher: #[bfs2
    def __init__(self, createOpenQueue=lambda space: MaxHeap(),
            createVisitedSet=lambda space: DummySet()):
        self.createOpenQueue = createOpenQueue
        self.createVisitedSet = createVisitedSet

    def enumerate(self, space, priority=lambda s: 0, createSolution=lambda i, d, f: d):
        open = self.createOpenSet(space)
        visited = self.createVisitedSet()
        for s in space.initial_states(): 
            open.add((priority(s), s, Decisions(), s))
            visited.add(s)
        while len(open) > 0:
            (_, i, ds, s) = self.open.extract_opt()
            if space.is_final(s): 
                yield createSolution(i, ds, s)
            for d in space.decisions(s):
                s_prime = space.decide(s, d)
                if s_prime not in visited:
                    open.add((priority(s_prime), s_prime, Decisions(ds, d), s))
                    visited.add(s_prime) #]bfs2
