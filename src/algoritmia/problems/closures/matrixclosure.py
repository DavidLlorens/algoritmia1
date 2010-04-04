from algoritmia.problems.closures.interfaces import IMatrixTransitiveClosureFinder

class MatrixTransitiveClosureFinder(IMatrixTransitiveClosureFinder): #[direct #[]direct2
    def __init__(self, createMatrix: "Iterable<Iterable<bool>> -> square Matrix<bool>"
                 =lambda it: [[cell for cell in row] for row in it]):
        self.createMatrix = createMatrix  

    def _square_and_add(self, M: "square Matrix<bool>") -> "square Matrix<bool>":
        R = self.createMatrix(M)
        n = len(M) 
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    R[i][j] = R[i][j] or (M[i][k] and M[k][j])
        return R #]direct

    def transitive_closure(self, M: "square matrix<bool>") -> "square matrix<bool>": #[direct2
        R = M
        i = 1
        while i <= len(M):
            R = self._square_and_add(R)
            i *= 2
        return R #]direct2

class WarshallMatrixTransitiveClosureFinder(IMatrixTransitiveClosureFinder): #[warshall
    def __init__(self, createMatrix: "Iterable<Iterable<bool>> -> square Matrix<bool>"
                 =lambda it: [[cell for cell in row] for row in it]):
        self.createMatrix = createMatrix  

    def transitive_closure(self, M: "Iterable<Iterable<bool>>") -> "square Matrix<bool>":
        R = self.createMatrix(M)
        n = len(R)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    R[i][j] = R[i][j] or (R[i][k] and R[k][j])
        return R #]warshall

class WarshallMatrixTransitiveClosureFinder2(IMatrixTransitiveClosureFinder): #[warshall2
    def __init__(self, createMatrix: "Iterable<Iterable<bool>> -> square Matrix<bool>"
                 =lambda it: [[cell for cell in row] for row in it]):
        self.createMatrix = createMatrix  

    def transitive_closure(self, M: "square Matrix<bool>") -> "square Matrix<bool>":
        R = self.createMatrix(M)
        n = len(R) 
        for k in range(n):
            for i in range(n):
                if R[i][k]:
                    for j in range(n):
                        if R[k][j]: R[i][j] = True
        return R #]warshall2