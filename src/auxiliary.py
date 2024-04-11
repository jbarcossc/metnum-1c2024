import numpy as np

def vectorSwap(vector, indexA, indexB):
  aux = vector[indexA]
  vector[indexA] = vector[indexB]
  vector[indexB] = aux
  return vector

def vectorSubstract(vector, index, substractIndex, scalar):
  vector[index] -= vector[substractIndex]*scalar
  return vector