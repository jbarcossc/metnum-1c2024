from matrix import *

mat = Matrix([[1,2.5,2.5],[0.5,2,3.5],[1.5,1.5,3]])
b = [6,6,6]

a,b,c = mat.getDiagonals()

print(a)
print(b)
print(c)