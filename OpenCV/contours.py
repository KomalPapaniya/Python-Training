from cv2 import circle
import numpy as np
import cv2

im = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\star-2.jpg')
im = cv2.resize(im, None, fx = 0.5, fy = 0.5)
print(im.shape)
# cv2.imshow('Image', im)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[-1]
M = cv2.moments(cnt)
print( M )

area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt,True)
print('area=', area)
print('Perimeter=', perimeter)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
print('hull=', hull)
print('hull Area=', float(area)/hull_area)

k = cv2.isContourConvex(cnt)
print('k=', k)


# cy = int(M['m01']/M['m00'])
# cx = int(M['m10']/M['m00'])
# print(cx, cy)

# print(contours)

c = cv2.drawContours(thresh, contours, -1, (0,255,0), 3)
# c = cv2.drawContours(thresh, contours, 3, (0,255,0), 3)
cv2.imshow('C', c)

x,y,w,h = cv2.boundingRect(cnt)
rect = cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('rect', rect)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
min_rect = cv2.drawContours(im,[box],0,(0,0,255),2)
cv2.imshow('min_rect', min_rect)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
circl = cv2.circle(im,center,radius,(0,255,0),2)
cv2.imshow('circle', circl)

ellipse = cv2.fitEllipse(cnt)
ellipse = cv2.ellipse(im,ellipse,(0,255,0),2)
cv2.imshow('ellipse', ellipse)
 

x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print('Aspect Ratio=', aspect_ratio)

rect_area = w*h
extent = float(area)/rect_area
print('Extent=', extent)

cv2.waitKey(0)
cv2.destroyAllWindows()
