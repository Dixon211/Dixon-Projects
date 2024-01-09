import tkinter as tk
import cv2
from PIL import Image, ImageTk

class VideoCapture:
    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        if not self.vid.isOpened():
            print ("Failed to open Video")
        
    
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_copy = frame.copy()
            height, width, _ = frame.shape
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


        
            
            frame = cv2.addWeighted(frame_copy, .5, frame, 1, 0)
            if ret:
                return(ret, frame, width, height)
            else:
                return(None)
        else:
            return(None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


class Librarian:
    def __init__(self):
        #window
        self.window= tk.Tk()
        self.window.title("Librarian")

        #video_canvas
        self.video_canvas = tk.Canvas(self.window)
        self.video_canvas.grid(column=0, row=0, rowspan=2, sticky="nesw")

        #button
        self.scan_btn= tk.Button(self.window, width =75, height = 5, text="Click Me")
        self.scan_btn.grid(column = 1, row= 1, sticky="s")

        #frame
        self.info_frame= tk.Frame(self.window)
        self.info_frame.grid(column=1, row=0)

        self.video_capture = VideoCapture()

        self.update_canvas()

        self.window.mainloop()

    def update_canvas(self):
        ret, frame, v_width, v_height = self.video_capture.get_frame()
        if ret:
            self.video_canvas.config(width=v_width, height=v_height)
            self.frame = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.video_canvas.create_image(0,0, image = self.frame, anchor = "nw")

        self.window.after(10, self.update_canvas)
        

    def __del__(self):
        if self.video_capture.isOpened():
            self.video_capture.__del__()

app = Librarian()