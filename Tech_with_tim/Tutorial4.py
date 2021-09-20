'''Drawing line, circle, rectangel, Text and some more using opencv'''

import cv2
import numpy as np

video = cv2.VideoCapture(0)
width = int(video.get(3))
height = int(video.get(4))

while True:
    rep, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    h,s,b = 40,2,70

    lower_white = np.array([0, 0, 0])
    upper_white = np.array([0, 0, 255])

    mask = cv2.inRange(hsv,lower_white,upper_white)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame', result)
    if cv2.waitKey(1) == ord('Q'):
        break

video.release()
cv2.destroyAllWindows()