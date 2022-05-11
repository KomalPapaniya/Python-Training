import numpy as np
import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\ground_img.png')
cv2.imshow('Original', img)

rows, cols = img.shape[:2]

M = np.float32([[1,0,100],[0,1,50]])
shift = cv2.warpAffine(img, M, (cols,rows))
cv2.imshow('shift', shift)

M = cv2.getRotationMatrix2D(((cols-1)/2, (rows-1)/2), -75, 0.5)
rot = cv2.warpAffine(img, M, (cols,rows))
cv2.imshow('rotation', rot)

pts1 = np.float32([[50,50], [200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])
M = cv2.getAffineTransform(pts1, pts2)
aff = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('affine', aff)

# plt.subplot(121), plt.imshow(img), plt.title('Input')
# plt.subplot(122), plt.imshow(aff), plt.title('Output')
# plt.show()

pts11 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts22 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts11,pts22)
prs = cv2.warpPerspective(img,M,(300,300))
cv2.imshow('perspective', prs)

# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(prs),plt.title('Output')
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
