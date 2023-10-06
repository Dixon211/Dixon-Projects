import cv2
import tensorflow as tf
import threading

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#create a window object and capture the video from the default input
cv2.namedWindow("Found you")
vc=cv2.VideoCapture(0)

#open webcam
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

#what to do
while rval:



    cv2.imshow("Found you", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27:
        break

vc.release()
cv2.destroyWindow("preview")