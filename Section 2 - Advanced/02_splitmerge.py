
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r]) 


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)  # it return 3 parameters  (pixel , pixel , color channels(3)) because it is a main image
print(b.shape)    # it return 2 parameters  (pixel , pixel )
print(g.shape)    # it return 2 parameters  (pixel , pixel )
print(r.shape)    # it return 2 parameters  (pixel , pixel )

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)

