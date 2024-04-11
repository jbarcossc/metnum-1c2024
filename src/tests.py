import unittest
from matrix import Matrix
import numpy as np

class TestMatrix(unittest.TestCase):

    def test_init(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        self.assertEqual(matrix.matrix.tolist(), data)

    def test_multiply_row(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        matrix.multiplyRow(1, 2)
        self.assertEqual(matrix.matrix.tolist(), [[1, 2], [6, 8]])

    def test_substract_row(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        matrix.substractRow(1, 0, 2)
        self.assertEqual(matrix.matrix.tolist(), [[1, 2], [1, 0]])

    def test_swap_rows(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        matrix.swapRows(0, 1)
        self.assertEqual(matrix.matrix.tolist(), [[3, 4], [1, 2]])

    def test_swap_cols(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        matrix.swapCols(0, 1)
        self.assertEqual(matrix.matrix.tolist(), [[2, 1], [4, 3]])

    def test_biggest_in_column_from(self):
        data = [[4,-60,2],[-2,1,3],[2,0,2]]
        matrix = Matrix(data)
        index = matrix.biggestInColumnFrom(1, 0)
        self.assertEqual(index, 0)
    
    def test_biggest_in_column_from2(self):
        data = [[4,-60,2],[-2,1,3],[2,2,2]]
        matrix = Matrix(data)
        index = matrix.biggestInColumnFrom(1, 1)
        self.assertEqual(index, 2)

    def test_shape(self):
        data = [[1, 2, 3], [3, 4, 1]]
        matrix = Matrix(data)
        shape = matrix.shape()
        self.assertEqual(shape, [2, 3])

    def test_at(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        value = matrix.at(1, 0)
        self.assertEqual(value, 3)
        
    def test_equal(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        self.assertEqual(matrix.equal(data), True)
        
    def test_gaussian_elimination(self):
        data = [[4,-2,2],[-2,1,1],[2,2,2]]
        matrix = Matrix(data)
        b = [5,2,1]
        matrixValue, bValue = matrix.gaussianElimination(b)
        expectedB = np.array([5,-1.5,4.5], dtype = float)
        expectedMatrix = [[4,-2,2],[0,3,1],[0,0,2]]
        self.assertEqual(np.array_equal(bValue, expectedB), True)
        self.assertEqual(matrixValue.equal(expectedMatrix), True)

    def test_solve(self):
        data = [[4,-2,2],[-2,1,1],[2,2,2]]
        matrix = Matrix(data)
        b = [5,2,1]
        value = matrix.solve(b)
        self.assertEqual(value, [-0.5,-1.25,2.25])

    def test_str(self):
        data = [[1, 2], [3, 4]]
        matrix = Matrix(data)
        string_rep = str(matrix)
        self.assertEqual(string_rep, '[[1. 2.]\n [3. 4.]]')

if __name__ == '__main__':
    unittest.main()
