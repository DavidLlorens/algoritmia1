#coding: latin1

from algoritmia.statespace import IReversibleForwardStateSpace #[conventional
from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.problems.exactcover.dlx0 import Column, DLX0, One, Cell
from algoritmia.problems.exactcover.dlx import DLX

class Column2(Column): #[dlx7
    def __init__(self, primary, L=None, R=None, S=0):
        super().__init__(L, R, S)
        self.primary = primary

class DLX2(DLX): #[]dlx8 #[]dlx9
    def __init__(self, ones, primary_columns, selected=[]):
        super().__init__(ones, selected)
        self.primary_columns = primary_columns

    class State(Cell):
        def __init__(self, ones, selected, n, m, primary_columns):
            super().__init__(None, None, None, None)
            self.row_index = {}
            self.build_column_headers(m, primary_columns)
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

        def build_column_headers(self, m, primary_columns):
            ptr = self
            for i in range(m):
                ptr.R = Column2(i in primary_columns)
                ptr.R.L = ptr
                ptr = ptr.R
            ptr.R = self
            self.L = ptr

    def initial_states(self):
        yield DLX2.State(self.ones, self.selected, self.n, self.m, self.primary_columns) #]dlx7

    def decisions(self, s): #[dlx8
        size, bestcol = self.n + 1, None
        for col in s.right():
            if col.primary and col.S < size: size, bestcol = col.S, col
            if size == 1: break
        bestcol.cover()
        for cell_in_row in bestcol.down():
            yield cell_in_row
        bestcol.uncover() #]dlx8

    def is_final(self, s): #[dlx9
        return all(col.primary==False for col in s.right()) #]dlx9