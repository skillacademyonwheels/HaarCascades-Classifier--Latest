import cv2
import os

#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

opencv_data_dir = cv2.data.haarcascades
xml_path = os.path.join(opencv_data_dir, "haarcascade_frontalface_default.xml")

face_cascade = cv2.CascadeClassifier(xml_path)
if face_cascade.empty():

    print("Error: Could not load the face cascade classifier!")

else:

    print("Success: Face cascade loaded perfectly!")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("error: Could not open camera")
    exit()

while True:
    ret,frame = cap.read()

    if not ret:
        print("error:Failed to capture image")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    for (x, y, w, h) in faces:
     cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection - press q to quit',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


### Install - 
## opencv-python &  opencv-contrib-python