import cv2
import numpy as np

# n_img = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\blue_ball.png')
n_img = cv2.imread(r'OpenCV\Images\flower.jpg')
# print(n_img.shape)
# print(repr(n_img))

# frame = cv2.resize(n_img, (416, 371))
# cv2.imshow('image', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

frame = n_img

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)

# define range of blue color in HSV
lower_blue = np.array([0,0,200])
upper_blue = np.array([145,60,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('hsv',hsv)

k = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
# print(hsv)

