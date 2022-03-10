import numpy as np

# program to compute the eigenvalues and eigenvectors of a given square array
A = np.array([[0, 1, 0], 
              [1, -1, 1], 
              [0, 1, 0]])

w, v = np.linalg.eig(A)
print("\nEigenvalues:\n", w)
print("\nEigenvectors:\n", v)
