import tkinter as tk
from tk import *
import camera_feed as cf

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hello World")
        self.window.geometry("900x500")

    def display_video(self):
        print("creating label")
        panel = Label(self.window, image=a)
        panel.pack()
        a = cf.get_video_feed()
        
    
    def mainloop(self):
        self.window.mainloop()

  

def create_window():
    #print(tk.TkVersion)
    a = Window()
    Window.display_video()
    a.mainloop()


# if __name__ == "__main__":
#     a = Window()
#     a.mainloop()

create_window()