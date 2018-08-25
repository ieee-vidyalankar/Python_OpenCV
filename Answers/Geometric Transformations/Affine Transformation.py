import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread("dragon.jpg")
rows, cols, ch = img.shape
 
cv2.circle(img, (83, 90), 5, (255, 0, 0), -1)
cv2.circle(img, (447, 90), 5, (255, 0, 0), -1)
cv2.circle(img, (83, 472), 5, (255, 0, 0), -1)
 
pts1 = np.float32([[83, 90], [447, 90], [83, 472]])
pts2 = np.float32([[0, 0], [447, 90], [150, 472]])
 
matrix = cv2.getAffineTransform(pts1, pts2)
result = cv2.warpAffine(img, matrix, (cols, rows))
 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(result),plt.title('Output')
plt.show()