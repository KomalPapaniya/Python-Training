import numpy as np

# program to compute the sum of the diagonal elements of a given array
A = np.array([[3, 4, 5],
              [-1, -2, 4],
              [-5, 0, 6]])
                
print(np.trace(A))