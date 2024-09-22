import cv2
import numpy as np
import time

# Load the face classifier
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Access the webcam
video_capture = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not video_capture.isOpened():
    print("Unable to access the camera")
    exit()

# Loop until 'q' key is pressed
quit_key_pressed = False
while not quit_key_pressed:
    ret, frame = video_capture.read()

    if ret:
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=2)

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the number of faces detected
        face_count_text = f"Faces Detected = {len(faces)}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, face_count_text, (10, 30), font, 1, (255, 0, 0), 2)

        # Show the frame with detected faces
        cv2.imshow("Face Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            quit_key_pressed = True

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
