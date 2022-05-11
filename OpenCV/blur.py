import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\coin.png')
img = cv2.resize(img, None, fx = 0.7, fy = 0.7)
print(img.shape)
img_copy = img.copy()
cv2.putText(img_copy, 'Original', (100,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
# cv2.imshow('Original', img)

# Image Filtering
kernel = np.ones((5,5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
cv2.putText(dst, 'Averaging', (90,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
# cv2.imshow('Averaging', dst)

# Averaging
blur = cv2.blur(img, (5,5))
cv2.putText(blur, 'Blur', (125,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
# cv2.imshow('Blur', blur)

# Gaussian Blurring
g_blur = cv2.GaussianBlur(img, (5,5), 0)
cv2.putText(g_blur, 'Gaussian Blur', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)
# cv2.imshow('Gaussian Blur', g_blur)

result1 = np.concatenate((img_copy, dst, blur, g_blur), axis=1)
cv2.imshow('IMAGE-1', result1)

# Median Blurring
noise = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\flower_noisy.jpg')
noise_copy = noise.copy()
cv2.putText(noise_copy, 'Original', (30,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
# cv2.imshow('Noisy Img', noise)

median = cv2.medianBlur(noise, 9)
cv2.putText(median, 'Median', (30,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
# cv2.imshow('Median', median)

# Bilateral Filtering
b_fltr = cv2.bilateralFilter(noise, 9, 75, 75)
cv2.putText(b_fltr, 'Bilateral Filter', (30,40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)
# cv2.imshow('Bilateral Filter', b_fltr)

result2 = np.concatenate((noise_copy ,median ,b_fltr), axis=1)
cv2.imshow('IMAGE-2', result2)

cv2.waitKey(0)
cv2.destroyAllWindows()

