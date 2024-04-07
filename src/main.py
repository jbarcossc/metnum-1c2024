from matrix import *

mat = Matrix([[4,-2,2],[-2,1,3],[2,-2,2]])
v = [1,1,0]
mat, b = mat.gaussianElimination(v)