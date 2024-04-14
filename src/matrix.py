import numpy as np
from auxiliary import *

class Matrix:
  # @param data: list[list](float)
  # data is expected to be homogeneus shape
  def __init__(self, data):
    self.matrix = np.array(data, dtype=float)
    self.dim = [len(self.matrix),len(self.matrix[0])]
    self.n = len(self.matrix)
    self.m = len(self.matrix)
  
  # @type void
  # @param rowIndex: int
  # @param scalar: float
  def multiplyRow(self, rowIndex, scalar):
    self.matrix[rowIndex] *= scalar

  # @type void
  # @param rowIndex: int
  # @param substractRowIndex: int
  # @param scalar: float
  def substractRow(self, rowIndex, substractRowIndex, scalar):
    self.matrix[rowIndex] -= self.matrix[substractRowIndex]*scalar

  # @type void
  # @param rowIndexA: int
  # @param rowIndexB: int
  def swapRows(self, rowIndexA, rowIndexB):
    self.matrix[[rowIndexA,rowIndexB]] = self.matrix[[rowIndexB,rowIndexA]]
    
  # @type void
  # @param rowIndexA: int
  # @param rowIndexB: int
  def swapCols(self, colIndexA, colIndexB):
    self.matrix[:,[colIndexA,colIndexB]] = self.matrix[:,[colIndexB,colIndexA]]

  # @type int 
  # @param columnIndex: int
  # @param offset: int
  # @return Row index greater or equal than offset with highest absolute value in specific column
  def biggestInColumnFrom(self, columnIndex, offset):
    # start from offset to avoid incorrect swaps
    return max(range(offset,len(self.matrix[:,columnIndex])), key=lambda x : abs(self.matrix[:,columnIndex][x]))
  
  # @type float
  # @return Value at position [row,column]
  def at(self, row, column):
    return self.matrix[row][column]
  
  # @type float
  # @param value: float, new value
  # @return Value at position [row,column]
  def setVal(self, row, column, value):
    self.matrix[row][column] = value
  
  # @type bool
  # @return Matrix equality
  def equal(self, data):
    result = True
    for i in range(0, self.n - 1):
      for j in range(0, self.m - 1):
        result = result or self.at(i,j) == data[i][j]
    return result
  
  # @type [Matrix, list(float)]
  # @param b: list(float), independent vector
  # @param partial: bool, defines if Gaussian Elimination uses partial pivoting
  # @param e: float, near-zero division warning margin
  # @return Gaussian elimination matrix
  def gaussianElimination(self, b, partial=True, e=0.1):
    result = Matrix(self.matrix)
    resVector = np.array(b, dtype = float)
    for i in range(0,self.dim[0]-1):
      # Pivot handling
      if partial:
        maxValue = result.biggestInColumnFrom(i,i)
        result.swapRows(i,maxValue)
        resVector = vectorSwap(resVector,i,maxValue)
        
      # Error handling
      if(result.at(i,i) == 0):
        if partial: 
          raise Exception("Matrix has no unique solution.")
        else: 
          raise Exception(f"Value at position [{i},{i}] ended up being 0. No further steps without pivoting.")
      else:
        for j in range(i+1, self.dim[0]):
          # Dividing near zero warning
          if(abs(result.at(i,i)) < e): 
            raise Warning(f"Dividing with values near zero at [{i},{i}].")
          
          multiplier = result.at(j,i) / result.at(i,i)
          result.substractRow(j, i, multiplier)
          resVector = vectorSubstract(resVector,j,i,multiplier)
          
    return [result,resVector]
  
  # @type ndarray
  # @param b: list(float), independent vector
  # @param partial: bool, defines if Gaussian Elimination uses partial pivoting
  # @return System solution
  def solve(self, b, partial=True):
    GEmatrix, GEb = self.gaussianElimination(b, partial=partial)
    n = len(b)
    res = [0]*n
    for i in range(n - 1, -1, -1):
      sum = 0
      for j in range(i + 1, n):
        sum += GEmatrix.at(i, j) * res[j]
      res[i] = (GEb[i] - sum) / GEmatrix.at(i, i)
    return res
  
  # @type bool
  # @return True if matrix is tridiagonal, False otherwise
  def isTridiagonal(self):
    if self.n != self.m: 
      return False
    for i in range(0, self.n):
      for j in range(0, self.n):
        if abs(i - j) > 1 and self.at(i,j) != 0:
          return False
        if abs(i - j) <= 1 and self.at(i,j) == 0:
          return False
    return True
  
  # @type [Matrix, list(float)]
  # @param d: list(float), independent vector
  # @return Thomas Algorithm preprocessed matrix and vector
  # For more info read: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
  def tridiagonalPreprocess(self, d):
    processedMatrix = self
    processedD = d
    
    # Set first value
    processedMatrix.setVal(0, 1, self.at(0,1) / self.at(0,0))
    processedD[0] = d[0] / self.at(0,0)
    
    # Set rest of values
    for i in range(1, self.n - 1):
      b_i = self.at(i,i)
      c_i = self.at(i,i+1)
      d_i = d[i]
      prev_c_i = processedMatrix.at(i-1,i)
      prev_d_i = processedD[i-1]
      a_i = self.at(i-1,i+1)
      # New values
      newC = c_i / (b_i - prev_c_i*a_i)
      newD = (d_i - prev_d_i*a_i) / (b_i - prev_c_i*a_i)
      # Set new values
      processedMatrix.setVal(i, i+1, newC)
      processedD[i] = newD
        
    return processedMatrix, processedD
    
  
  # @type ndarray
  # @param d: list(float), independent vector
  # @return System solution
  def solveTridiagonal(self, d):
    # Verify matrix is tridiagonal
    if not self.isTridiagonal():
      raise Exception("Matrix is not tridiagonal.")
    
    pMatrix, pD = self.tridiagonalPreprocess(d)
    result = [0]*self.n
    result[self.n - 1] = pD[self.n - 1]
    for i in range(self.n - 2, -1, -1):
      result[i] = pD[i] - pMatrix.at(i,i+1)*result[i+1]
    
    return result
    
  
  def __str__(self):
    return str(self.matrix)