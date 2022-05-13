import cv2
import numpy as np
img_1 = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\letter_j\\j.png', 0)
cv2.imshow('Original Image', img_1)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img_1,kernel,iterations = 3)
cv2.imshow('erosion', erosion)

dilation = cv2.dilate(img_1,kernel,iterations = 2)
cv2.imshow('dilation', dilation)

img_2 = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\letter_j\\noisy_j-1.png', 0)
cv2.imshow('noisy j-1', img_2)

opening = cv2.morphologyEx(img_2, cv2.MORPH_OPEN, kernel, iterations = 3)
cv2.imshow('opening', opening)

img_3 = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\letter_j\noisy_j-2.png', 0)
cv2.imshow('noisy j-2', img_3)

closing = cv2.morphologyEx(img_3, cv2.MORPH_CLOSE, kernel, iterations = 3)
cv2.imshow('closing', closing)

gradient = cv2.morphologyEx(img_1, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Gradient', gradient)

kernel_1 = np.ones((25,25),np.uint8)
tophat = cv2.morphologyEx(img_1, cv2.MORPH_TOPHAT, kernel_1)
cv2.imshow('Tophat', tophat)

blackhat = cv2.morphologyEx(img_1, cv2.MORPH_BLACKHAT, kernel_1)
cv2.imshow('Blackhat', blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()

