import numpy as np

# program for multiplication of two matrices
matrix_a = np.array([[3, 2, 5], 
                     [-2, -1, 4],
                     [2, 1, -5]])

matrix_b = np.array([[2, 1], 
                     [0, -3], 
                     [1, 9]])

print(matrix_a.dot(matrix_b))
 