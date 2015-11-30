#this script shows how class created widgets can be added to another GUI

from tkinter import *
from tkinter102 import MyGui

#main app window
mainwin = Tk()
Label(mainwin, text=__name__).pack()

#popup window
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT) #attach frame
mainwin.mainloop()
