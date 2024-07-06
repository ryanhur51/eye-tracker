import cv2
import numpy

cam = cv2.VideoCapture(0)

# Loading the webcam.
while True:
    ret, frame = cam.read()
    if not ret:
        print('Error, failed to capture the frame')
    cv2.imshow  ('Hello world', frame)
    if cv2.waitKey(1) & 0xFF == 8: # Masks the last 8 bits which are the only bits needed to recongnize the key-press. '8' represents the number for backspace. 
        break

cam.release()
cv2.destroyAllWindows()