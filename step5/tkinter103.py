'''
This script shows how to get input data from the user in an Entry widget
and display it in a pop-up dialog.
The lamda used in the script defers the call of the reply function so that
further inputs can be passed in.
The script also demonstrates how to change the icon and the title of the
top-level window (though this can be notoriously platform specific).
'''

from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')
#top.iconbitmap('py-blue-trans-out.ico')

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()
