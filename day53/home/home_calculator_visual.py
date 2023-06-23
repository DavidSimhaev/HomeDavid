import tkinter as tk
from tkinter import Button,Checkbutton, Entry
from solver import solve
window = tk.Tk()
window.title("CALCULATOR")
window.geometry("550x500")
label = tk.Label(window, text = "CALCULATOR")
label.grid()
res = ""
index_int = 0
def click_button(number):
    global res 
    global index_int 
    index_int +=1
    entry = Entry(window, background="yellow", font="TkHeadingFont" )
    entry.place( relx=0.325, rely=0.5, anchor="c", width=200, height=40)
    if number == "-" or number == "+" or number == "*"  or number == "/" or number == "c" or number == "=":
        try:
            if number == "+":
                if res[-1] not in "+-/*":
                    res += "+"
            elif number == "-":
                if res[-1] not in "+-/*":
                    res += "-"
            elif number == "*":
                if res[-1] not in "+-/*":
                    res += "*"
            elif number == "/":
                if res[-1] not in "+-/*":
                    res += "/"
            elif number == "c":
                res= ""
            elif number == "=":
                res= solve(res)
                entry.insert(0, res)
                return    
        except:
            pass
        entry.insert(0, res)
        return
    
    res +=str(number)
    print(res)
    entry.insert(0, res)
buttons = []   
for x in range(10):
    swich = tk.IntVar()
    swich.set(x)
    button = tk.Button(window, textvariable= swich , bg= "blue", fg= "white", width= 5, height= 3, text=x, command=lambda x=x: click_button(x))
    button.focus_set()
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
            pass
        button_minus = tk.Button(window, textvariable= "-" , bg= "yellow", width= 5, height= 3, text="-", command=lambda x=x:click_button("-"))
        button_minus.grid(row=3, column=5)
        button_plus = tk.Button(window, textvariable= "+" , bg= "yellow", width= 5, height= 3, text="+", command=lambda x=x: click_button("+"))
        button_plus.grid(row=4, column=5)
        button_c = tk.Button(window, textvariable= "*" , bg= "yellow", width= 5, height= 3, text="*", command=lambda x=x: click_button("*"))
        button_c.grid(row=1, column=5)
        button_des = tk.Button(window, textvariable= "/" , bg= "yellow", width= 5, height= 3, text="/", command=lambda x=x: click_button("/"))
        button_des.grid(row=2, column=5)
        button_rovno = tk.Button(window, textvariable= "=" , bg= "yellow", width= 5, height= 3, text="=", command=lambda x=x: click_button("="))
        button_rovno.grid(row=4,column=4)
        button_clear = tk.Button(window, textvariable= "c" , bg= "yellow", width= 5, height= 3, text="c", command=lambda x=x: click_button("c"))
        button_clear.grid(row=4,column=3)
        button_space = tk.Button(window, textvariable= " " , bg= "yellow", width= 5, height= 3, text=" ", command=lambda x=x: click_button(" "))
        button_space.grid(row=4,column=2)
res.split("+")
print(res)
window.mainloop()
