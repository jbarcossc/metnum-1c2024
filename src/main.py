from matrix import *

mat = Matrix([[4,-2,0],[-2,1,1],[0,-1,2]])
v = [2,1,4]
#b,mat = mat.gaussianElimination(v)
mat, b = mat.tridiagonalPreprocess(v)
print(mat)
print(b)