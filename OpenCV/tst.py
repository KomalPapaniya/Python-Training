import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\wot-komal\\Desktop\\Komal_Training\\Python_Training\\OpenCV\\Images\\apple.jpg')
cv2.imshow('Original', img)
print(type(img))
cv2.waitKey(0)
cv2.destroyAllWindows()

