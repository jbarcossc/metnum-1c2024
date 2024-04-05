import numpy as np

class Matrix:
  # @param {@data: list[list]}
  # data is expected to be homogeneus shape
  def __init__(self, data):
    self.matrix = np.array(data)
  
  # @type void
  # @param {@rowIndex: int, @scalar: float}
  def multiplyRow(self, rowIndex, scalar):
    self.matrix[rowIndex] *= scalar

  # @type void
  # @param {@rowIndex: int, @substractRowIndex: int, @scalar: float}
  def substractRow(self, rowIndex, substractRowIndex, scalar):
    self.matrix[rowIndex] -= self.matrix[substractRowIndex]*scalar

  # @type void
  # @param {@rowIndexA: int, @rowIndexB: int}
  def swapRows(self, rowIndexA, rowIndexB):
    self.matrix[[rowIndexA,rowIndexB]] = self.matrix[[rowIndexB,rowIndexA]]

  # @type int 
  # @param {@columnIndex: int, @offset: int}
  # @return Row index greater or equal than offset with highest absolute value in specific column
  def biggestInColumnFrom(self, columnIndex, offset):
    # sum offset to retrieve matrix's original index
    return np.argmax(np.abs(self.matrix[offset:,columnIndex])) + offset

  def __str__(self):
    return str(self.matrix)