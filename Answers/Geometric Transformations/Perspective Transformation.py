import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('grid.jpg')
rows,cols,ch = img.shape

cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)
cv2.circle(img, (447, 472), 5, (0, 0, 255), -1)

pts1 = np.float32([[83,90],[447,90],[83,472],[447,472]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(600,600))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()