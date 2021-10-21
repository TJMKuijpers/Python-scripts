import cv2
import numpy as np

# read image
img = cv2.imread('C:/Users/tkuijpe1/OneDrive - TU Eindhoven/Documents/01_Projects/04_ImageRecognitionFeatures/Surface_FeatureIdx_10.png')

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
