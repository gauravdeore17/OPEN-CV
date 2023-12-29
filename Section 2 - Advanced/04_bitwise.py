
import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)

'''
 * Bitwise Operations in Open CV:

        In OpenCV (Open Source Computer Vision Library), bitwise operations are commonly used for image 
    processing tasks, such as masking, logical operations, and bitwise manipulation. OpenCV provides several 
    bitwise operations that can be applied to images or binary masks. Here are some of the key bitwise 
    operations in OpenCV:

1. AND Operation (cv2.bitwise_and):

    Syntax: cv2.bitwise_and(src1, src2[, dst[, mask]])
    Performs bitwise AND operation between two input arrays (src1 and src2).
    dst: Destination array to store the result.
    mask: Optional mask specifying elements of the output array to be modified.

2. OR Operation (cv2.bitwise_or):
    Syntax: cv2.bitwise_or(src1, src2[, dst[, mask]])
    Performs bitwise OR operation between two input arrays (src1 and src2).

3. XOR Operation (cv2.bitwise_xor):
    Syntax: cv2.bitwise_xor(src1, src2[, dst[, mask]])
    Performs bitwise XOR operation between two input arrays (src1 and src2).
    
4. NOT Operation (cv2.bitwise_not):
    Syntax: cv2.bitwise_not(src[, dst[, mask]])
    Performs bitwise NOT operation on the input array (src).

    These bitwise operations are often used in combination with masks to selectively process 
regions of interest in images. Keep in mind that the input arrays should be of the same size 
when performing bitwise operations.

'''