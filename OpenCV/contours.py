import numpy as np
import cv2
im = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\coin.png')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(hierarchy)

# cv2.imshow('img', imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()
