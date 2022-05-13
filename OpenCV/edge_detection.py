import numpy as np
import cv2 
from matplotlib import pyplot as plt
img = cv2.imread(r'C:\Users\wot-komal\Desktop\Komal_Training\Python_Training\OpenCV\Images\blue_ball.png',0)
edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()