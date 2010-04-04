from algoritmia.statespace import IReversibleForwardStateSpace

class NQueensStateSpace2(IReversibleForwardStateSpace): #[space
    class State:
        def __init__(self, prev=None, row=None, n=0):
            self.prev, self.row, self.n = prev, row, n
            self._rows = [] if prev == None else prev._rows

        def to_list(self):
            s = self
            aux = [None] * self.n
            while s.prev != None: aux[s.n-1], s = s.row, s.prev
            return aux 

        def __repr__(self):
            return str(self.to_list())
                
    def __init__(self, N: "int"):
        self.n = N

    def initial_states(self):
        yield NQueensStateSpace2.State()

    def is_final(self, s: "State") -> "bool":
        return s.n == self.n

    def decisions(self, s: "IList<int>") -> "Iterable<IList<int>>":
        for row in range(self.n):
            if row not in s._rows and all(s.n-j != abs(row-s._rows[j]) for j in range(s.n)):
                yield row

    def decide(self, s: "State", d: "int") -> "State":
        s_prime = NQueensStateSpace2.State(s, d, s.n+1)
        s_prime._rows.append(d)
        return s_prime 

    def undo(self, s: "IList<int>", d: "int") -> "IList<int>":
        s._rows.pop()
        return s.prev #]space

class NQueensEnumerator: #[enum
    def __init__(self, createList: "-> IList<int>"=list):
        self.createList = createList
        
    def enumerate(self, space: "NQueensStateSpace1") -> "Iterable<IList<int>>":
        def backtracking(state: "IList<int>") -> "Iterable<IList<int>>":
            if space.is_final(state): 
                yield state
            for decision in space.decisions(state):
                decisions.append(decision)
                state = space.decide(state, decision)
                for result in backtracking(state): yield result
                decisions.pop()
                state = space.undo(state, decision)
        decisions = self.createList()
        initial = next(space.initial_states(), None)
        if initial != None:
            for result in backtracking(initial):
                yield result
    
    def first(self, space: "NQueensStateSpace1") -> "IList<int>":
        return next(self.enumerate(space), None)#]enum
