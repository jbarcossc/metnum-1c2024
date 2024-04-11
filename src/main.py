from matrix import *

mat = Matrix([[4,-2,2],[-2,1,1],[2,2,2]])
v = [5,2,1]
mat, b = mat.gaussianElimination(v)
print(mat)