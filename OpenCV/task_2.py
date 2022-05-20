import cv2
import numpy as np

img = cv2.imread(r"OpenCV\Images\mountain.jpg")
# img = cv2.resize(img, None, fx = 0.5, fy = 0.5)


print(img.shape)
# print(img)

# cv2.imshow("Image", img)

pts_1 = np.array([[25, 70], [25, 160], [110, 200], [200, 160], [200, 70], [110, 20]])
pts_2 = np.array([[275, 70], [275, 160], [310, 200]])
pts = [pts_1, pts_2]
colors = [(255,0,0), (0,255,0)]


for i, p in enumerate(pts):
    img_c = img.copy()

    line = cv2.polylines(img_c,[p], isClosed=True, color=colors[i], thickness=1)
    cv2.imshow(f"Poly-{i+1}", line)
    cv2.waitKey(1000)

    poly = cv2.fillPoly(img_c, [p], color=colors[i])

    array = np.where(poly == colors[i], f'p{i+1}', '0')
    print(f"Array {i+1} : {array} \n\n\n")

    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# cv2.waitKey(0)
# cv2.destroyAllWindows()