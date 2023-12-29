import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Could not open camera")
    exit()

# Set up an infinite while loop
while True:
    # Read the frame
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Could not read frame")
        break

    # Display the frame
    cv2.imshow('frame', frame)

    # Break the loop if the user presses 'c'
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

# Release the camera
cap.release()

# Close all windows
cv2.destroyAllWindows()