import time
import tkinter as tk
from tkinter import Button ,Checkbutton , Entry, Frame, W, E, PhotoImage
from tkinter.ttk import Style
import tkinter.font as tkFont

res = 0
First= True
end = False
counter = 0
class Example(Frame):
    def __init__(self):
        super().__init__()
        self.func()
        
    def func(self):
        self.master.title("MBook")
        self.photo = PhotoImage(file = r"day56/user.png")
        self.subsise = self.photo.subsample(5, 5)
        
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        
        
        label = tk.Label(self, text = "Message Book",background="yellow" , font = "Haettenschweiler 50" )
        label.grid(row= 0, columnspan= 5, sticky= W+E)
        
        def main_p():
             
            button_image_acc = Button(self, image= self.subsise)
            button_image_acc.grid(row = 2 , columnspan = 3, pady= 20 )
            
            label_name = tk.Label(self, text = "Name", font="Haettenschweiler 20")
            label_name.grid(row = 2, column= 3)
            biography = tk.Label(self, text = "Biography", font="Haettenschweiler 30")
            biography.grid(row = 3, columnspan= 5)
            ####
            def check_text(text):
                
                global counter
                global First
                counter +=57
                try:
                    if First:
                        First = False
                        result = text[counter] 
                        c = 0
                        while result != " ":
                            c += 1
                            result = text[counter-c]
                        counter -= c 
                        return text[0:counter]            
                    else:
                        result = text[counter]
                        c = 0
                        while result != " ":
                            c+=1
                            result = text[counter-c]
                        counter -= c
                        return text[counter-57+c:counter]
                         
                except:
                    global end
                    end = True
                    return text[counter::]
                                    
                            
                
            row_x = 3    
            text_ch = "Charles Spencer Chaplin was an English actor, director, and writer who was one of the most famous figures in the history of film. Born in 1889, Chaplin began his career as a performer in British vaudeville and music hall before moving to Hollywood in 1913. Chaplin is best known for his work as a silent film actor, in which he starred in a series of classic comedies featuring his most famous character, the «Tramp.» The Tramp, a lovable and resourceful character with a distinctive appearance (including a small mustache and bowler hat), appeared in many of Chaplin’s films, including «The Kid,» «The Gold Rush,» and «Modern Times.» Chaplin was a pioneer in the film industry and was known for his innovative use of film techniques and storytelling. He wrote, directed, and produced many of his own films and was a key figure in the development of the Hollywood studio system. Chaplin continued to act and make films until the 1950s and received numerous awards and accolades throughout his career. He died in 1977 at the age of 88."
            
            while True:
                row_x +=1
                characteristic_text = tk.Label(self, text = check_text(text_ch), font="GothicLight 10")
                print(characteristic_text["text"])
                print(len(characteristic_text["text"]))
                characteristic_text.grid(row = row_x, columnspan= 5)
                
                global end
                
                if end == True:
                    break
            global counter
            counter = 0
            ####
        Button_page = tk.Button(self, text = "Main Page", bg= "yellow", font="Haettenschweiler 20", command= main_p)
        Button_page.grid(row=1, column=0)
        
        Button_message = Button(self, text= "Message", bg= "yellow", font="Haettenschweiler 20")
        Button_message.grid(row=1, column=1)
        
        
        Button_music = Button(self, text= "Music", bg= "yellow", font="Haettenschweiler 20")
        Button_music.grid(row=1, column=2)
        
        Button_support = Button(self, text= "Support", bg= "yellow", font="Haettenschweiler 20")
        Button_support.grid(row=1, column=3)
        
        def exit():
            self.master.destroy()
        
        button_exit = Button(self, text= "Exit", bg= "red", font="Haettenschweiler 20", command=exit)
        button_exit.grid(row=1, column=4)
        
        
        self.pack()
        
def main():
    window = tk.Tk()
    app = Example()
    window.geometry("414x736")
    window.mainloop()

if __name__ == '__main__':
    main()
        