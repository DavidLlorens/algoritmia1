#coding: latin1

#< full
from algoritmia.problems.matrix.optimalmatrixproduct import OptimalMatrixProduct

dim = [ (7,4), (4,3), (3,10), (10,7), (7,2), (2,8) ]
print('Producto entre escalares:', OptimalMatrixProduct().flops(dim))
#> full