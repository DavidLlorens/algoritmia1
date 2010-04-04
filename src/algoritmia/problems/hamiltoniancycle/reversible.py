#coding: latin1
from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.statespace import IReversibleForwardStateSpace

class HamiltonianCycleStateSpace(IReversibleForwardStateSpace):#[space
    class State:
        def __init__(self, v, pred=None):
            self.last_vertex = v
            self.pred = pred
            self.added = set() if pred == None else self.pred.added
            self.added.add(v)
            self.first_vertex = v if pred == None else self.pred.first_vertex

        def _path(self, p):
            if self.pred != None: p = self.pred._path(p)
            p.append(self.last_vertex)
            return p

        def __repr__(self):
            return repr(self._path([]) + [self.first_vertex])            

    def __init__(self, G):
        self.G = G

    def initial_states(self):
        yield HamiltonianCycleStateSpace.State(next(iter(self.G.V)))

    def is_final(self, s):
        return len(s.added) == len(self.G.V) and (s.last_vertex, s.first_vertex) in self.G.E

    def decisions(self, s):
        if len(s.added) < len(self.G.V):
            for v in self.G.succs(s.last_vertex):
                if v not in s.added:
                    yield v 

    def decide(self, s, v):
        return HamiltonianCycleStateSpace.State(v, s)

    def undo(self, s, v):
        s.added.remove(s.last_vertex)
        return s.pred 

class HamiltonianCycleSolver:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def solve(self, G):
        space = HamiltonianCycleStateSpace(G)
        return next(self.enumerator.enumerate(space))#]space