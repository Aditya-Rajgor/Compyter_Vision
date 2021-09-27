'''Face and eye detection'''

import cv2
import numpy as np

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
        roi_gray = gray[y:y+w,x:x+h]
        roi_real = frame[y:y+w,x:x+h]
        eye = eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_real,(ex,ey),(ex+ew,ey+eh),(255,0,0),5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('Q'):
        break

video.release()
cv2.destroyAllWindows()