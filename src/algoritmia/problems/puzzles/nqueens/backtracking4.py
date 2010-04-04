from algoritmia.statespace import IReversibleForwardStateSpace
 
class NQueensStateSpace4(IReversibleForwardStateSpace): #[space
    class State:
        def __init__(self, N: "int", prev: "State"=None, row: "int"=None):
            self.N, self.prev, self.row= N, prev, row
            if prev == None:
                self.n = 0
                self.available_rows = set(range(N))
                self.diag = [True] * (2*N-1)
                self.gaid = [True] * (2*N-1)
            else:
                self.n = prev.n + 1
                self.available_rows = prev.available_rows
                self.diag = prev.diag
                self.gaid = prev.gaid
                col = self.n-1
                self.diag[col+row] = self.gaid[col-row+self.N-1] = False
                self.available_rows.remove(row)

        def remove_row(self, row: "int") -> "State":
            col = self.n-1
            self.available_rows.add(row)
            self.gaid[col-row+self.N-1] = self.diag[col+row] = True
    
        def cell_is_free(self, col: "int", row: "int") -> "bool":
            return self.diag[col+row] and self.gaid[col-row+self.N-1]
        
        def free_rows(self) -> "Iterable<int>":
            col = self.n
            for row in tuple(self.available_rows):
                if self.diag[col+row] and self.gaid[col-row+self.N-1]:
                    yield row

    def __init__(self, N: "int"):
        self.N = N

    def initial_states(self) -> "Iterable<State>":
        yield NQueensStateSpace4.State(self.N)

    def is_final(self, s: "State") -> "bool":
        return s.n == self.N

    def decisions(self, s: "State") -> "Iterable<int>":
        return s.free_rows()
    
    def decide(self, s: "State", d: "int") -> "State":
        return NQueensStateSpace4.State(self.N, s, d)

    def undo(self, s: "State", d: "int") -> "State":
        s.remove_row(d)
        return s.prev#]space

class NQueensEnumerator: #[enum
    def __init__(self, createList: "-> IList<int>"=list):
        self.createList = createList
        
    def enumerate(self, space: "NQueensStateSpace1") -> "Iterable<IList<int>>":
        def backtracking(state: "IList<int>") -> "Iterable<IList<int>>":
            if space.is_final(state): yield decisions
            for decision in space.decisions(state):
                decisions.append(decision)
                state = space.decide(state, decision)
                for result in backtracking(state): yield result
                decisions.pop()
                state = space.undo(state, decision)
        decisions = self.createList()
        for state in space.initial_states():
            for result in backtracking(state):
                yield result
    
    def first(self, space: "NQueensStateSpace1") -> "IList<int>":
        return next(self.enumerate(space), None)#]enum