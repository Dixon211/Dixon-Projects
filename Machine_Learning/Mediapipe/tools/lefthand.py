class LeftHand:
    def __init__(self):
        #
        try:
            import pyautogui
            self.pygi = pyautogui
        except:
            print('Couldnt import modules for LeftHand class')
        try:
            self.cords = None
        except:
            print('couldnt create variables for LeftHand class')
    def set(self, cords):
        self.cords = cords
        print('cords received\n')
