import tkinter as tk
from tkinter import Button,Checkbutton, Entry

window = tk.Tk()
window.title("CALCULATOR")
window.geometry("550x500")
label = tk.Label(window, text = "CALCULATOR")
label.grid()


def click_button(event=None):
    txt = button.get()
    print(txt)
    
buttons = []   
for x in range(10):
    swich = tk.IntVar()
    swich.set(x)
    button = tk.Button(window, textvariable= swich , bg= "blue", width= 5, height= 3)
    buttons.append( button)
    
for index in range(1,len(buttons)+1):
    if index <= 3:
        buttons[index].grid(row=1,  column = index+1)
    elif index <=6:
        buttons[index].grid(row=2, column = index+1-3)
    elif index <= 9:
        try:
            buttons[index].grid(row=3, column = index+1-6)
        except:
            swich 
print(len(buttons))


window.mainloop()
