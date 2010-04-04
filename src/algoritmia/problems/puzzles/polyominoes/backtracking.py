#coding: latin1
from algoritmia.statespace import IReversibleForwardStateSpace #[s1
from algoritmia.schemes.backtracking import BacktrackingEnumerator

class PolyominoesStateSpace(IReversibleForwardStateSpace): #[]s2 #[]s3
    class State:
        def __init__(self, board):
            self.board = [list(row) for row in board.split('\n')]
            self.freecells = sum(cell == '.' for row in board for cell in row)
            self.i = 0

        def __repr__(self):
            return '\n'.join([''.join(row) for row in self.board])

    def __init__(self, board, polyominoes):
        self.board = board
        self.pieces = polyominoes

    def initial_states(self):
        yield PolyominoesStateSpace.State(self.board)

    def is_final(self, s):
        return s.freecells == 0 and s.i == len(self.pieces) #]s1

    def decisions(self, s): #[s2
        if s.i < len(self.pieces):
            symbol, polyominoes = self.pieces[s.i]
            for polyomino in polyominoes:
                for y in range(len(s.board)):
                    for x in range(len(s.board[y])):
                        if all(0<=j+y<len(s.board) and 0<=i+x<len(s.board[j+y]) and\
                               s.board[j+y][i+x] == '.' for (i,j) in polyomino):
                            yield (symbol, polyomino, x, y) #]s2

    def destination_is_promising(self, s, symbol_piece_x_and_y): #[s3
        (symbol, piece, x, y) = symbol_piece_x_and_y
        return all(0<=j+y<len(s.board) and 0<=i+x<len(s.board[j+y]) and\
                   s.board[j+y][i+x] == '.' for (i,j) in piece)
            
    def decide(self, s, symbol_piece_x_and_y):
        (symbol, piece, x, y) = symbol_piece_x_and_y
        for (i,j) in piece: s.board[j+y][i+x] = symbol
        s.freecells -= len(piece)
        s.i += 1
        return s
            
    def undo(self, s, symbol_piece_x_and_y):
        (symbol, piece, x, y) = symbol_piece_x_and_y
        s.i -= 1
        s.freecells += len(piece)
        for (i,j) in piece: s.board[j+y][i+x] = '.'
        return s 

class PolyominoesSolver:
    def __init__(self, ):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def solve(self, board, tetrominos):
        space = PolyominoesStateSpace(board, tetrominos)
        return next(self.enumerator.enumerate(space))
#] s3

