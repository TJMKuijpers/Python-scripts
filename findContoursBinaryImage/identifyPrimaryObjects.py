import cv2
import numpy as np

# read image
img = cv2.imread('C:/Users/tkuijpe1/Desktop/aSMA analysis/AnnotationFiles/FeatureImages/Pattern_FeatureIdx_430.png')

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]

# get contours
result = img.copy()
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
counter=1
contour_info=dict()

for cntr in contours:
    x, y, w, h = cv2.boundingRect(cntr)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
    print("x,y,w,h:", x, y, w, h)
    # store infromation in dictionary
    contour_info['Object'+str(counter)]={'x':x,'y':y,'w':w,'h':h}
    counter=counter+1

# show thresh and result
cv2.imshow("bounding_box", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculate the distance between the ojects
# spacing objects: space=(x_object2)-(x_object1+w_object1)
