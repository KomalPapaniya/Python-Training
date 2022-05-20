import cv2
import numpy as np

A = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\apple.jpg')
A = cv2.resize(A, (512, 512))

B = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\orange.jpg')
B = cv2.resize(B, (512, 512))

rows, cols, ch = A.shape
# cv2.imshow('Apple', A)
# cv2.imshow('Orange', B)

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(5):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(5):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[-1]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[-1]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

cv2.imshow('blended', ls_)
cv2.imshow('real', real)

cv2.waitKey(0)
cv2.destroyAllWindows()
