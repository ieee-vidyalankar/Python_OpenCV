import cv2

img = cv2.imread('dragon.jpg')
rows,cols = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 30, 1)
img_rotation = cv2.warpAffine(img, rotation_matrix, (cols,rows))
cv2.imshow('rotated_img',img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()