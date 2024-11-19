from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()
    image = filedialog.askopenfile()
    return image

def setup_gui():
    window = Tk()
    button = Button(text="Open",command=openFile)
    button.pack()
    window.mainloop()

setup_gui()