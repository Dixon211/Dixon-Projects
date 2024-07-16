import cv2

def overlay(image):
    copy = image.copy()
    #top
    cv2.rectangle(copy, (0,0), (copy.shape[1],int(copy.shape[0]/6)), (0,0,0), -1)
    #bottom
    cv2. rectangle(copy, (copy.shape[1],copy.shape[0]), (0,int((5*copy.shape[0])/6)), (0,0,0), -1)
    #leftside
    cv2.rectangle(copy, (0, 0), (int(copy.shape[1]/8), copy.shape[0]), (0,0,0), -1)
    #rightside
    cv2.rectangle(copy, (copy.shape[1], copy.shape[0]), (int(7*copy.shape[1]/8), 0), (0,0,0), -1)
    #middle
    cv2.rectangle(copy, (int(3*copy.shape[1]/8),0), (int(5*copy.shape[1]/8),copy.shape[0]), (0,0,0), -1)

    copy = cv2.addWeighted(copy, 0.5, image, 1-(0.5), 0, image)

    cv2.rectangle(copy, (int(frame.shape[1]/8),int(frame.shape[0]/6)), (int(3*frame.shape[1]/8), int(5*frame.shape[0]/6)), (0,0,255), 2)
    cv2.rectangle(copy, (int(5*frame.shape[1]/8), int(frame.shape[0]/6)), (int(7*frame.shape[1]/8), int(5*frame.shape[0]/6)), (0,0,255), 2)

def overlay2(image):
    text = f"Put hands in center of rectangles"
    font = cv2.FONT_HERSHEY_COMPLEX
    fontsize = .5
    fontthickness = 2
    fontcolor = (0,0,0)
    
    #add rectangles
    cv2.rectangle(image, (int(image.shape[1]/8),int(image.shape[0]/6)), (int(image.shape[1]*(3/8)), int(image.shape[0]*(5/6))), (0,0,255), 2)
    cv2.rectangle(image, (int(image.shape[1]*(5/8)), int(image.shape[0]/6)), (int(image.shape[1]*(7/8)), int(image.shape[0]*(5/6))), (0,0,255), 2)

    # calculate to compensate for string length, font size. Then place text
    text_size = cv2.getTextSize(text, font, fontsize, fontthickness)
    text_x = int(frame.shape[1]/2-(text_size[0][0]/2)) 
    text_y = int(frame.shape[0]/12)
    cv2.putText(image, text, (text_x, text_y), font, fontsize, fontcolor, fontthickness)

cap =cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    overlay2(frame)
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()