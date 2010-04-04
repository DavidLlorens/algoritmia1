from algoritmia.problems.puzzles.nqueens.backtracking4 import NQueensStateSpace4
from algoritmia.problems.puzzles.nqueens.backtracking4 import NQueensEnumerator
 
class NQueensStateSpace5(NQueensStateSpace4): #[full
    class State(NQueensStateSpace4.State):
        def free_rows(self) -> "Iterable<int>":
            col = self.n-1
            if col == 0:
                for row in range((self.N+1)//2):
                    yield row
            else:
                for row in tuple(self.available_rows):
                    if self.diag[col+row] and self.gaid[col-row+self.N-1]:
                        yield row
                      
    def initial_states(self):
        yield NQueensStateSpace5.State(self.N) 
        
class SpecialNQueensEnumerator(NQueensEnumerator):
    def enumerate(self, space: "NQueensStateSpace5") -> "Iterable<Tuple<int>>>":
        for solution in super().enumerate(space):
            yield solution
            if solution[0] < space.N//2:
                yield list(space.N-i-1 for i in solution) #]full
