from algoritmia.problems.exactcover.dlx0 import DLX0
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class DLX(DLX0): #[dlx6
    def __init__(self, ones, selected=[]):
        super().__init__(ones, selected)

    def decisions(self, s):
        size, bestcol = self.n + 1, None
        for col in s.right():
            if col.S < size: size, bestcol = col.S, col
            if size == 1: break
        bestcol.cover()
        for cell_in_row in bestcol.down():
            yield cell_in_row
        bestcol.uncover()
    
    def decide(self, s, cell_in_row):
        s.selected.add(s.row_index[cell_in_row])
        for cell in cell_in_row.right(): cell.H.cover()
        return s

    def undo(self, s, cell_in_row):
        s.selected.remove(s.row_index[cell_in_row])
        for cell in cell_in_row.left(): cell.H.uncover()
        return s #]dlx6
    
class DLXSolver:
    def __init__(self):
        self.solver = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
        
    def solve(self, ones):
        space = DLX(ones)
        return(next(self.solver.enumerate(space)))
