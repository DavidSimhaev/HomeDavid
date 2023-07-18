
Images = iter(['C:/Users/ASUS/Desktop/HomeWorkDavid/day56/user2.png', 'C:/Users/ASUS/Desktop/HomeWorkDavid/day56/search_2.png', 'C:/Users/ASUS/Desktop/HomeWorkDavid/day56/user.png'])
from tkinter import filedialog
import tkinter as tk

import os
filedialog
# Create empty list for coordinate arrays to be appended to
coords = []

# Function to be called when mouse is clicked
def save_coords(event):
    click_loc = [event.x, event.y]
    print ("you clicked on", click_loc)
    coords.append(click_loc)

# Function to load the next image into the Label
def next_img():
    img_label.img = tk.PhotoImage(file=next(imgs))
    img_label.config(image=img_label.img)

root = tk.Tk()

# Choose multiple images
img_dir = filedialog.askdirectory(parent=root, initialdir="C:/Users/ASUS/Desktop/", title='Choose folder')
print(img_dir)
os.chdir(img_dir)
imgs = iter(os.listdir(img_dir))

img_label = tk.Label(root, width= 500, height= 500)
img_label.pack()
img_label.bind("<Button-1>",save_coords)

btn = tk.Button(root, text='Next image', command=next_img)
btn.pack()

next_img() # load first image

root.mainloop()
