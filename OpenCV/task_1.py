import cv2
import numpy as np

im = cv2.imread(r'OpenCV\Images\sunflower.jpg')
im = cv2.resize(im, None, fx = 0.25, fy = 0.25)
# cv2.imshow("Original", im)

# Blur
g_blur = cv2.GaussianBlur(im, (5,5), 0)
# cv2.imshow('Blur', g_blur)

# Sharpen
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
sharp = cv2.filter2D(im, -1, kernel)
# cv2.imshow("Sharpen", sharp)

# Edge Detection
edges = cv2.Canny(im, 300, 150)
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
# cv2.imshow("Edges", edges)

# Contours
img = cv2.imread(r'OpenCV\Images\flower.jpg')
img = cv2.resize(img, None, fx = 0.5, fy = 0.5)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# cv2.imshow("thresh",thresh)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
im2 = img.copy()
C = cv2.drawContours(im2, contours, -1, (0,255,0), 1)
# cv2.imshow("Contours", C)

# res = np.concatenate((im, g_blur, sharp, edges, C), axis=1)
cv2.imshow("Result", C)

cv2.waitKey(0)
cv2.destroyAllWindows()