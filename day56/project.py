import glob
import time
import tkinter as tk
from tkinter import ttk ,Button ,Checkbutton , Entry, Frame, W, E, PhotoImage, Text, IntVar, Menu, filedialog, messagebox
from tkinter.ttk import Style
import tkinter.font as tkFont
res = 0
First= True
end = False
counter = 0

class Example(Frame):
    def __init__(self):
        super().__init__()
        
        self.FILES_LIST = []
                
        self.photo = PhotoImage(file = "day56/user.png")
        self.subsise = self.photo.subsample(5, 5)
        
        
        
        self.seacrh_photo = PhotoImage(file = r"day56/search_2.png")
        self.subsise_seatch = self.seacrh_photo.subsample(50,50)
        
        self.url_img = PhotoImage()
        self.subsise_img = self.url_img.subsample(5,5)
        self.func()          
        
    def func(self):
        self.master.title("MBook")
        
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
        
        self.label = tk.Label(self, text = "Photo recognition",background="yellow" , font = "Haettenschweiler 50" )
        self.label.grid(row= 0, columnspan= 5, sticky= W+E)
        
        
        def main_p():
            
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
    
            button_image_acc = Button(self, image= self.subsise )
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
                characteristic_text.grid(row = row_x, columnspan= 5)
                global end
                if end == True:
                    break
            global counter
            end = False
            counter = 0
                    ####
            
        
        self.Button_page = tk.Button(self,  text = "Main Page", bg= "yellow"  ,font="Haettenschweiler 20", command= main_p)
        self.Button_page.grid(row=1, column=0)
        
        def all_projects():
            
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            
            
            Label_pr = tk.Label(self, text = "Your projects" , fg= "gray", font= "Haettenschweiler 25")
            Label_pr.grid(row= 2 , columnspan= 5, pady= 8)
            if glob.glob("C:/Users/ASUS/Desktop/HomeWorkDavid/day56/projects*/*.py") == []:
                return
            else:
                b = 0
                for file in glob.glob("C:/Users/ASUS/Desktop/HomeWorkDavid/day56/projects*/*.py"):
                    b+=1
                    label_file = tk.Label(self, text = f"Project: {file[-8::]}", bg= "gray" ,font = 10)
                    label_file.grid(row = 3+b, columnspan= 2)
        
        self.Button_projects = Button(self, text= "Projects", bg= "yellow", font="Haettenschweiler 20", command= all_projects)
        self.Button_projects.grid(row=1, column=1)
        
        
        
        
        
        
        def func_files():
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            
            entry_search = Entry(self, width= "40")
            entry_search.grid(row = 2, columnspan= 4, ipady=10)
            
            
            button_search = Button(self, image= self.subsise_seatch)
            button_search.grid(row = 2 , column= 3, pady= 20, sticky = "e" )
         
            if self.FILES_LIST == []:
                return        
            else:
                b = 0
                for file_name in self.FILES_LIST:
                    b += 1
                    label_f = tk.Label(self, text= f"FILE {b}: {file_name[-8:-4:]}", bg= "gray" ,font = 10 )   
                    label_f.grid(row= 2+b, columnspan= 2) 
                    ###############################################
        
                    ###############################################
                
                
        self.Button_files = Button(self, text= "Files", bg= "yellow", font="Haettenschweiler 20",command= func_files)
        self.Button_files.grid(row=1, column=2)
        
        self.Button_support = Button(self, text= "Support", bg= "yellow", font="Haettenschweiler 20")
        self.Button_support.grid(row=1, column=3)
        
        def exit():
            if self.FILES_LIST == []:
                self.master.destroy()
            else:
                answer = messagebox.askyesno(title="question?", message= "Do you want to save the result?")
                if answer:
                
                    files = [('All Files', '*.*'),
                                ('Python Files', '*.py'),
                                ('Text Document', '*.txt')]
                            
                    file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
                    write_res_to_file = open(file.name, "w", encoding= "utf-8")
                    write_res_to_file.write("res ="+ str(self.FILES_LIST) )
                    write_res_to_file.close()
                    self.master.destroy()
                else:
                    self.master.destroy()
        
        self.button_exit = Button(self, text= "Exit", bg= "red", font="Haettenschweiler 20", command=exit)
        self.button_exit.grid(row=1, column=4)
                
        
        self.pack() #<<<<<<<<<<< Запомнить
        
        

def main():
    
    window = tk.Tk()
    app = Example()
    window.geometry("414x736")
    mainmenu = Menu(window)
    window.config(menu= mainmenu)
    
    file_menu = Menu(mainmenu, tearoff= 0)
    
    def open_file():
        files = [('PNG', '*.png'),('JPG', '*.jpg')]
        
        name = filedialog.askopenfilename(filetypes = files, defaultextension = files)
        if name == "":
            return
        
        
        
        app.FILES_LIST.append(name)
        print(app.FILES_LIST)
        app.Button_files.invoke() # ИНВОК ЗАПУСКАЕТ ВИДЖЕТ БЕЗ КЛИКА!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
            
        
    def save_project():
        name = filedialog.asksaveasfile()
        
    file_menu2 = Menu(file_menu, tearoff= 0)
    file_menu2.add_command(label="Work1")
    file_menu2.add_command(label="Work2")
    
    file_menu.add_command(label="Open File", command= open_file)
    file_menu.add_command(label="Save File", command= save_project)
    file_menu.add_cascade(label="Open Recent", menu= file_menu2)
    
    
    mainmenu.add_cascade(label= "File", menu= file_menu )
    
    mainmenu.add_cascade(label= "Settings")
        
    window.mainloop()

if __name__ == '__main__': # Не понял
    main()
        