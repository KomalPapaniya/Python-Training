import numpy as np
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\apple.jpg',0)
# img = cv2.resize(img, None, fx = 0.5, fy = 0.5)
edges = cv2.Canny(img, 300, 150)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
