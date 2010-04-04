from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.problems.exactcover.dlx import DLX

class PolyominoesSolver:#[dlx
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def solve(self, board, polyominoes):
        matrix, row_coding =self.polyominos_matrix_and_rows_coding(board, polyominoes)
        space = DLX(matrix)
        selected_rows = next(self.enumerator.enumerate(space))
        return self.solution_as_string(selected_rows, board, row_coding)
        
    def polyominos_matrix_and_rows_coding(self, board, polyominoes):
        polyomino_column = {}
        col = 0
        for polyomino in polyominoes:
            symbol, pieces = polyomino
            polyomino_column[symbol] = col
            col += 1
    
        board = [list(row) for row in board.split('\n')]
    
        xy_column = {}
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == '.':
                    xy_column[x,y] = col
                    col += 1
    
        matrix = []
        rows_coding = []
    
        for polyomino in polyominoes:
            symbol, pieces = polyomino
            for piece in pieces:
                for y in range(len(board)):
                    for x in range(len(board[y])):
                        if all(0<=x+i<len(board[y]) and 0<=y+j<len(board) and \
                               board[y+j][x+i] == '.' for (i,j) in piece):
                            rows_coding.append((symbol, piece, x, y))
                            matrix.append([polyomino_column[symbol]])
                            for (i,j) in piece:
                                matrix[-1].append(xy_column[x+i,y+j])
        return matrix, rows_coding

    def solution_as_string(self, selected_rows, board, rows_coding):
        board = [list(row) for row in board.split('\n')]
        for selected_row in selected_rows:
            symbol, piece, x, y = rows_coding[selected_row]
            for i, j in piece:
                board[y+j][x+i] = symbol
        return ('\n'.join(''.join(row) for row in board)).replace("*", " ") #]dlx