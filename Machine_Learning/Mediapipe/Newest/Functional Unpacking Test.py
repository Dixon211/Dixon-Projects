import cv2
import mediapipe as mp


class Handcontroller:
    def __init__(self, handclass):
        self.handata = handclass
        self.activation = 0
        self.activestartx, self.activestarty = 0,0
        self.results = 0
        self.thumbx, self.thumby = 0,0
        self.pointerx, self.pointery = 0,0
    def updatevalues(self, ):





#place circles and put coordinates into JSON formatting
def unpack_landmarks(results, frame):
    ML_positions = {}
    for j, hand_landmarks in enumerate(results.multi_hand_landmarks):
        hands = {}
        for i, handlandmark in enumerate(hand_landmarks.landmark):
            match i:
                case 4:
                    x,y= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                    hands["Thumb"] = [x, y]
                case 8:
                    x,y= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                    hands["Pointer"] = [x, y]
                case 12:
                    x,y= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                    cv2.circle(frame,(x, y), 5, (0,0,255), -1)
                    hands["Middle"] = [x, y]
                case 16:
                    x,y= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                    cv2.circle(frame,(x, y), 5, (0,0,255), -1)
                    hands["Ring"] = [x, y]
                case 20:
                    x,y= int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                    cv2.circle(frame,(x, y), 5, (0,0,255), -1)
                    hands["Pinky"] = [x, y]
        ML_positions[f"{j}"] = hands
    return(ML_positions)


def check_position(ML_positions, frame):
    #detection modifier range
    ds = 20
    thumbx, thumby = int(ML_positions['0']['Thumb'][0]), int(ML_positions['0']['Thumb'][1])
    cv2.circle(frame, (thumbx, thumby), 5, (0,255,0),-1)

    pointerx, pointery = int(ML_positions['0']['Pointer'][0]), int(ML_positions['0']['Pointer'][1])
    if thumbx in range(pointerx-ds, pointerx+ds):
        if thumby in range(pointery-ds, pointery+ds):
            cv2.circle(frame, (thumbx, thumby), 5, (255,0,0),-1)
            cv2.circle(frame, (pointerx,pointery), 5, (255,0,0),-1)  
    return 0


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0)

#Main            
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results=hands.process(image)
    #process to put circles on the image and what color they are
    if results.multi_hand_landmarks:
        ML_positions = unpack_landmarks(results, frame)
        check_position(ML_positions, frame)

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()