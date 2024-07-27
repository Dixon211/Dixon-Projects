import cv2


class FrameController:
    def __init__(self):
        try:
            #set variables
            self.frame = None
            self.colorcorrectedframe = None
            self.framex = None
            self.framey = None
            self.capture = cv2.VideoCapture(0)
            self.check = self.capture.isOpened()
        except Exception as e:
            print(f'\nIssue in FrameController.init:\n{e}\n')

    #update class values
    def readframe(self) -> None:
        try:
            _, self.frame = self.capture.read()
            self.colorcorrectedframe = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            self.framex = self.frame.shape[1]
            self.framey = self.frame.shape[0]
            cv2.imshow('this thing',self.frame)
        except Exception as e:
            print(f'\nIssue in Framecontroller.run:\n{e}\n')
            self.close()

    #add objects to frame
    def setobject(self, templatedict) -> None:
        try:
           for name, templateobj in templatedict.items():
                match name:
                    case '0':
                        cv2.circle(self.frame, (int(templateobj[0][0][0]*self.framex),int(templateobj[0][0][1]*self.framey)), 2, (int(templateobj[0][1][0]), int(templateobj[0][1][1]), int(templateobj[0][1][2])), -1)
                        print('circle created')
                    case 'text':
                        cv2.addText()
            
        except Exception as e:
            print(f'\nIssue in Framecontroller.setobject:\n{e}\n')
        cv2.imshow('window', self.frame)
    #show frame, duh
    def show(self):
        try:
           # print('entered in show')
            #cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
            #cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow('this thing',self.frame)
        except Exception as e:
            print(f'\nIssue in FrameController.show:\n{e}\n')
            self.close()

    def close(self):
        cv2.destroyAllWindows()