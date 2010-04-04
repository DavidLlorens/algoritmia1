#coding: latin1

#< full
from algoritmia.statespace import IForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator

wolf, goat, cabbage = "lobo", "cabra", "col"

class WolfGoatCabbageSpaceState(IForwardStateSpace):
    class State:
        def __init__(self, state: "State"=None):
            if state is None:
                self.shore = [set([wolf, goat, cabbage]), set()]
                self.boat = 0
                self.decision = None
                self.previous = None
            else:
                self.shore = [set(state.shore[0]), set(state.shore[1])]
                self.boat = state.boat
                self.decision = None
                self.previous = state

        def __hash__(self) -> "int":
            h = self.boat
            for item in self.shore[0]: h ^= hash(item)
            return h

        def __eq__(self, other: "object") -> "bool":
            return other != None and self.boat == other.boat and self.shore[0] == other.shore[0]
        
    def initial_states(self) -> "Iterable<State>":
        yield WolfGoatCabbageSpaceState.State()

    def is_final(self, s: "State") -> "bool":
        return s.boat == 1 and len(s.shore[s.boat]) == 3

    def decisions(self, s: "State") -> "Iterable<str>":
        for d in s.shore[s.boat]:
            unattended = s.shore[1 - s.boat]
            if d not in (wolf, goat) and wolf in unattended and goat in unattended:
                continue
            if d not in (goat, cabbage) and goat in unattended and cabbage in unattended:
                continue
            yield d
        yield ""

    def decide(self, s: "State", d: "str") -> "State":
        s_prime = WolfGoatCabbageSpaceState.State(s)
        s_prime.boat = 1 - s.boat
        if d != "": 
            s_prime.shore[s.boat].remove(d)
            s_prime.shore[s_prime.boat].add(d)
        s_prime.decision = d
        s_prime.previous = s
        return s_prime

    def undo(self, s: "State", d: "str") -> "State":
        return s.previous

class StateSet:
    def __init__(self):
        self.set = set()
        
    def add(self, s: "State"):
        self.set.add(s)
        
    def __contains__(self, s: "State") -> "bool":
        return s in self.set

class WolfGoatCabbageSolver:
    def __init__(self):
        self.solver = BacktrackingEnumerator(createSet=lambda space: StateSet(),
                                             createSolution=lambda space, i, d, f: d)
    
    def solve(self) -> "IList<str>":
        space = WolfGoatCabbageSpaceState()
        return next(self.solver.enumerate(space))
#> full