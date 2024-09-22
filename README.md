# Simple Face Detection with OpenCV

This project = Simple Face Detection using Python3.x, OpenCV and the Haar Cascade classifier to detect faces in real-time from a webcam feed. The program captures video, processes each frame to detect faces, and displays the count of faces detected on the screen.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.x
- OpenCV
- NumPy

You can install the required packages using pip:

```bash
pip install opencv-python numpy
```

Additionally, you need the Haar Cascade XML file for face detection. It is included in OpenCV, but you can also download it manually from this [link](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## How to Run

1. Clone this repository or download the script.
2. Ensure you have a webcam connected to your system.
3. Place the haarcascade_frontalface_default.xml file in the same directory as your script.
4. Run the Python script:

```bash
python script.py
```

The webcam will activate, and the program will begin detecting faces. The number of faces detected will be displayed on the video feed.

## Explanation of the Code

- Libraries Used:

  - cv2: The OpenCV library is used for video capture and image processing.
  - numpy: This is required for handling arrays, although it's not directly used in this example.
  - time: The time module is imported but not used.

- Face Classifier:
  The face detection is done using OpenCV’s pre-trained model haarcascade_frontalface_default.xml:

```python
# Load the face classifier
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
```

- Video Capture:
  The cv2.VideoCapture(0) function is used to access the webcam feed. If the camera is unavailable, an error message is printed:

```python
# Access the webcam
video_capture = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not video_capture.isOpened():
    print("Unable to access the camera")
    exit()
```

- Face Detection and Display:
  The program reads frames from the webcam and converts them to grayscale. It then applies the face classifier to detect faces, drawing rectangles around them and showing the number of faces detected on the screen:

```python
# Convert the frame to grayscale
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
# Detect faces in the frame
faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=2)
```

Each face detected is highlighted with a green rectangle, and the face count is displayed in blue text at the top of the screen.

- Exiting the Program:
  The program will continue running until the user presses the 'q' key, which exits the loop and stops the video capture.

## Sample Output:

Once the script is running, you will see a video window from your webcam with rectangles drawn around detected faces and the total face count displayed at the top.

<hr/>

## Future Enhancements

- Improve face detection accuracy by adjusting the scaleFactor and minNeighbors parameters.
- Add functionality to recognize and label specific faces.
- Implement real-time emotion detection or other advanced features.

## License

This project is open-source and available under the MIT License.

<br/>"# Simple-Face-Detection-with-OpenCV" 
