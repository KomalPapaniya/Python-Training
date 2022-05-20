import numpy as np
import cv2

roi = cv2.imread(r'OpenCV\Images\rose_red.jpg')
roi = cv2.resize(roi, None, fx = 0.5, fy = 0.5)
# print(roi.shape)
hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

target = cv2.imread(r'OpenCV\Images\pink_rose_flower.jpg')
target = cv2.resize(target, (500, 725))
hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Target', hsvt)

# calculating object histogram
roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )


# normalize histogram and apply backprojection
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
cv2.filter2D(dst,-1,disc,dst)

# threshold and binary AND
ret,thresh = cv2.threshold(dst,50,255,0)
thresh = cv2.merge((thresh,thresh,thresh))
res = cv2.bitwise_and(target,thresh)
res = np.vstack((target,thresh,res))

# cv2.imshow('result',res)

cv2.waitKey(0)
cv2.destroyAllWindows()

