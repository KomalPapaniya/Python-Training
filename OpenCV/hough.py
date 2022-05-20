import cv2
import numpy as np
# cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Result', (800,266))

# img1 = cv2.imread(r'OpenCV\Images\Sudoku-4.jpg')
# # img1 = cv2.resize(img1, None, fx = 0.5, fy = 0.5)
# print(img1.shape)
# img = img1.copy()
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# # lines = cv2.HoughLines(edges,1,np.pi/180,200)

# lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
# for line in lines:
#     x1,y1,x2,y2 = line[0]
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.imshow('houghlines5',img)


# for line in lines:
#     rho,theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    

# res = np.hstack((img1, img))
# cv2.imshow("Result", img)

# cv2.imshow("Edges", edges)
# cv2.imshow('houghlines3',img)

img = cv2.imread(r'OpenCV\Images\OpenCV_Logo.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


cv2.imshow('detected circles',cimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


cv2.waitKey(0)
cv2.destroyAllWindows()
