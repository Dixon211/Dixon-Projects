import cv2
import numpy as np

vc = cv2.VideoCapture(0)


while True:
    _, frame = vc.read()
    frame_copy = frame.copy()
    height, width, _ = frame.shape
    #print(str(height) + " " + str(width))

    #guidelines for card
    #horizontal
    #cv2.line(video, (1, height//8), (width, height//8), (0,255,0), 2)
    #cv2.line(video, (1, (height//4)*2), (width, (height//4)*2), (0,255,0), 2)
    #cv2.line(video, (1, (height//8)*7), (width, (height//8)*7), (0,255,0), 2)
    #vertical
    #cv2.line(video, ((width//4), 1), ((width//4), height), (0,0,255), 2)
    #cv2.line(video, ((width//4)*2, 1), ((width//4)*2, height), (0,0,255), 2)
    #cv2.line(video, ((width//4)*3, 1), ((width//4)*3, height), (0,0,255), 2)

    #bounding box for card
    cv2.rectangle(frame_copy, 
    (((width//32)*9),(height//8)), 
    (((width//32)*23),((height//8)*7)),
    (255,0, 0), 
    5)

    #deadarea
    #leftbox
    cv2.rectangle(frame_copy,
    (1,1),
    (((width//32)*9), height),
    (0,0,0),
    -1)
    #topbox
    cv2.rectangle(frame_copy,
    (1,1),
    (width, (height//8)),
    (0,0,0),
    -1)
    #rightbox
    cv2.rectangle(frame_copy,
    (width, 1),
    (((width//32)*23), height),
    (0,0,0),
    -1)
    #bottombox
    cv2.rectangle(frame_copy,
    (width, height),
    (1, ((height//8)*7)),
    (0,0,0),
    -1)


  
    
    frame_with_overlay = cv2.addWeighted(frame_copy, .5, frame, 1, 0)
    cv2.imshow("VideoFeed", frame_with_overlay)
    #cv2.imshow("original", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

vc.release()    
cv2.destroyAllWindows()