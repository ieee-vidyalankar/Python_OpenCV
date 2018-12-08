import cv2
import numpy as np

#capture video from webcam '0' denotes webcam of laptop
cap=cv2.VideoCapture(0)

#loop for frames
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    #hue, saturation, and value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of skin color in HSV
    lower_skin = np.array([0, 30, 60])
    upper_skin = np.array([20, 150, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    #keep the window till q is pressed
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
