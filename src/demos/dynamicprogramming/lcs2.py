#coding: latin1

#< full
from algoritmia.problems.sequencecomparison.lcs import LongestCommonSubsequence

x, y = "comparsa", "causarte"
print("Subsecuencia com�n m�s larga entre {} y {}: {}".format(x, y, LongestCommonSubsequence().subsequence(x, y)))
#> full