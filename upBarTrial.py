#Import the tkinter library
from tkinter import *

def grid_hide(widget):
    widget._grid_info = widget.grid_info()
    widget.grid_remove()


def grid_show(widget):
    widget.grid(**widget._grid_info)

#Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

#Create a Label to print the Name
label= Label(win, text="This is a New Line Text", font= ('Helvetica 14 bold'), foreground= "red3")
label.pack()

win.wm_attributes('-fullscreen', 'False')
win.wm_attributes('-topmost', 'True')
win.mainloop()