from tkinter import *

from tkinter import *

root = Tk()



Frame_app = LabelFrame(text="ГЛАВНЫЙ ФРЕЙМ")
Frame_app.pack(side = TOP)

Frame_Instruction = Frame(Frame_app, width=250, height=400, bg='brown')
Frame_Instruction.pack(side = LEFT)

img_logo = PhotoImage

Frame_Recording = Frame(Frame_app, width=342, height=400, bg='blue')
Frame_Recording.pack(side = LEFT)

Frame_Handler = Frame(Frame_app, width=250, height=400, bg='red')
Frame_Handler.pack(side = LEFT)

Load_frame_app = LabelFrame()
Load_frame_app.pack(side= TOP)
label_Load = Label(Load_frame_app, width=120, height=2, bg='yellow', text="ЗАГРУЗКА")
label_Load.pack()


root.mainloop()





text = "One of the most iconic landmarks in Moscow is the Kremlin, a fortified complex that houses the offices of the President of Russia and serves as a symbol of the country’s power and strength. The Kremlin is home to several beautiful cathedrals and churches, including the famous St. Basil’s Cathedral, which is known for its colorful, onion-shaped domes. In addition to its historical and cultural attractions, Moscow is also a modern city with a vibrant nightlife and a variety of restaurants, bars, and clubs. Despite its reputation as a bustling metropolis, Moscow is also home to several beautiful parks and gardens, including the Moscow State University Botanical Garden, which is home to thousands of plant species from around the world. Moscow is a city that has something for everyone, and it is a place that is sure to leave a lasting impression on anyone who visits."
res = ""
s = 0
for elem in text:
    s+=1
    res+=elem
    if s == 50:
        s = 0
        res+= "\n"
        





root.mainloop()