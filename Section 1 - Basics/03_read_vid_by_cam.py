import cv2

# Open a video capture object (camera)
capture = cv2.VideoCapture(0)  # 0 represents the default camera (you can change it to the camera index you want)

# Set the width of the captured frames to 640 pixels
capture.set(3, 640)

# Read and display frames
while True:
    ret, frame = capture.read()

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close windows
capture.release()
cv2.destroyAllWindows()
