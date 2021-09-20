'''Drawing line, circle, rectangel, Text and some more using opencv'''

import cv2
import numpy as np

video = cv2.VideoCapture(0)
width = int(video.get(3))
height = int(video.get(4))

while True:
    rep, frame = video.read()

    image = cv2.line(frame,(0,0),(width,height),(0,0,255),10)
    image = cv2.line(image, (width,0), (0,height), (0,0,255),10)
    image = cv2.rectangle(image, (100,100),(200,200),(255,0,0),-1)
    image = cv2.circle(image,(width//2,height//2),30,(0,255,0),2, lineType=2)
    image = cv2.putText(image,'Hello world !',(width//2,height//2+40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA)
    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('Q'):
        break

video.release()
cv2.destroyAllWindows()