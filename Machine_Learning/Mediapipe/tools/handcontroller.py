# controller for the machine learning model to scan for hands
import mediapipe as mp
import numpy as np
from tools.lefthand import LeftHand as lh
from framecontrol import FrameController as fc

class HandMLData:
   def __init__(self):
      #setting variables
      try:
         self.image = None
         self.handcords = [
        {'thumb':np.array([0,0,0]), 'pointer':np.array([0,0,0]), 'middle':np.array([0,0,0]), 'ring':np.array([0,0,0]), 'pinky':np.array([0,0,0]), 'mid':np.array([0,0])},
        {'thumb':np.array([0,0,0]), 'pointer':np.array([0,0,0]), 'middle':np.array([0,0,0]), 'ring':np.array([0,0,0]), 'pinky':np.array([0,0,0]), 'mid':np.array([0,0])}
        ]
         self.mphandclass = mp.solutions.hands
         self.hands = self.mphandclass.Hands()
         self.lefthand = lh
         self.framecontroller = fc

         if self.framecontroller.check == True:
             self.getframedata()
      except Exception as e:
         print(f'\nIssue in HandMLData Creation:\n{e}\n')
         quit()

   def getframedata(self):
         self.framecords = self.framecontroller.getframe()
         self.translatedata()

   #change data to readable format 
   def translatedata(self):
      try:
         results = self.hands.process(self.framecontroller.colorcorrectedframe)
         if results.multi_hand_landmarks:
            for j, singlehandlandmark in enumerate(results.multi_hand_landmarks):
                  for i, handlandmark in enumerate(singlehandlandmark.landmark):
                     match i:
                        case 4:
                              try:
                                 self.handcords[j]['thumb'] = np.array([int(handlandmark.x*self.framecontroller.framex), int(handlandmark.y*self.framecontroller.framey), int(handlandmark.z*1000)])
                              except:
                                 self.handcords[j]['thumb'] = self.np.array([None, None, None])
                        case 8:
                              try:
                                 self.handcords[j]['pointer'] = np.array([int(handlandmark.x*self.framecontroller.framex), int(handlandmark.y*self.framecontroller.framey), int(handlandmark.z*1000)])
                              except:
                                 self.handcords[j]['pointer'] = self.np.array([None, None, None])
                        case 9:
                              try:
                                 self.handcords[j]['mid'] = np.array([int(handlandmark.x*self.framecontroller.framex), int(handlandmark.y*self.framecontroller.framey)])
                              except:
                                 self.handcords[j]['mid'] = self.np.array([None, None])
                        case 12:
                              try:
                                 self.handcords[j]['middle'] = np.array([int(handlandmark.x*self.framecontroller.framex), int(handlandmark.y*self.framecontroller.framey), int(handlandmark.z*1000)])
                              except:
                                 self.handcords[j]['middle'] = self.np.array([None, None, None])
                        case 16:
                              try:
                                 self.handcords[j]['ring'] = np.array([int(handlandmark.x*self.framecontroller.framex), int(handlandmark.y*self.framecontroller.framey), int(handlandmark.z*1000)])
                              except:
                                 self.handcords[j]['ring'] = self.np.array([None, None, None])
                        case 20:
                              try:
                                 self.handcords[j]['pinky'] = np.array([int(handlandmark.x*self.framecontroller.framex), int(handlandmark.y*self.framecontroller.framey), int(handlandmark.z*1000)])
                              except:
                                 self.handcords[j]['pinky'] = self.np.array([None, None, None])
            if self.lefthand.cords == None:
                self.setinitialcords()
            
            return(0)
      except Exception as e:
          print(f'Could not translate data, check issue in HandMLData class:\n{e}\n')
          quit()

   #set initial cords for first pass
   def setinitialcords(self):
      #set variables
      try:
         text = f"Put hands in center of the squares"
         font = self.cv2.FONT_HERSHEY_COMPLEX
         fontsize = .5
         fontthickness = 2
         fontcolor = (0,0,0)
         leftboxcolor = (0,0,255)
         rightboxcolor = (0,0,255)
         leftcenter = int(self.framex*(3/4)), int(self.framey*(1/2))
         rightcenter = int(self.framex*(1/4)), int(self.framex*(1/2))
         text_size = self.cv2.getTextSize(text, font, fontsize, fontthickness)
         text_x = int(self.framex/2-(text_size[0][0]/2)) 
         text_y = int(self.framey/12)
      except Exception as e:
         print(f'Issue in HandMLData.setinitialcords() variable creation:\n{e}\n')
         quit()

      #set boxes
      try:
         self.cv2.putText(frame, text, (text_x, text_y), font, fontsize, fontcolor, fontthickness)

      except Exception as e:
          print(f'Issue in HandMLData.setinitialcord() setting center:\n{e}\n')
          quit()


   #check which handclass gets which dataset
   def seperatedata(self):
      try:
          pass
      except Exception as e:
          print(f'Issue in HandMLData.seperatedata:\n{e}\n')