import cv2
import numpy

cam = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('eye-tracker/haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier('eye-tracker/haarcascade_eye_tree_eyeglasses.xml')

if not cam.isOpened():
    print("Error: Unable to open the webcam.")
    exit()

# Webcam loop
while cam.isOpened():
    ret, frame = cam.read()

    # Horizontally flip the frame
    frame = cv2.flip(frame, 1)

    # Covert the frame into grayscale
    faceGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(faceGray, 1.1, 4)

    # Face Loop
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 255), 5)
        eyesGray = faceGray[y:y+h, x:x+w]
        eyesColor = frame[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(eyesGray)

        # Eyes Loop
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(eyesColor, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 5)

    cv2.imshow('Eye Tracker', frame)

    # Exit the loop (Backspace)
    if cv2.waitKey(1) & 0xFF == 8: # Masks the last 8 bits which are the only bits needed to recongnize the key-press. '8' represents the number for backspace. 
        break
 
cam.release()
cv2.destroyAllWindows()