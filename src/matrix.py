import numpy as np
from auxiliary import *

class Matrix:
  # @param data: list[list](float)
  # data is expected to be homogeneus shape
  def __init__(self, data):
    self.matrix = np.array(data, dtype=float)
    self.dim = np.shape(self.matrix)
    self.L = None
    self.U = None
  
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
    # sum offset to retrieve matrix's original index
    return np.argmax(np.abs(self.matrix[offset:,columnIndex])) + offset
  
  # @type tuple(int,int)
  # @return Matrix dimensions
  def shape(self):
    return self.dim
  
  # @type float
  # @return Value at position [row,column]
  def at(self, row, column):
    return self.matrix[row][column]
  
  # @type Matrix
  # @param partial: bool, defines if Gaussian Elimination uses partial pivoting
  # @param b: list(float), independent vector
  # @return Gaussian elimination matrix
  def gaussianElimination(self, b, partial=True):
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
          raise Exception(f"Matrix has no unique solution.")
        else:
          raise Exception(f"Value at position [{i},{i}] ended up being 0. No further steps without pivoting.")
      else:
        for j in range(i+1, self.dim[0]):
          multiplier = result.at(j,i) / result.at(i,i)
          result.substractRow(j, i, multiplier)
          resVector = vectorSubstract(resVector,j,i,multiplier)
          
    return [result,resVector]
  
  def __str__(self):
    return str(self.matrix)