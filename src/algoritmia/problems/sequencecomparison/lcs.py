#coding: latin1

#< full
class LongestCommonSubsequence:#[]lcs
    def length(self, x: "Ilist<T>", y: "Ilist<T>") -> "int":
        LCS = [[0] * (1+len(y)) for _ in range(1+len(x))]
        for j in range(1, len(y)+1):
            LCS[0][j] = 0
            for i in range(1, len(x)+1):
                if x[i-1] != y[j-1]: LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
                else:                LCS[i][j] = LCS[i-1][j-1] + 1
        return LCS[len(x)][len(y)]
#> full
#< lcs
    def subsequence(self, x: "IList<T>", y: "IList<T>") -> "IList<T>":
        LCS = [[0] * (1+len(y)) for _ in range(1+len(x))]
        back = [[None] * (1+len(y)) for _ in range(1+len(x))]
        for j in range(1, len(y)+1):
            LCS[0][j] = 0
            for i in range(1, len(x)+1):
                if x[i-1] == y[j-1]:              LCS[i][j], back[i][j] = LCS[i-1][j-1] + 1, (i-1, j-1)
                elif LCS[i][j-1] > LCS[i-1][j]:   LCS[i][j], back[i][j] = LCS[i][j-1], (i,j-1)      
                else:                             LCS[i][j], back[i][j] = LCS[i-1][j], (i-1,j)
        sequence = []
        (i, j) = (len(x), len(y))
        while back[i][j] != None:
            if back[i][j] == (i-1,j-1): sequence.append(x[i-1])
            (i, j) = back[i][j]
        return ''.join(reversed(sequence))
#> lcs