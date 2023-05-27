from tkinter import *

def donothing():
    x+=0

#create the root window
root = Tk()
root.resizable(True, True)
root.bind("<Escape>", lambda x: root.destroy())
root.configure(bg='blue')
root.geometry('1000x800')
root.overrideredirect(True)

#create the top frame
top_frame = Frame(root, bg = "gray", height=30)
top_frame.grid( row = '0', column = '0', sticky="nsew")

top_menu = Menu(top_frame)
top_filemenu=Menu(top_menu, tearoff=0)
top_filemenu.add_command(label="New", command=donothing)
top_filemenu.add_command(label='Open', command=donothing)
top_filemenu.add_command(label='Save', command=donothing)
top_filemenu.add_separator()
top_filemenu.add_command(label='Exit', command=root.destroy)
top_menu.add_cascade(label="File", menu=top_filemenu)
root.config(menu=top_menu)




root.mainloop()