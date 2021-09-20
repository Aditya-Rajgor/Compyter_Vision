'''Detecting corners and drawing circle over it using openCV'''

import cv2
import numpy as np

img= cv2.imread('Images/chess_board.jpeg')
img = cv2.resize(img,(0,0), fx=0.5,fy=0.5)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey,30, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img,(x,y),5,(0,0,255),1)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()