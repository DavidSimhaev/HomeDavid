from tkinter import *
import os
window=Tk()
window.geometry('300x300')

def update():
 window.destroy()
 os.system('test.py')
Button(window,text="Refresh",command=update).pack()
window.mainloop()