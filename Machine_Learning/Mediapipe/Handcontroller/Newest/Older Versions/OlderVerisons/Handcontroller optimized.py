import cv2
import mediapipe as mp
import pyautogui
import numpy as np

class Handcontroller:
    def __init__(self, handclass):
        self.handata = handclass
        self.enable = False
        self.showimages = False
        #x,y
        self.activestart =np.array([0,0])
        self.handmid = np.array([0,0])
        #x,y,z
        self.thumbcord = np.array([0,0,0])
        self.pointercord = np.array([0,0,0])
        self.middlecord = np.array([0,0,0])
        self.ringcord = np.array([0,0,0])
        self.pinkycord = np.array([0,0,0])
        #deadzone and tip check radius
        self.dz = 25
        self.ds = 20
        #thread variable setting

    def movemouse(self):
        if np.linalg.norm(self.handmid - self.activestart) >= self.dz:
            difx = (.4*(((self.activestart[0]-self.handmid[0]))/frame.shape[1]))*screenx
            dify = (.4*((-1*(self.activestart[1]-self.handmid[1]))/frame.shape[0]))*screeny
            pyautogui.move(difx, dify)
        return 0

    def updatevalues(self, image):
        self.results = self.handata.process(image)
        cv2.putText(frame, f"Enable: {self.enable}", (20,40), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)
        if self.activestart[0] == 0:
            self.activestart[0], self.activestart[1] = int(frame.shape[1] / 2), int(frame.shape[0]/2)


        #handlandmark list is not subscriptable, best work around (that I know)
        if self.results.multi_hand_landmarks:
            for singlehandlandmark in self.results.multi_hand_landmarks:
                for i, handlandmark in enumerate(singlehandlandmark.landmark):
                    #if enabled check only needed values
                    if self.enable is True:
                        #update values, assign markers
                        match i:
                            case 4:
                                self.thumbcord[0] = int(handlandmark.x * frame.shape[1])
                                self.thumbcord[1] = int(handlandmark.y * frame.shape[0])
                                self.pointercord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.thumbcord[0], self.thumbcord[1]), 5, (0,0,255), -1)
                            case 8:
                                self.pointercord[0] = int(handlandmark.x * frame.shape[1])
                                self.pointercord[1] = int(handlandmark.y * frame.shape[0])
                                self.pointercord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.pointercord[0], self.pointercord[1]), 5, (0,0,255), -1)
                            case 9:
                                self.handmid[0] = int(handlandmark.x * frame.shape[1])
                                self.handmid[1] = int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.handmid[0], self.handmid[1]), 5, (0,0,255), -1)
                            case 12:
                                self.middlecord[0] = int(handlandmark.x * frame.shape[1])
                                self.middlecord[1] = int(handlandmark.y * frame.shape[0])
                                self.middlecord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.middlecord[0], self.middlecord[1]), 5, (0,0,255), -1)
                            case 16:
                                self.ringcord[0] = int(handlandmark.x * frame.shape[1])
                                self.ringcord[1] = int(handlandmark.y * frame.shape[0])
                                self.ringcord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.ringcord[0], self.ringcord[1]), 5, (0,0,255), -1)
                            case 20:
                                self.pinkycord[0] = int(handlandmark.x * frame.shape[1])
                                self.pinkycord[1] = int(handlandmark.y * frame.shape[0])
                                self.pinkycord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.pinkycord[0], self.pinkycord[1]), 5, (0,0,255), -1)

                    if self.enable is False:
                        match i:
                            case 4:
                                self.thumbcord[0] = int(handlandmark.x * frame.shape[1])
                                self.thumbcord[1] = int(handlandmark.y * frame.shape[0])
                                self.thumbcord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.thumbcord[0], self.thumbcord[1]), 5, (255,0,0), -1)
                            case 16:
                                self.ringcord[0] = int(handlandmark.x * frame.shape[1])
                                self.ringcord[1] = int(handlandmark.y * frame.shape[0])
                                self.ringcord[2] = int(handlandmark.z)
                                cv2.circle(frame, (self.ringcord[0], self.ringcord[1]), 5, (0,0,255), -1)

                     

                #actions with needed info/state
                if self.enable is True:

                    cv2.line(frame, (self.activestart[0], 0), (self.activestart[0], frame.shape[0]), (0, 0, 255), 1)
                    cv2.line(frame, (0, self.activestart[1]), (frame.shape[1], self.activestart[1]), (0,0,255), 1)
                    self.movemouse()

                    #Euclidian distance formula
                    if np.linalg.norm(self.thumbcord - self.pointercord) <= self.ds:
                        cv2.circle(frame, (self.pointercord[0], self.pointercord[1]), 5, (0,255,0), -1)
                        pyautogui.click(button='left')

                    elif np.linalg.norm(self.thumbcord - self.middlecord) <= self.ds:
                        cv2.circle(frame, (self.middlecord[0], self.middlecord[1]), 5, (0,255,0), -1)
                        pyautogui.click(button='right')

                    elif np.linalg.norm(self.thumbcord - self.ringcord) <= self.ds:
                        cv2.circle(frame, (self.ringcord[0], self.ringcord[1]), 5, (0,255,0), -1)
                        self.activestart[0], self.activestart[1] = self.handmid[0], self.handmid[1]

                    elif np.linalg.norm(self.thumbcord - self.pinkycord) <= self.ds:
                        cv2.circle(frame, (self.pinkycord[0], self.pinkycord[1]), 5, (0,255,0), -1)
                        pyautogui.click(button='right')
                        self.enable = False


                if self.enable is False:
                    if np.linalg.norm(self.thumbcord - self.ringcord) <= self.ds:
                        cv2.circle(frame, (self.ringcord[0], self.ringcord[1]), 5, (0,255,0), -1)
                        self.activestart[0], self.activestart[1] = self.handmid[0], self.handmid[1]
                        self.enable = True
                        
                    
                    

                #Do not process second hand
                break




if __name__ == '__main__':
    # load machine learning model
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    #accessing camera
    cap = cv2.VideoCapture(0)
    #creating hands
    Controls = Handcontroller(hands)
    #getting screen size
    screenx, screeny = pyautogui.size()
    pyautogui.FAILSAFE = False


    



    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        framex, framey = frame.shape[1], frame.shape[0]
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Controls.updatevalues(image)
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()