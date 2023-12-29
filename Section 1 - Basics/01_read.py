import cv2 as cv

# for reading images

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img) # it show the seperate window with the window name and the what we have to show as img or vid    

cv.waitKey(0) # allows user to display the next window after some milisecond or untill the key is pressed


# for reading Videos

capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
# 0 represents the default camera (you can change it to the camera index you want)

while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            # waitkey is take the parameter as a milisecond or 'delay'
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
