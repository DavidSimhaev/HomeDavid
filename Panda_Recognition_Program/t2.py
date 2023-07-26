import tkinter as tk
import os

root = tk.Tk()
root.title('background image')
root["bg"] = "black"
local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
img_logo = tk.PhotoImage(file = rf"{local_url}/image/user.png" ).subsample(2,2)

# get the image size
w = img_logo.width()
h = img_logo.height()

# make the root window the size of the image
root.geometry("%dx%d" % (w, h))

# root has no image argument, so use a label as a panel
panel1 = tk.Label(root, image=img_logo)
panel1.pack(side='top', fill='both', expand='yes')

# put a button/label on the image panel to test it
label1 = tk.Label(panel1, text='here i am')
label1.pack(side=tk.TOP)

button2 = tk.Button(panel1, text='button2')
button2.pack(side=tk.TOP)
root["bg"] = "black"
# start the event loop
root.mainloop()