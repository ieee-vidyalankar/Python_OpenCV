import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('grid.jpg')
rows,cols,ch = img.shape

#draw circles at desired coordinates
cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)
cv2.circle(img, (447, 472), 5, (0, 0, 255), -1)

#points where transformation is to be occured
pts1 = np.float32([[83,90],[447,90],[83,472],[447,472]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
#perform transformation
M = cv2.getPerspectiveTransform(pts1,pts2)
#wrap the image
dst = cv2.warpPerspective(img,M,(600,600))
#plot the image results
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
