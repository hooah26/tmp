import cv2

# Create VideoCapture objects for two webcams (0 and 1)
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

# Check if cameras opened successfully
if not (cap1.isOpened() and cap2.isOpened()):
    print("Error: Could not open cameras.")
    exit()

while True:
    # Capture frames from both cameras
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Check if frames were captured successfully
    if ret1 and ret2:
        # Display the frames
        cv2.imshow('Camera 1', frame1)
        cv2.imshow('Camera 2', frame2)

        # Break loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error reading frames.")
        break

# Release the VideoCapture objects and close the windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()
