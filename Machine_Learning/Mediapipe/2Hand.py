import cv2
import mediapipe as mp
import pyautogui as pyag
import numpy as np

#public
def handid(image, cords1, cords2):
    text = f"Put hands in center of the squares"
    font = cv2.FONT_HERSHEY_COMPLEX
    fontsize = .5
    fontthickness = 2
    fontcolor = (0,0,0)
    leftboxcolor = (0,0,255)
    rightboxcolor = (0,0,255)
    leftcenter = int(image.shape[1]*(3/4)), int(image.shape[0]*(1/2))
    rightcenter = int(image.shape[1]*(1/4)), int(image.shape[0]*(1/2))

    # calculate to compensate for string length, font size. Then place text
    text_size = cv2.getTextSize(text, font, fontsize, fontthickness)
    text_x = int(frame.shape[1]/2-(text_size[0][0]/2)) 
    text_y = int(frame.shape[0]/12)
    cv2.putText(image, text, (text_x, text_y), font, fontsize, fontcolor, fontthickness)
    
    #add rectangles
    if np.linalg.norm(leftcenter-cords1) <= 20 or np.linalg.norm(leftcenter-cords2) <= 20:
        leftboxcolor = (0,255,0)
    cv2.rectangle(image, (int(image.shape[1]*(5/8)), int(image.shape[0]/3)), (int(image.shape[1]*(7/8)), int(image.shape[0]*(2/3))), leftboxcolor, 2)
    
    if np.linalg.norm(rightcenter-cords1) <= 20 or np.linalg.norm(rightcenter-cords2) <= 20:
        rightboxcolor = (0,255,0)
    cv2.rectangle(image, (int(image.shape[1]/8),int(image.shape[0]/3)), (int(image.shape[1]*(3/8)), int(image.shape[0]*(2/3))), rightboxcolor, 2)

    if leftboxcolor == (0,255,0) and rightboxcolor == (0,255,0):
        #if the distance from right to second set of cords is bigger than the distance to first set of coords
        if np.linalg.norm(rightcenter-cords2) > np.linalg.norm(rightcenter-cords1):
            return (False, True)
        else:
            return (True, False)
        
    return (None,None)



class Handcontroller():
    def __init__(self, string):
        self.string = string
        self.id = None
        self.cords = None
        self.midmemory = np.array([0,0])

    def drawcircles(self):
        for cord in self.cords:
            cv2.circle(frame, (cord[0], cord[1]), 5, (0,0,255),-1)

    def run(self):
        cv2.putText(frame, self.string, (self.cords['mid']), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)
        #self.drawcircles()
        self.midmemory = self.cords['mid']



if __name__ == "__main__":
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    cap =cv2.VideoCapture(0)
    left_hand= Handcontroller("left")
    right_hand= Handcontroller("right")
    screenx, screeny = pyag.size()
    pyag.FAILSAFE = False

    handcords = [
        {'thumb':np.array([0,0,0]), 'pointer':np.array([0,0,0]), 'middle':np.array([0,0,0]), 'ring':np.array([0,0,0]), 'pinky':np.array([0,0,0]), 'mid':np.array([0,0])},
        {'thumb':np.array([0,0,0]), 'pointer':np.array([0,0,0]), 'middle':np.array([0,0,0]), 'ring':np.array([0,0,0]), 'pinky':np.array([0,0,0]), 'mid':np.array([0,0])}
        ]
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        #image data and color convert
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        if results.multi_hand_landmarks:
            for j, singlehandlandmark in enumerate(results.multi_hand_landmarks):
                for i, handlandmark in enumerate(singlehandlandmark.landmark):
                    match i:
                        case 4:
                            try:
                                handcords[j]['thumb'][0] = int(handlandmark.x * frame.shape[1])
                                handcords[j]['thumb'][1] = int(handlandmark.y * frame.shape[0])
                                handcords[j]['thumb'][2] = int(handlandmark.z * 100)
                            except:
                                pass
                        case 8:
                            try:
                                handcords[j]['pointer'][0] = int(handlandmark.x * frame.shape[1])
                                handcords[j]['pointer'][1] = int(handlandmark.y * frame.shape[0])
                                handcords[j]['pointer'][2] = int(handlandmark.z * 100)
                            except:
                                pass
                        case 9:
                            try:
                                handcords[j]['mid'][0] = int(handlandmark.x * frame.shape[1])
                                handcords[j]['mid'][1] = int(handlandmark.y * frame.shape[0])
                            except:
                                pass
                        case 12:
                            try:
                                handcords[j]['middle'][0] = int(handlandmark.x * frame.shape[1])
                                handcords[j]['middle'][1] = int(handlandmark.y * frame.shape[0])
                                handcords[j]['middle'][2] = int(handlandmark.z * 100)
                            except:
                                pass
                        case 16:
                            try:
                                handcords[j]['ring'][0] = int(handlandmark.x * frame.shape[1])
                                handcords[j]['ring'][1] = int(handlandmark.y * frame.shape[0])
                                handcords[j]['ring'][2] = int(handlandmark.z * 100)
                            except:
                                pass
                        case 20:
                            try:
                                handcords[j]['pinky'][0] = int(handlandmark.x * frame.shape[1])
                                handcords[j]['pinky'][1] = int(handlandmark.y * frame.shape[0])
                                handcords[j]['pinky'][2] = int(handlandmark.z * 100)
                            except:
                                pass
            # check hands
            if left_hand.id == None:
                left_hand.id, right_hand.id = handid(frame, handcords[0]['mid'], handcords[1]['mid'])
                match right_hand.id:
                        case True:
                            right_hand.cords = handcords[0]
                            left_hand.cords = handcords[1]
                        case False:
                            right_hand.cords = handcords[1]
                            left_hand.cords = handcords[0]

            else:
                match len(results.multi_hand_landmarks):
                    case 1:
                        right_hand.run()
                        left_hand.run()
                    case 2:
                        right_hand.run()
                        left_hand.run()

        else:
            text_size = cv2.getTextSize("show me your hands", cv2.FONT_HERSHEY_COMPLEX, .5, 2)
            text_x = int(frame.shape[1]/2-(text_size[0][0]/2)) 
            text_y = int(frame.shape[0]/12)
            cv2.putText(frame, "Show me your hands", (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)
        #show image
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()