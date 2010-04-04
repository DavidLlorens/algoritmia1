from algoritmia.statespace import IForwardStateSpace

class NQueensStateSpace1(IForwardStateSpace): #[full
    def __init__(self, N: "int"):
        self.n = N

    def initial_states(self) -> "Iterable<IList<int>>": 
        yield []

    def is_final(self, s: "IList<int>") -> "bool":
        return len(s) == self.n

    def decisions(self, s: "IList<int>") -> "Iterable<IList<int>>":
        for row in range(self.n):
            if row not in s and all(len(s)-j != abs(row-s[j]) for j in range(len(s))):
                yield row

    def decide(self, s: "IList<int>", d: "int") -> "IList<int>":
        return s + [d]
    
class NQueensEnumerator: 
    def __init__(self, createList: "-> IList<int>"=list):
        self.createList = createList
        
    def enumerate(self, space: "NQueensStateSpace1") -> "Iterable<IList<int>>":
        def backtracking(state: "IList<int>") -> "Iterable<IList<int>>":
            if space.is_final(state): 
                yield state
            for decision in space.decisions(state):
                decisions.append(decision)
                successor = space.decide(state, decision)
                for result in backtracking(successor): 
                    yield result
                decisions.pop()
        decisions = self.createList()
        initial = next(space.initial_states(), None)
        if initial != None:
            for result in backtracking(initial):
                yield result
    
    def first(self, space: "NQueensStateSpace1", initial: "IList<int>"=None)\
            -> "IList<int>":
        return next(self.enumerate(space, initial), None)
    #]full