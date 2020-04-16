import cv2
import random

cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)  # 0 for web camera live stream
#video_capture = cv2.VideoCapture('rtsp://username:password@ip_address:554/h264Preview_01_sub')



def camera_stream():
     # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # Draw a rectangle around the faces
    # Radius of circle
    r = 20
    # Blue color in BGR
    color = (0, 69, 255)
    # Line thickness of 2 px
    thickness = 2
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    # org
    org = (50, 50)
    # fontScale
    fontScale = 0.9
    # Blue color in BGR
    txtcolor = (255, 0, 0)
    # Line thickness of 2 px
    txtthickness = 2
    for (x, y, w, h) in faces:
        my_temp = str(random.randint(358, 364) / 10)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.ellipse(frame, (x + int(w/2), y), (r*3, r), 0, 0, 360, color, thickness)
        cv2.putText(frame, my_temp, (x + int(w/3), y + int(r/2)), font, fontScale, txtcolor, txtthickness, cv2.LINE_AA)

    # Display the resulting frame in browser
    return cv2.imencode('.jpg', frame)[1].tobytes()
