import tkinter as tk


root = tk.Tk()
root.resizable(True, True)
root.overrideredirect(True)
root.bind("<Escape>", lambda x: root.destroy())
root.mainloop()
