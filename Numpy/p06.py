import numpy as np

# program to compute the inverse of a given matrix
matrix = np.array([[1, 2, 3],
                  [0, 1, 4],
                  [5, 6, 0]])
                  
print(np.linalg.inv(matrix))