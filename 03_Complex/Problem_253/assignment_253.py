'''
Write a Python Program to play a video in python
'''
import cv2

# Open the video file
video_path = 'path_to_your_video.mp4'  
cap = cv2.VideoCapture(video_path)

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Create a window to display the video
cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If the video has ended, break the loop
    if not ret:
        break

    # Display the current frame
    cv2.imshow('Video Player', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video file and close the window
cap.release()
cv2.destroyAllWindows()
