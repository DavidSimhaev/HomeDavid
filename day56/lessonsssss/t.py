from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
def single_click(event): 
    btn["text"] ="Single Click"
 
def double_click(event): 
    btn["text"] ="Double Click"
 
btn = ttk.Button(text="Click")
btn.pack(anchor=CENTER, expand=1)
 
btn.bind("<ButtonPress-1>", single_click)
btn.bind("<Double-ButtonPress-1>", double_click)
 
root.mainloop()