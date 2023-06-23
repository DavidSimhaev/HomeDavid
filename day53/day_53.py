import tkinter as tk
from tkinter import Button, messagebox

mywindows = tk.Tk()
mywindows.title = "Название окна"
def ButoonClick():
    warning = messagebox.askquestion("Уверены?", "Продолжить?")
    if warning == "yes":
        mywindows.destroy()
button = Button(mywindows, text= "Bye!", command= ButoonClick)
button.place(x = 10, y = 10)
mywindows.mainloop()
