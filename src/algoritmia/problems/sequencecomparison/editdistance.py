#coding: latin1

#< lev
class EditDistanceComputer:
    def distance(self, x: "IList<T>", y: "IList<T>") -> "int":
        D = [[None] * (1+len(y)) for _ in range(1+len(x))]
        D[0][0] = 0
        for i in range(1, len(x)+1): D[i][0] = D[i-1][0] + 1
        for j in range(1, len(y)+1):
            D[0][j] = D[0][j-1] + 1
            for i in range(1, len(x)+1):
                D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (x[i-1] != y[j-1]))
        return D[len(x)][len(y)]
#> lev

#< dist2
class SpaceSavingEditDistanceComputer:
    def distance(self, x: "IList<T>", y: "IList<T>") -> "int":
        current_row, previous_row = [None] * (1+len(x)), [None] * (1+len(x))
        current_row[0] = 0
        for i in range(1, len(x)+1): current_row[i] = current_row[i-1] + 1
        for j in range(1, len(y)+1):
            previous_row, current_row = current_row, previous_row
            current_row[0] = previous_row[0] + 1
            for i in range(1, len(x)+1):
                current_row[i] = min(current_row[i-1] + 1,
                                     previous_row[i] + 1,
                                     previous_row[i-1] + (x[i-1] != y[j-1]))
        return current_row[len(x)]
#> dist2