import numpy as np

# program to compute the determinant of a given square array
sq_array = np.array([[1, 2, 3], 
                     [0, -1, 2], 
                     [-2, 0, 1]])

print(np.linalg.det(sq_array))