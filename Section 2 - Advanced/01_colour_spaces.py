
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)



'''

1. BGR to Grayscale : For Simplicity and Reduced Dimensionality , Computational Efficiency,
                                   Compatibility with Algorithms & noise reduction

'''

'''

2. BGR to HSV : Converting an image from the BGR color space to the HSV color space can be beneficial for 
             various image processing tasks, especially when dealing with color information. The HSV color 
             space separates the color information into three components: Hue, Saturation, and Value.

what is HSV :

   * Hue (H): Represents the type of color. It is expressed as an angle from 0 to 360 degrees on the color wheel, 
              where 0 and 360 both correspond to red.

   * Saturation (S): Represents the intensity or vividness of the color. A saturation value of 0 corresponds 
                     to grayscale (no color), and a saturation value of 1 corresponds to pure color.

   * Value (V): Represents the brightness of the color. It ranges from 0 to 1, with 0 being black and 1 being 
                the maximum brightness.
                
 Very useful for complex computer vision task like : 
     
     1. Color Filtering: You can easily filter specific colors by setting appropriate ranges for the Hue, 
                         Saturation, and Value components.

     2. Color Segmentation: Separating objects based on color becomes simpler in the HSV space compared to 
                            the RGB or BGR space.

     3. Image Recognition: HSV can be more robust in certain lighting conditions compared to RGB, making it 
                           useful for object recognition tasks.

     4. Color-based Thresholding: Thresholding based on color information can be more intuitive in HSV, 
                                  especially when the lighting conditions vary.

'''

'''

3. BGR to L*a*b : Converting an image to the Lab color space in OpenCV is often done for various computer 
                  vision and image processing tasks. The Lab color space separates color information into 
                  three components: L* (luminance), a* (green to red), and b* (blue to yellow). Unlike RGB 
                  and HSV, the Lab color space is designed to be perceptually uniform, meaning that a uniform 
                  change in color values should correspond to a perceptually uniform change in color.

 why we might want to convert an image to the Lab color space in OpenCV:

    1. Color Invariance: The Lab color space is more perceptually uniform than RGB, making it useful for 
                         tasks where you want color information to be invariant to changes in lighting conditions.

    2. Color-based Segmentation: In certain image processing tasks, such as segmentation, color information 
                                 is crucial. The Lab color space can make it easier to separate color regions 
                                 in an image.

    3. Color Quantization: Lab can be useful in color quantization tasks, where you want to reduce the number 
                           of colors in an image while preserving perceptual differences between colors.

    4. Color Correction: Lab is sometimes used in color correction algorithms, as it provides a more accurate 
                         representation of human perception of color.

'''

'''

4. BGR to RGB : It's common to convert images from BGR (Blue-Green-Red) to RGB (Red-Green-Blue) color space 
                when working with many libraries and tools outside of OpenCV. The reason for this lies in the 
                convention used by various image processing libraries and applications.

        In OpenCV, the default color space for reading and displaying images is BGR. However, many other libraries 
    and tools, such as Matplotlib and most image processing algorithms, expect images in RGB format.

'''

'''

5. HSV to BGR : Converting an image from HSV (Hue-Saturation-Value) to BGR (Blue-Green-Red) in OpenCV is often 
                done when you want to perform operations or manipulations in the HSV color space and then convert 
                the result back to BGR for visualization or further processing. The HSV color space is useful for
                tasks involving color manipulation because it separates the color information into three components:

           1. Hue (H): Represents the color information.
           2. Saturation (S): Represents the intensity of the color.
           3. Value (V): Represents the brightness of the color.
           
        Performing operations in the HSV color space can be beneficial for certain tasks, such as color-based 
    object detection, segmentation, or image editing. Once you've manipulated the image in the HSV color space, 
    you may want to convert it back to BGR for display or further processing, as BGR is a common color 
    representation in OpenCV.

'''