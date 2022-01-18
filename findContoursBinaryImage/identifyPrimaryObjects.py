import cv2
import numpy as np

# Set location and load image
image_to_read='' 
img = cv2.imread(image_to_read)

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('threshold',thresh)
# get contours
result = img.copy()
contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

contour_image=cv2.drawContours(img,contours,-1,(255,0,0),3)
cv2.imshow('Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TO DO: calculate distance from center
