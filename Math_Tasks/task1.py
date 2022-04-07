# Let's imagine a rectangle of height 1 and length 2. The four corner points of the rectangle are:
# a = (0, 0)
# b = (2, 0)
# c = (2, 1)
# d = (0, 1)
# Now, apply the shearing transformation to these four points. Can you imagine the rectangle turning into a parallelogram.
# Shear matrix = [[1, 1], [0, 1]]
# Now the origin has been shifted to (1, 3)
# What will be the output points: - Solve using 2 approaches
# Without using numpy or 2D list
# Use numpy for matrix computation

# Without using numpy 2D List
a = (0, 0)
b = (2, 0)
c = (2, 1)
d = (0, 1)

# dividing shear matrix into rows
r1 = [1, 1]
r2 = [0, 1]

# finding new co-ordinates
a0 = (r1[0] * a[0]) + (r1[1] * a[1])
a1 = (r2[0] * a[0]) + (r2[1] * a[1])
s_a = tuple((a0, a1))

b0 = (r1[0] * b[0]) + (r1[1] * b[1])
b1 = (r2[0] * b[0]) + (r2[1] * b[1])
s_b = tuple((b0, b1))

c0 = (r1[0] * c[0]) + (r1[1] * c[1])
c1 = (r2[0] * c[0]) + (r2[1] * c[1])
s_c = tuple((c0, c1))

d0 = (r1[0] * d[0]) + (r1[1] * d[1])
d1 = (r2[0] * d[0]) + (r2[1] * d[1])
s_d = tuple((d0, d1))

# printing points of parallelogram
print('points of parallelogram: ')
print(s_a)
print(s_b)
print(s_c)
print(s_d)

# new points after origin shifted to (1, 3)
origin = (1, 3)
new_a = tuple((s_a[0] + origin[0], s_a[1] + origin[1]))
new_b = tuple((s_b[0] + origin[0], s_b[1] + origin[1]))
new_c = tuple((s_c[0] + origin[0], s_c[1] + origin[1]))
new_d = tuple((s_d[0] + origin[0], s_d[1] + origin[1]))

print('\nnew points: ')
print(new_a)
print(new_b)
print(new_c)
print(new_d)


# Using numpy for matrix Computation

import numpy as np

a = np.array([0, 0])
b = np.array([2, 0])
c = np.array([2, 1])
d = np.array([0, 1])

shear_matrix = [[1, 1], [0, 1]]

s_a = np.dot(shear_matrix, a)
s_b = np.dot(shear_matrix, b)
s_c = np.dot(shear_matrix, c)
s_d = np.dot(shear_matrix, d)

# new points after origin shifted to (1, 3)
origin = np.array([1, 3])

print('new points: ')
print(origin + s_a)
print(origin + s_b)
print(origin + s_c)
print(origin + s_d)