import tkinter as tk

class Window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hello World")
        self.window.geometry("900x500")
    
    def mainloop(self):
        self.window.mainloop()

def create_window():
    #print(tk.TkVersion)
    a = Window()
    a.mainloop()
# if __name__ == "__main__":
#     a = Window()
#     a.mainloop()
