from PIL import Image
import numpy as np
import tkinter as tk

# def 
# Window = tk.Tk()
# Window.title("Picture viewer")
# Window.geometry("400x300")
# Window.geometry("1800x900")

class Windowsettings:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")
        self.root.geometry("400x300")

    def run(self):
        self.root

def main():
    root = tk.Tk()
    app = Windowsettings(root)
    app.run()

#Main
if __name__ =="__main__":
    main()
    # img = np.asarray(Image.open("./stinkbug.png"))

