from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.problems.exactcover.dlx2 import DLX2

class NQueensDLXSolver:#[solver
    def __init__(self):
        self.solver = BacktrackingEnumerator()
    
    def solve(self, N: "int") -> "IList<int> or None":
        M, row_coding = self.nqueens_to_matrix(N)
        space = DLX2(M, set(range(2*N)))
        self.solver.createSolution = \
           lambda space, i, d, s: self.selected_nqueens(s.selected, row_coding)
        return next(self.solver.enumerate(space), None)
        
    def nqueens_to_matrix(self, N: "int") -> "matrix, IList<(int, int)>":
        M = []
        rows_coding = []
        for row in range(N):
            for col in range(N):
                M.append([row, N+col, 2*N + col-row+N-1, 2*N+2*N-1 + col+row])
                rows_coding.append((row,col))
        return M, rows_coding

    def selected_nqueens(self, selected: "IList<int>", row_coding: "IList<(int, int)>") \
            -> "IList<int> or None":
        if selected != None:
            return tuple(q[1] for q in sorted(row_coding[row] for row in selected))
        else:
            return None #]solver
