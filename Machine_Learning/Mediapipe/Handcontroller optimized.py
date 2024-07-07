import cv2
import mediapipe as mp
import pyautogui
import numpy as np


class Handcontroller:
    def __init__(self, handclass):
        self.handata = handclass
        self.enable = False
        self.activestartx, self.activestarty = 0,0
        self.thumbx, self.thumby = 0,0
        self.pointerx, self.pointery = 0,0
        self.middlex, self.middley = 0,0
        self.ringx, self.ringy = 0,0
        self.pinkyx, self.pinkyy =0,0
        self.handmidx, self.handmidy = 0,0
        self.dz = 25
    
    def calcangle(self):
        anglerads = np.arctan2((-1*(self.pointery-self.activestarty)),(-1*(self.pointerx-self.activestartx)))
        angledeg = np.degrees(anglerads)
        cv2.putText(frame, f"Angle: {angledeg}", (20,20), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)
        cv2.putText(frame, f"Center: {self.activestartx}, {self.activestarty}", (20,40), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)
        return angledeg
    
    def movemouse(self):
        cv2.circle(frame, (self.activestartx, self.activestarty), (self.dz), (0,0,255), 2)
        if (self.handmidx < (self.activestartx - self.dz) or self.handmidx > (self.activestartx + self.dz) or self.handmidy < (self.activestarty - self.dz) or self.handmidy > (self.activestarty + self.dz)):
            difx = (.2*(((self.activestartx-self.handmidx))/frame.shape[1]))*screenx
            dify = (.2*((-1*(self.activestarty-self.handmidy))/frame.shape[0]))*screeny
            pyautogui.move(difx, dify)
        return 0

    def updatevalues(self, image):
        self.results = self.handata.process(image)
        cv2.putText(frame, f"Enable: {self.enable}", (20,40), cv2.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 2)
        ds = 20
        if self.activestartx == 0:
            self.activestartx, self.activestarty = int(frame.shape[1] / 2), int(frame.shape[0]/2)


        #handlandmark list is not subscriptable, best work around (that I know)
        if self.results.multi_hand_landmarks:
            for singlehandlandmark in self.results.multi_hand_landmarks:
                for i, handlandmark in enumerate(singlehandlandmark.landmark):
                    #if enabled check only needed values
                    if self.enable is True:
                        #update values, assign markers
                        match i:
                            case 4:
                                self.thumbx, self.thumby = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.thumbx, self.thumby), 5, (255,0,0), -1)
                            case 8:
                                self.pointerx, self.pointery = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.pointerx, self.pointery), 5, (0,0,255), -1)
                            case 9:
                                self.handmidx, self.handmidy = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.handmidx, self.handmidy), 5, (0,0,255), -1)
                            case 12:
                                self.middlex, self.middley = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.middlex, self.middley), 5, (0,0,255), -1)
                            case 16:
                                self.ringx, self.ringy = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.ringx, self.ringy), 5, (0,0,255), -1)
                            case 20:
                                self.pinkyx,self.pinkyy = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.pinkyx, self.pinkyy), 5, (0,0,255), -1)
                        
                        
                    if self.enable is False:
                        match i:
                            case 4:
                                self.thumbx, self.thumby = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.thumbx, self.thumby), 5, (255,0,0), -1)
                            case 16:
                                self.ringx,self.ringy = int(handlandmark.x * frame.shape[1]), int(handlandmark.y * frame.shape[0])
                                cv2.circle(frame, (self.ringx, self.ringy), 5, (0,0,255), -1)

                #actions with needed info/state
                if self.enable is True:

                    cv2.line(frame, (self.activestartx, 0), (self.activestartx, frame.shape[0]), (0, 0, 255), 1)
                    cv2.line(frame, (0, self.activestarty), (frame.shape[1], self.activestarty), (0,0,255), 1)
                    self.movemouse()

                    if ((self.thumbx >= (self.pointerx-ds)) and ((self.pointerx+ds) >= self.thumbx)) and (self.thumby >= (self.pointery-ds) and (self.pointery+ds) >= self.thumby):
                        cv2.circle(frame, (self.pointerx, self.pointery), 5, (0,255,0), -1)
                        pyautogui.click(button='left')
                    elif (self.thumbx >= (self.middlex-ds) and (self.middlex+ds) >= self.thumbx) and (self.thumby >= (self.middley-ds) and (self.middley+ds) >= self.thumby):
                        cv2.circle(frame, (self.middlex, self.middley), 5, (0,255,0), -1)
                        pyautogui.click(button='right')
                    elif (self.thumbx >= (self.ringx-ds) and (self.ringx+ds) >= self.thumbx) and (self.thumby >= (self.ringy-ds) and (self.ringy+ds) >= self.thumby):
                        cv2.circle(frame, (self.ringx, self.ringy), 5, (0,255,0), -1)
                        self.activestartx, self.activestarty = self.handmidx, self.handmidy
                    elif (self.thumbx >= (self.pinkyx-ds) and (self.pinkyx+ds) >= self.thumbx) and (self.thumby >= (self.pinkyy-ds) and (self.pinkyy+ds) >= self.thumby):
                        cv2.circle(frame, (self.pinkyx, self.pinkyy), 5, (0,255,0), -1)
                        self.enable = False

                if self.enable is False:
                    if self.thumbx in range(self.ringx-ds, self.ringx+ds) and self.thumby in range(self.ringy-ds, self.ringy+ds):
                        cv2.circle(frame, (self.ringx, self.ringy), 5, (0,255,0), -1)
                        self.activestartx, self.activestarty = self.handmidx, self.handmidy
                        self.enable = True
                    
                    

                #Do not process second hand
                break




if __name__ == '__main__':

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    cap = cv2.VideoCapture(0)
    Controls = Handcontroller(hands)
    screenx, screeny = pyautogui.size()
    pyautogui.FAILSAFE = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Controls.updatevalues(image)
        cv2.imshow('Hand Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()