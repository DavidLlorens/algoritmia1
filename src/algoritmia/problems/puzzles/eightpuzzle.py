#coding: latin1

#< full
from algoritmia.utils import infinity

class Board(object):
    def __init__(self, pieces):
        self.pieces = list(pieces)
        self.freepos = self._freepos() 
    
    def __getitem__(self, ij):
        i, j = ij
        return self.pieces[i*3+j]

    def __setitem__(self, ij, v):
        i, j = ij
        self.pieces[i*3+j] = v
        return v
    
    def _freepos(self):
        for i in range(3):
            for j in range(3):
                if self[i,j] == 9: return (i,j)

    def can_move(self, dir):
        (i, j) = self.freepos
        return (dir == 'l' and j > 0) or (dir == 'r' and j < 2) or \
               (dir == 'u' and i > 0) or (dir == 'd' and i < 2)
        
    def move(self, dir):
        (i, j) = self.freepos
        if dir == 'l':
            self[i,j],self[i,j-1] = self[i,j-1], self[i,j]
            self.freepos = (i, j-1)
        elif dir == 'r':
            self[i,j],self[i,j+1] = self[i,j+1], self[i,j]   
            self.freepos = (i, j+1)
        elif dir == 'u':
            self[i,j],self[i-1,j] = self[i-1,j], self[i,j]   
            self.freepos = (i-1, j)
        elif dir == 'd':
            self[i,j],self[i+1,j] = self[i+1,j], self[i,j]   
            self.freepos = (i+1, j)
    
    def __repr__(self):
        s = ['+-+-+-+\n']
        for i in range(3):
            for j in range(3):
                if self[i,j] == 9: s.append('| ')
                else: s.append('|%d' % self[i,j])
            s.append('|\n')
            s.append('+-+-+-+\n')
        return ''.join(s)
    
    def manhattan_distance(self):
        dst = 0
        for i in range(3):
            for j in range(3):
                ii, jj = self[i, j] / 3, self[i, j] % 3
                dst += abs(i-ii) + abs(j-jj)
        return dst

class EightPuzzle:
    class State:
        def __init__(self, s=None, d=None, board=None):
            self.previous = s
            self.direction = d
            self.board = Board(s.board.pieces) if s != None else board
            if d == None: 
                self.len = 0
            else:
                self.board.move(d)
                self.len = s.len + 1
                
        def _movements(self):
            if self.previous == None: return []
            seq = self.previous._movements()
            seq.append(self.direction)
            return seq
        
        def movements(self):
            return ''.join(reversed(self._movements()))
        
        def __hash__(self):
            h = 0
            for n in self.board.pieces: h = (h << 3) + (n-1)
            return h
        
        def __eq__(self, other):
            return other != None and self.board.pieces == other.board.pieces

        def __repr__(self):
            return repr((self.movements(), self.board.pieces))
    
    def __init__(self, board):
        self.board = board

    def initial_states(self):
        yield EightPuzzle.State(board=self.board)

    def is_final(self, s):
        k = 1
        for i in range(3):
            for j in range(3):
                if s.board[i,j] != k: return False
                k += 1
        return True

    def decisions(self, s):
        for dir in 'udlr':
            if s.board.can_move(dir): 
                yield dir

    def take_decision(self, s, d):
        return EightPuzzle.State(s, d)

    def destination_is_promising(self, s, d):
        return True
  
    def f(self, x):
       return (len(x), len(x))

    def opt(self, a, b):
       return min(a, b)

    def optimistic(self, s):
        return (s.len + s.board.manhattan_distance(), s.len)

    def suboptimal_solution(self):
        return None

    def pessimistic(self, s):
        return self.zero

    def solution(self, s):
        return s.movements()

    zero = (infinity, 0)
    one = -infinity

class NilssonEightPuzzle(EightPuzzle):
    def __init__(self, board):
        super().__init__(board)
        
    def optimistic(self, s):
        score = EightPuzzle.optimistic(self, s)[0]
        if s.board[1,1] != 9: score += 1
        if s.board[0,0] != 9 and s.board[0,0] != s.board[1,0]+1: score +=2
        if s.board[0,1] != 9 and s.board[0,1] != s.board[0,0]+1: score +=2
        if s.board[0,2] != 9 and s.board[0,2] != s.board[0,1]+1: score +=2
        if s.board[1,2] != 9 and s.board[1,2] != s.board[0,2]+1: score +=2
        if s.board[2,2] != 9 and s.board[2,2] != s.board[1,2]+1: score +=2
        if s.board[2,1] != 9 and s.board[2,1] != s.board[2,2]+1: score +=2
        if s.board[2,0] != 9 and s.board[2,0] != s.board[2,1]+1: score +=2
        if s.board[1,0] != 9 and s.board[1,0] != s.board[2,0]+1: score +=2
        
        return score

problem = NilssonEightPuzzle(Board([2, 4, 9, 1, 8, 5, 3, 6, 7]))
problem = EightPuzzle(Board([2, 8, 3, 1, 6, 4, 7, 9, 5]))
from algoritmia.datastructures.prioritymaps import MinHeapMap
from algoritmia.schemes.branchandbound import *

solver = BfoWithOptimisticPruningSolver(problem, lambda keyvalues: MinHeapMap(keyvalues), lambda initial_states: set(initial_states))

#solver = BranchAndBoundSolver(problem, lambda keyvalues: MinHeapMap(keyvalues), lambda initial_states: set(initial_states))
print(solver.solve())
#> full