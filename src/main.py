from matrix import *

mat = Matrix([[4,-2,2],[-2,1,1],[2,-1,2]])
v = [2,1,4]
b,mat = mat.gaussianElimination(v)
print(b,mat)