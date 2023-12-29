
import cv2 as cv


img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)


# these are the multiple type of to make blur the image.

# Averaging
avg = cv.blur(img,(7,7))
cv.imshow('Average Blur',avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

# Mediun Blur
median = cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

# Bilateral Filter
bilateral = cv.bilateralFilter(img , 5 , 35 , 25 )  # we can also change the last 2 values which show the image better
cv.imshow('Bilateral Filter',bilateral)

cv.waitKey(0)

