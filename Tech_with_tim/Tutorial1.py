'''
Read, Save and Rotate image using OpenCV
'''

import cv2
import numpy as np
img = cv2.imread('Images/Lofi_cafe_wallpaper.jpg', 1)
# 1 for original
# 0 for greyscale
# -1 for transparent pixels
cv2.rotate(img,cv2.ROTATE_180) # to rotate the image

cv2.resize(img,(400,400)) #make the image 400*400
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) # make the image half of the original size

cv2.imshow('white',img)

#Save the opencv image
cv2.imwrite('imdownloaded', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
How to change and replace the image part
'''
img = cv2.imread('Images/Lofi_cafe_wallpaper.jpg',1)
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) # make the image half of the original size
print(img.shape)
img[0:300,300:600] = img[200:500,500:800]

cv2.imshow('replaced',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
