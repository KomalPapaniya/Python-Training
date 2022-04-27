import math
A = [[3,-1],
     [0,1]]
# A = [[a,b],
#      [c,d]]

a = A[0][0]
b = A[0][1]
c = A[1][0]
d = A[1][1]
Tr = a + d  # trace of A
det = a*d - b*c  # determinant of A

# Finding eigenvalues
e_values = []
L1 = (Tr + math.sqrt(Tr**2 - 4*det))/2
L2 = (Tr - math.sqrt(Tr**2 - 4*det))/2
e_values.append(L1)
e_values.append(L2)
print('Eigenvalues: ', e_values)

# Finding eigenvectors
e_vectors = []
if b == 0 and a - L1 == 0:
    V1 = [d - L1, -c]
else:
    V1 = [-b, a-L1]

if b == 0 and a - L2 == 0:
    V2 = [d - L2, -c]
else:
    V2 = [-b, a-L2]

e_vectors.append(V1)
e_vectors.append(V2)

for vector in e_vectors:
    if abs(vector[0]) > abs(vector[1]):
        v = vector[0]
    else:
        v = vector[1]

    if v != 0:
        vector[0] /= v
        vector[1] /= v
print('Eigenvectors', e_vectors)

