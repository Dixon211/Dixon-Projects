from tkinter import *
from tkinter.ttk import *

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("My Program")
        self.root.resizable(True, True)
        self.root.overrideredirect(True)
        
        self.create_frame()
        self.create_menu()
        
        
    def create_frame(self):
            self.root_frame = Frame(self.root)
            self.root_frame.pack(fill=BOTH, expand=True)
        
    
    
    def create_menu(self):
        def donothing():
            filewin = Toplevel(self.root_frame)
            button = Button(filewin, text="Do nothing button")
            button.pack()
            
        menubar = Frame(self.root_frame, height=30)
        menubar.pack(fill=X)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
            
        self.root_frame.config(menu=menubar)

    def run(self):
        self.root.mainloop()


window = Window()
window.run()

# need to change menu to a frame, and then modify the cascade commands