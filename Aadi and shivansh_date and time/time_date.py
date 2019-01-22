import numpy as np
import cv2
import time
cap = cv2.VideoCapture(0)

t = time.time()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_COMPLEX
    k1 = str(time.ctime())
    k2 = ky.split(" ")
    k3 = str(k[3])
    k4 = str((k[0]) + ', ' + k[1] + ' ' + k[2] + ' ' + k[4])
    frame = cv2.putText(frame, k3, (500,90), font, 0.5, (0, 0, 0), 2)
    frame = cv2.putText(frame, k4, (50,90), font, 0.5, (0, 0, 0), 2)
    frame = cv2.rectangle(frame,(475,70),(600,100),(255,255,255),2)
    frame = cv2.rectangle(frame,(25,70),(230,100),(255,255,255),2)
 
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
