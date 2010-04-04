#coding: latin1

#< full
from algoritmia.problems.sequencecomparison.lcs import LongestCommonSubsequence

x, y = "comparsa", "causarte"
print("Longitud de la LCS entre {} y {}: {}".format(x, y, LongestCommonSubsequence().length(x, y)))
#> full