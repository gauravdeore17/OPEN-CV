#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# why we convert it into grayscale --> Simplicity and Reduced Dimensionality , Computational Efficiency,
#                                      Compatibility with Algorithms & noise reduction

# Blur --> To create the blur image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) # (7,7) is used to hadle the intensity of blur effect
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175) # here 125 and 175 is the lower and upper edges of threshold 
cv.imshow('Canny Edges', canny)

# Dilating the image ( dilation operation on the edges obtained from the Canny edge detector )
dilated = cv.dilate(canny, (7,7), iterations=3)  # iteration refere as how much dilation operation perform
cv.imshow('Dilated', dilated)

# Eroding --> commonly used for tasks such as noise reduction, object separation, and text extraction.
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)