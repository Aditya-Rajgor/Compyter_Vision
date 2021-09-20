'''Mirroring webcam into 4 parts using openCV'''

import cv2
import numpy as np

video = cv2.VideoCapture(0)
print(np.uint8)
width = int(video.get(3))
height = int(video.get(4))

while True:
    rep, frame = video.read()
    new_image = np.zeros(frame.shape, np.uint8)

    #print(f'width is {width}, frame shape is {frame.shape}')

    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    new_image[:height//2,:width//2] = smaller_frame
    new_image[height//2:,:width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    new_image[:height//2,width//2:] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    new_image[height//2:,width//2:] = smaller_frame

    cv2.imshow('frame', new_image)
    if cv2.waitKey(1) == 113:
        break

video.release()
cv2.destroyAllWindows()