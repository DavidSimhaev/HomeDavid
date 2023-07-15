from check_width_and_height import Image_ch
import os
import glob
import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk ,Button ,Checkbutton , Entry, Frame, W, E, PhotoImage, Text, IntVar, Menu, filedialog, messagebox, END
from tkinter.ttk import Style
import tkinter.font as tkFont
res = 0
First= True
end = False
counter = 0
b = 3
q = 3
class Example(Frame):
    def __init__(self):
        super().__init__()
        
        self.FILES_LIST = []
        self.image = None       
        self.sub = None         
        self.photo = PhotoImage(file = "day56/image/user.png")
        self.subsise = self.photo.subsample(5, 5)
        self.icon_del = PhotoImage(file = "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/975968.png")
        self.sub_icon_del = self.icon_del.subsample(25, 25)
        self.editing_icon = PhotoImage(file = "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/950768.png")
        self.sub_editing = self.editing_icon.subsample(25,25)
        self.icon_sell = PhotoImage(file= "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/1778661.png")
        self.sub_sell = self.icon_sell.subsample(25,25)
        
        self.dict = {}
        
        
        self.seacrh_photo = PhotoImage(file = r"day56/image/search_2.png")
        self.subsise_seatch = self.seacrh_photo.subsample(50,50)
        
        
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
        
        self.label = tk.Label(self, text = "Photo-Recognition",background="yellow" , font = "Haettenschweiler 50" )
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
            
            
            Label_pr = tk.Label(self, text = "Your projects" , font= "@yugothic 20 bold ") # При нажатие выдасть диологовое окно и загрузить проект
            Label_pr.grid(row= 2 , columnspan= 5, pady= 8)
            
            if glob.glob("C:/Users/ASUS/Desktop/HomeWorkDavid/day56/projects*/*.txt") == []:
                label_str = tk.Label(self, text = "You don't have any active projects at the moment.", font="@yugothic 11 ")
                label_str.grid(row= 3 , columnspan= 5)
                label_str2 = tk.Label(self, text = "Log in to the 'files' tab and upload the recordings,", font="@yugothic 11 ")
                label_str2.grid(row= 4 , columnspan= 5)
                label_str2 = tk.Label(self, text = "and save the result.", font="@yugothic 11 ")
                label_str2.grid(row= 5 , columnspan= 5)
            else:
                b = 0
                
                def on_label_enter(e):
                    e.widget['background'] = 'gray50'

                def on_label_leave(e):
                    e.widget['background'] = 'SystemButtonFace'

                def on_enter(e):
                    e.widget['background'] = 'blue'
                            
                def on_leave(e):
                    e.widget['background'] = 'SystemButtonFace'
                            
                        
                def on_enter2(e):
                    e.widget['background'] = 'green'
                            
                def on_leave2(e):
                    e.widget['background'] = 'SystemButtonFace'
                    
                    
                def on_enter3(e):
                    e.widget['background'] = 'red'
                            
                def on_leave3(e):
                    e.widget['background'] = 'SystemButtonFace'
                    
                def rename_pr(event, file_pr):
                    
                    def change_name(event):
                        answer = messagebox.askyesno(message="Are you sure you want to change the name of the project?")
                        if answer:
                            b = 0
                            for el in str(file_pr["elem"]["textvariable"])[::-1]:
                                b+=1
                                if el == "/": 
                                    os.rename(file_pr["elem"]["textvariable"],file_pr["elem"]["textvariable"][:-b]+"/"+rename.get()+".txt")
                                    self.Button_projects.invoke()
                                    w.destroy()
                                    break
                                    
                        else:
                            
                            w.destroy()
                            
                        
                            
                    w = tk.Tk()              
                    w.geometry("150x40")      
                    print(file_pr["elem"]["textvariable"])
                    rename = tk.Entry(w, font= 50)
                    rename.delete(0,END)
                    rename.insert(0,file_pr["elem"]["text"])    
                    rename.place(width=150, height=40)
                    
                    
                    rename.bind("<Return>",change_name)
                    
                    #os.rename(file_pr["elem"]["textvariable"], rename["text"])
                
                
                
                
                
                def on_click_ed(event, file_pr):
                    if self.FILES_LIST != []:
                        answer = messagebox.askyesno(title="Open another project",message="The program at the development stage and allows you to conduct only one project, in cases of opening another project, the current one will reset, are you sure?")
                        if answer:
                            self.FILES_LIST =[]    
                            file = open(str(file_pr["elem"]["textvariable"]), "r", encoding= "utf-8")
                            s = file.read()
                            s = s.split("\n")
                            s = s[:-1:]
                            for el in s:
                                self.FILES_LIST.append(el)
                            self.Button_files.invoke()
                        else:
                            return
                    else:
                        file = open(str(file_pr["elem"]["textvariable"]), "r", encoding= "utf-8")
                        s = file.read()
                        s = s.split("\n")
                        s = s[:-1:]
                        for el in s:
                            self.FILES_LIST.append(el)
                        self.Button_files.invoke()
                
                def delete_pr(event, file_pr):
                    
                    answer = messagebox.askyesno(title="Remove the Project",message="Do you want to delete this project?")
                    if answer: 
                        os.remove(str(file_pr["elem"]["textvariable"]))
                        file_pr["elem"].destroy()
                        file_pr["self"].Button_projects.invoke()
                        messagebox.showinfo(title="Project deleted", message="This project was deleted successfully")
                    else:
                        return
                
                
                    
                for file_project in glob.glob("C:/Users/ASUS/Desktop/HomeWorkDavid/day56/projects*/*.txt"):
                    global q
                    if q % 2: # Четное
                        q+=2
                    else:
                        q+=1 
                    
                    
                    file_project = file_project.replace("\\", "/")
                    index = 0
                    
                    for i in file_project[::-1]:
                        index +=1 
                        if i == "/":
                            if len(file_project[-index::]) > 15:
                                label_file = tk.Label(self, textvariable= file_project, text = f"{file_project[-(index-1):-abs(index-14):]}.." ,font = "@yugothic 15")
                                
                                break
                            else:
                                label_file = tk.Label(self,  textvariable= file_project ,text = f"{file_project[-(index-1):-4:]}" ,font = "@yugothic 15")
                                
                                break
                        
                    
                    
                    label_file.grid(row = q, column= 0 , columnspan= 2)
                    
                    Label_sell1 = tk.Label(self, image = self.sub_sell)
                    Label_sell1.grid(row = q , column= 2, pady = 10)
                    
                    label_editing2 = tk.Label(self, image = self.sub_editing)
                    label_editing2.grid(row= q, column= 3, pady = 10 )
                    
                    Label_del = tk.Label(self,image= self.sub_icon_del)
                    Label_del.grid(row = q, column= 4, pady= 10 ,sticky= "s")
                    
                    canv = tk.Canvas(self, bg= "gray", height= 2, width=350)
                    canv.grid(row = q+1, columnspan= 5, pady= 4)
                    
                    
                    
                    
                    data={"elem":label_file, "self": self }
                        
                    
                    label_file.bind("<Enter>", on_label_enter)
                    label_file.bind("<Leave>", on_label_leave)
                    label_file.bind("<Button-1>", lambda event, arg=data: rename_pr(event, arg))          
                    
                    
                    Label_sell1.bind("<Enter>", on_enter)
                    Label_sell1.bind("<Leave>", on_leave)
                              

                    label_editing2.bind("<Enter>", on_enter2)
                    label_editing2.bind("<Leave>", on_leave2)
                    label_editing2.bind("<Button-1>", lambda event, arg=data: on_click_ed(event, arg))
                    
                        
                    Label_del.bind("<Enter>", on_enter3)
                    Label_del.bind("<Leave>", on_leave3)
                    
                    Label_del.bind("<Button-1>", lambda event, arg=data: delete_pr(event, arg))
                    
                          
        
        
        
        self.Button_projects = Button(self, text= "Projects", bg= "yellow", font="Haettenschweiler 20", command= all_projects)
        self.Button_projects.grid(row=1, column=1)
        
        
        def func_files():
            
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            
            
            label_w = tk.Label(self, text = "Files in your project", font= "@yugothic 13 bold")
            label_w.grid(row = 2, column= 0 , columnspan= 2)
            
            entry_search = Entry(self, width= "25")
            entry_search.grid(row = 2, column=2 , columnspan= 3 , ipady=10, sticky = "w")
            
            
            button_search = Button(self, image= self.subsise_seatch)
            button_search.grid(row = 2 , column= 4, pady= 20, sticky = "e" )
            
            def f():
                if self.FILES_LIST == []:
                    return        
                else:
                    def on_enter(e):
                        e.widget['background'] = 'gray'
                        
                    def on_leave(e):
                        
                        e.widget['background'] = 'SystemButtonFace'
                        
                    
                    def on_enter2(e):
                        e.widget['background'] = 'LimeGreen'
                        
                    def on_leave2(e):
                        
                        e.widget['background'] = 'SystemButtonFace'
                        
                    
                    
                    def on_enter3(e):
                        e.widget['background'] = 'red'
                        
                    def on_leave3(e):
                        e.widget['background'] = 'SystemButtonFace'
                        
                    def on_click_del_file(event, arg):
                        for index in range(len(self.FILES_LIST)):
                            if self.FILES_LIST[index] == arg["elem"]:
                                self.FILES_LIST.remove(self.FILES_LIST[index])
                                break
                        self.Button_files.invoke()
                    
                    def func_c(event, arg):
                        w = tk.Toplevel(self)
                        
                        arg["self"].image = PhotoImage(file = arg["elem"])

                        label_img = tk.Label(w, image=arg["self"].image).pack()
                    
                    
                    for elem in self.FILES_LIST:
                        global b
                        if b % 2: # Четное
                            b+=2
                        else:
                            b+=1    
                        index_start = 0
                        for elem_symbov in elem[::-1]: 
                            index_start +=1
                            if elem_symbov  == "/":
                                break
                        
                        if len(elem[-index_start::]) > 12:
                            Label_str = tk.Label(self,textvariable= elem, text = f"{elem[-(index_start-1):-(index_start-11):]}..{elem[-4::]}", font= "@yugothic 15", fg = "black")
                            
                        else:
                            Label_str = tk.Label(self, textvariable= elem, text = f"{elem[-(index_start-1)::]}", font= "@yugothic 15", fg = "black")
                                
                                    
                        
                        Label_str.grid(row = b, column=0, columnspan= 2 , pady= 3)
                        Label_str2 = tk.Label(self, text= "recognize text" , font= "@yugothic 15")
                        Label_str2.grid(row = b, column= 2, columnspan= 2 , pady= 3,sticky= "w")
                        
                        Label_str3 = tk.Label(self, image= self.sub_icon_del)
                        Label_str3.grid(row = b, column= 4, pady= 10 ,sticky= "s")
                        
                        canv = tk.Canvas(self, bg= "gray", height= 2, width=350)
                        canv.grid(row = b+1, columnspan= 5, pady= 4)
                            
                        data={"self": self, "elem": elem, }
                        
                        Label_str.bind("<Button-1>", lambda event, arg=data: func_c(event, arg))
                        
                        Label_str.bind("<Enter>", on_enter)
                        Label_str.bind("<Leave>", on_leave)
                        
                        Label_str2.bind("<Enter>", on_enter2)
                        Label_str2.bind("<Leave>", on_leave2)
                        
                        
                        Label_str3.bind("<Enter>", on_enter3)
                        Label_str3.bind("<Leave>", on_leave3)
                        Label_str3.bind("<Button-1>", lambda event, arg=data: on_click_del_file(event, arg))

                    for key in self.dict:
                        print(self.dict[key])
            
            f()

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
                
                    files = [
                                ('Text Document', '*.txt'),]
                    try:
                        file = filedialog.asksaveasfile(filetypes = files, defaultextension = files,initialdir= "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/projects")
                    except AttributeError:
                        return
                    write_res_to_file = open(file.name, "w", encoding= "utf-8")
                    
                    
                    for el in self.FILES_LIST:
                        write_res_to_file.write(f"{str(el)}\n")
                    
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
    window.iconbitmap("C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image/photo_photography_picture_camera_summer_icon_251688.ico")
    mainmenu = Menu(window)
    window.config(menu= mainmenu)
    
    file_menu = Menu(mainmenu, tearoff= 0)
    
    def open_file():
        files = [('PNG', '*.png'),('JPG', '*.jpg')]
        
        try:
            name = filedialog.askopenfilename(filetypes = files, defaultextension = files, initialdir= "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/image" )
        except AttributeError:
            return
        if name == "":
            return
        
        save_image = Image_ch(name).save()
        
        app.FILES_LIST.append(save_image)
        print(app.FILES_LIST)
        app.Button_files.invoke() # ИНВОК ЗАПУСКАЕТ ВИДЖЕТ БЕЗ КЛИКА!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
            
        
    def save_project():
        name = filedialog.asksaveasfile(initialdir= "C:/Users/ASUS/Desktop/HomeWorkDavid/day56/projects")
        
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
        