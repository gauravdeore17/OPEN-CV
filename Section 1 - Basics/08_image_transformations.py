
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# For Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right 
# y --> Down

translated = translate(img, -100, 100)  # ranslate(img,X,Y)
cv.imshow('Translated', translated)

#  For Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

#  For Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# For Flipping
# Flip the frame horizontally (1 for horizontal, 0 for vertical, -1 for both)
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# For Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
'''
 img[200:400, 300:400]: This line uses array slicing to extract a subregion 
 of the image. The format is img[y_start:y_end, x_start:x_end], where y_start, y_end, x_start, 
 and x_end define the range of rows and columns to be extracted. In this case, it is extracting 
 rows from 200 to 399 and columns from 300 to 399.
'''
cv.waitKey(0)