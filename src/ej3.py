# For a detailed explanation read: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
def tridiagonalPreprocess(a,b,c,d):
  c[0] /= b[0]
  d[0] /= b[0]
  for i in range(0, len(d) - 1):
    c[i] /= b[i] - a[i-1]*c[i-1]
    d[i] = (d[i] - a[i-1]*d[i-1]) / (b[i] - a[i-1]*c[i-1])
  
  i = len(d) - 1
  d[i] = (d[i] - a[i-1]*d[i-1]) / (b[i] - a[i-1]*c[i-1])
    
def solveTridiagonal(a,b,c,d):
  tridiagonalPreprocess(a,b,c,d)
  n = len(d)
  result = [0]*n
  result[n-1] = d[n-1]
  for i in range(n - 2, -1, -1):
    result[i] = d[i] - c[i]*result[i+1]
  
  return result