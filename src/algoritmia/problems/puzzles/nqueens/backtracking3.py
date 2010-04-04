from algoritmia.statespace import IReversibleForwardStateSpace

class NQueensStateSpace3(IReversibleForwardStateSpace): #[space
    class State:
        def __init__(self, N: "int", prev: "State"=None, row: "int"=None):
            self.N, self.prev, self.row= N, prev, row
            if prev == None:
                self.n = 0
                self.free_row = [True] * N 
                self.diag = [True] * (2*N-1)
                self.gaid = [True] * (2*N-1)
            else:
                self.n = prev.n + 1
                self.free_row = prev.free_row
                self.diag = prev.diag
                self.gaid = prev.gaid
                col = self.n-1
                self.free_row[row] = self.diag[col+row] = self.gaid[col-row+self.N-1] = False
                
        def remove_last(self) -> "State":
            col, row = self.n-1, self.row
            self.gaid[col-row+self.N-1] = self.diag[col+row] = self.free_row[row] = True
    
        def cell_is_free(self, col: "int", row: "int") -> "bool":
            return self.free_row[row] and self.diag[col+row] and self.gaid[col-row+self.N-1]

        def __repr__(self):
            s = self
            aux = [None] * self.n
            while s.prev != None: aux[s.n-1], s = s.row, s.prev 
            return str(aux)

  
    def __init__(self, N: "int"):
        self.N = N

    def initial_states(self) -> "Iterable<State>":
        yield NQueensStateSpace3.State(self.N)

    def is_final(self, s: "State") -> "bool":
        return s.n == self.N

    def decisions(self, s: "State") -> "Iterable<State>":
        col = s.n
        for row in range(self.N):
            if s.cell_is_free(col, row):
                yield row

    def decide(self, s: "State", d: "int") -> "State":
        return NQueensStateSpace3.State(self.N, s, d)

    def undo(self, s: "State", d: "int") -> "State":
        s.remove_last()
        return s.prev#]space
    
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
        for state in space.initial_states():
            for result in backtracking(state):
                yield result
    
    def first(self, space: "NQueensStateSpace1") -> "IList<int>":
        return next(self.enumerate(space), None)#]enum
