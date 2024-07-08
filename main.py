import cv2
import numpy

cam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(cam, cv2.COLOR_BAYER_BG2GRAY)
faces = face_cascade.detectMultiScale(gray, 1, 4)

# Loading the webcam.
while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print('Error, failed to capture the frame')
        break
    cv2.imshow('Eye Tracker', frame)

    if cv2.waitKey(1) & 0xFF == 8: # Masks the last 8 bits which are the only bits needed to recongnize the key-press. '8' represents the number for backspace. 
        break

    
    

cam.release()
cv2.destroyAllWindows()