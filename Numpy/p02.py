import numpy  as np

# program to compute the outer product of two given vectors 
vector_1 = np.array([3, 5, 2, 10])
vector_2 = np.linspace(1, 2, 5)

print(np.outer(vector_1, vector_2))