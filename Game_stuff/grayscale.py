import cv2
import sys

def grayscale_view(queue = None):
    vc = cv2.VideoCapture(0)
    print("attempting to capture video")
    i = 5
    while i > 0:
        i = i-1
        print(i)
    while True:
        print("loop boy")
        frame = queue.get()
        rval, frame = vc.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Camera Feed", gray)
        print(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            sys.exit()
        
    vc.release()
    cv2.destroyAllWindows()

