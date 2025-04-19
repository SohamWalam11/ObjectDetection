# import cv2
# capture=cv2.VideoCapture(0)
# while True:
#     ret,frame=capture.read()
#     cv2.imshow('Color',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# capture.release()
# cv2.
# cv2.destroyAllWindows()

import cv2

# Initialize video capture from the default camera (0)
capture = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not capture.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()
    
    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break
    
    # Display the resulting frame
    cv2.imshow('Color', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()