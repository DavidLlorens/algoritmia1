from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.statespace import IReversibleForwardStateSpace

class Cell: #[dlx1
    def __init__(self, L, R, U, D):
        self.L, self.R = L, R
        self.U, self.D = U, D

    def iterate(self, dir):
        cell = self.__dict__[dir]
        while cell != self:
            yield cell
            cell = cell.__dict__[dir]

    def up(self): return self.iterate('U')
    def down(self): return self.iterate('D')
    def left(self): return self.iterate('L')
    def right(self): return self.iterate('R') #]dlx1

class One(Cell): #[dlx2
    def __init__(self, U=None, D=None, H=None):
        super().__init__(self, self, U, D)
        self.H = H

    def remove(self):
        self.D.U, self.U.D = self.U, self.D
        self.H.S -= 1

    def restore(self):
        self.D.U = self.U.D = self
        self.H.S += 1 #]dlx2

class Column(Cell): #[dlx3 #[]dlx5 
    def __init__(self, L=None, R=None, S=0):
        super().__init__(L, R, self, self)
        self.S = S

    def cover(self):
        self.R.L, self.L.R = self.L, self.R
        for row in self.down():
            for cell in row.right():
                cell.remove()

    def uncover(self):
        for row in self.up():
            for cell in row.left():
                cell.restore()
        self.R.L = self.L.R = self #]dlx3 

class DLX0(IReversibleForwardStateSpace): #[dlx4
    def __init__(self, ones, selected=[]):
        self.ones = ones
        self.selected = selected
        self.n, self.m = len(ones), 1+max(max(row) for row in ones)

    class State(Cell):
        def __init__(self, ones, selected, n, m):
            super().__init__(None, None, None, None)
            self.row_index = {}
            self.build_column_headers(m)
            for row in range(n):
                current_col = self
                first = None
                for col in range(m):
                    current_col = current_col.R
                    if col in ones[row]:
                        current_col.S += 1
                        one = One(H=current_col, U=current_col.U, D=current_col)
                        self.row_index[one] = row
                        if first == None:
                            first = one
                        else:
                            one.L, one.R = first.L, first
                            one.L.R = first.L = one
                        current_col.U = one.U.D = one
            self.selected = set(selected)

        def build_column_headers(self, m):
            ptr = self
            for _ in range(m):
                ptr.R = Column()
                ptr.R.L = ptr
                ptr = ptr.R
            ptr.R = self
            self.L = ptr

        def __iter__(self):
            return iter(sorted(self.selected))

        def __repr__(self):
            return repr(list(sorted(self.selected))) #]dlx4

    def initial_states(self): #[dlx5
        yield DLX0.State(self.ones, self.selected, self.n, self.m)

    def is_final(self, s):
        return s.R == s
    
    def decisions(self, s):
        size, bestcol = self.n + 1, None
        for col in s.right():
            if col.S < size: size, bestcol = col.S, col
            if size == 1: break
        for cell_in_row in bestcol.down():
            yield (bestcol, cell_in_row)

    def decide(self, s, col_and_cell_in_row):
        col, cell_in_row = col_and_cell_in_row
        col.cover()
        s.selected.add(s.row_index[cell_in_row])
        for cell in cell_in_row.right(): cell.H.cover()
        return s

    def undo(self, s, col_and_cell_in_row):
        col, cell_in_row = col_and_cell_in_row
        s.selected.remove(s.row_index[cell_in_row])
        for cell in cell_in_row.left(): cell.H.uncover()
        col.uncover()
        return s #]dlx5

class DLXSolver:#[solver
    def __init__(self):
        self.solver = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
        
    def solve(self, ones):
        space = DLX0(ones)
        return(next(self.solver.enumerate(space)))#]solver