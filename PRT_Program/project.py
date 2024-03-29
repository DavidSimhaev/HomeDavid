import shutil
import threading
from frame_easyocr import Recording_text
from check_width_and_height import Image_ch
import os
import glob
import tkinter as tk
from tkinter import Button, Frame, W, E, PhotoImage, Menu, filedialog, messagebox, END
from tkinter.ttk import Style
import time
res = 0
First= True
end = False
counter = 0
b = 3
q = 0
count_threads=0

class Example(Frame):
    def __init__(self):
        super().__init__()
        
        self.local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
        self.FILES_LIST = []
        self.running = True
        self.image = None       
        self.sub = None         
        self.load = None
        self.support_1 = PhotoImage(file = rf"{self.local_url}/support_img/1.png" )
        self.support_2 = PhotoImage(file = rf"{self.local_url}/support_img/2.png")
        self.support_3 = PhotoImage(file = rf"{self.local_url}/support_img/3.png").subsample(2,2)
        self.support_4 = PhotoImage(file = rf"{self.local_url}/support_img/4.png")
        self.support_6 = PhotoImage(file = rf"{self.local_url}/support_img/6.png")
        
        self.photo = PhotoImage(file = rf"{self.local_url}/image/user.png")
        self.subsise = self.photo.subsample(5, 5)                      
        self.icon_del = PhotoImage(file = rf"{self.local_url}/image/975968.png")
        self.sub_icon_del = self.icon_del.subsample(25, 25)
        self.editing_icon = PhotoImage(file = rf"{self.local_url}/image/950768.png")
        self.sub_editing = self.editing_icon.subsample(25,25)
        self.icon_sell = PhotoImage(file= rf"{self.local_url}/image/1778661.png")
        self.sub_sell = self.icon_sell.subsample(25,25)
        self.change_height =1
        self.dict = {}
        
        

        self.app()          
        
    def app(self):
        self.master.title("PRT")
        
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
        
        
        self.label = tk.Label(self, text = "PRT Progamm",background="#78DBE2" , font = "Haettenschweiler 50" ,fg = "black")
        self.label.grid(row= 0, columnspan= 5, sticky= W+E)
        
        
        def main_p():
            
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            
            
            biography = tk.Label(self, text = "Introduction", font="Haettenschweiler 30", fg = "black")
            biography.grid(row = 2, columnspan= 5, pady= 30)
            
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
                    return text[448::] 
            row_x = 3    
            text_ch = "PRT Progamm - The mobile application is designed for fast recognition of text into images in PNG, JBG, GIF files format. The application can be used as a digitizer of papers, as it includes a tool for direct interception of photos from the scanner. Developed based on the Easyocr library. The application loads an image or projects from an images and processes the result of a txt file. Before using it we recommend that you familiarize yourself with the characteristics of the application visit (Support tab)"
                    
            while True:
                row_x +=1
                characteristic_text = tk.Label(self, text = check_text(text_ch), font="GothicLight 10", fg = "black")
                characteristic_text.grid(row = row_x, columnspan= 5)
                global end
                if end == True:
                    break
            global counter
            end = False
            counter = 0
                    ####
            
        
        self.Button_page = tk.Button(self,  text = "Main Page", bg= "#78DBE2"  ,font="Haettenschweiler 20", command= main_p, cursor="hand2", fg = "black")
        self.Button_page.grid(row=1, column=0)
        
        def all_projects():
            
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            counter_pr = len(glob.glob(rf"{self.local_url}/projects*/*.txt"))
            Label_pr = tk.Label(self, text = f"Your projects: {counter_pr}" , font= "@yugothic 13 bold", fg = "black")
            Label_pr.grid(row= 2 , column= 0, columnspan= 3, pady= 8)
            
            
            if glob.glob(rf"{self.local_url}/projects*/*.txt") == []:
                canv = tk.Canvas(self, bg= "gray", height= 2, width=350)
                canv.grid(row = 3, columnspan= 5, pady= 4)
                label_str = tk.Label(self, text = "You don't have any active projects at the moment.", font="@yugothic 11 ", fg = "black")
                label_str.grid(row= 4 , columnspan= 5)
                label_str2 = tk.Label(self , text = "Log in to the 'files' tab and upload the recordings,", font="@yugothic 11 ", fg = "black")
                label_str2.grid(row= 5 , columnspan= 5)
                label_str2 = tk.Label(self, text = "and save the result.", font="@yugothic 11  ", fg = "black")
                label_str2.grid(row= 6 , column=0, columnspan= 3)
            
            
            else:
                    
                ###########################################################################
                #ОПИСАНИЕ ПРОКРУТКИ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                
                master_frame = tk.Frame(self, bd=3, relief=tk.RIDGE)
                master_frame.grid(columnspan=5)
                master_frame.columnconfigure(0, weight=1)
                frame2 = tk.Frame(master_frame, bd=2, relief=tk.FLAT)
                frame2.grid(row=3, column=0, sticky=tk.NW)   
                canvas = tk.Canvas(frame2)
                canvas.grid(row=0, column=0)
                # Create a vertical scrollbar linked to the canvas.
                vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
                vsbar.grid(row=0, column=1, sticky=tk.NS)
                canvas.configure(yscrollcommand=vsbar.set)
                widget_frame = tk.Frame(canvas)

                #ЗАПОМНИТЬ!!!!!!!!!!
                ##################################################################################
                
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
                    rename = tk.Entry(w, font= 50)
                    rename.delete(0,END)
                    rename.insert(0,file_pr["elem"]["text"])    
                    rename.place(width=150, height=40)
                    rename.bind("<Return>",change_name)
                
                
                
                
                
                        
                
                
                
                
                def start_action(event, arg_e):
                    def close():
                        self.change_height +=0.1
                        canvas.destroy()
                    global count_threads
                    if count_threads >= 3:
                        messagebox.showinfo(title="Exceeded the limit", message="At least 3 threads are supported, please wait for the end of the work and try again.")
                        return
                    count_threads+=1
                    thread = threading.Thread(target=recognize_pr, kwargs={"arg_elem": arg_e["elem"]["textvariable"]})
                    thread.start()
                    width= 150 
                    height=40
                    text_png = str(arg_e["elem"]["textvariable"])[-10::]
                    canvas =  tk.Canvas(self, bg = "#78DBE2", highlightbackground = "#7FFFD4" , height= height, width= width)
                    canvas.create_text(width/2, height/2, fill="black", text = f"add: {text_png}", font= "@yugothic 10")
                    self.change_height -=0.1
                    canvas.place(relx=0.60, rely=self.change_height)
                    canvas.after(3000, close)
                        
                def recognize_pr(arg_elem):
                    global count_threads
                    window = tk.Tk()
                    file = open(str(arg_elem), "r", encoding= "utf-8")
                    s = file.read()
                    s = s.split("\n")
                    s = s[:-1:]
                    res = ""
                    for el in s:
                        res+= Recording_text.text_recognition_res(el)        
                    count_threads-=1
                    label = tk.Label(window)
                    label["text"] = res
                    label.pack()
                    window.mainloop()
                    
                    
                
                
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
                
                
                    
                for file_project in glob.glob(rf"{self.local_url}/projects*/*.txt"):
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
                                label_file = tk.Label(widget_frame, textvariable= file_project, text = rf"{file_project[-(index-1):-abs(index-14):]}.." ,font = "@yugothic 15", cursor="hand2", fg = "black")
                                
                                break
                            else:
                                label_file = tk.Label(widget_frame,  textvariable= file_project ,text = rf"{file_project[-(index-1):-4:]}" ,font = "@yugothic 15", cursor="hand2", fg = "black")
                                
                                break
                        
                    
                    
                    label_file.grid(row = q, column= 0 , columnspan= 2)
                    
                    Label_sell1 = tk.Label(widget_frame, image = self.sub_sell, cursor="hand2")
                    Label_sell1.grid(row = q , column= 2, pady = 10)
                    
                    label_editing2 = tk.Label(widget_frame, image = self.sub_editing, cursor="hand2")
                    label_editing2.grid(row= q, column= 3, pady = 10 )
                    
                    Label_del = tk.Label(widget_frame,image= self.sub_icon_del, cursor="hand2")
                    Label_del.grid(row = q, column= 4, pady= 10 ,sticky= "s")
                    
                    canv = tk.Canvas(widget_frame, bg= "gray", height= 2, width=350)
                    canv.grid(row = q+1, columnspan= 5, pady= 4)
                    
                    
                    data={"elem":label_file, "self": self }
                        
                    
                    label_file.bind("<Enter>", on_label_enter)
                    label_file.bind("<Leave>", on_label_leave)
                    label_file.bind("<Button-1>", lambda event, arg=data: rename_pr(event, arg))          
                    
                    
                    Label_sell1.bind("<Enter>", on_enter)
                    Label_sell1.bind("<Leave>", on_leave)
                    
                    Label_sell1.bind("<Button-1>",lambda event, arg=data: start_action(event, arg))

                    label_editing2.bind("<Enter>", on_enter2)
                    label_editing2.bind("<Leave>", on_leave2)
                    
                    label_editing2.bind("<Button-1>", lambda event, arg=data: on_click_ed(event, arg))
                    
                        
                    Label_del.bind("<Enter>", on_enter3)
                    Label_del.bind("<Leave>", on_leave3) 
                    Label_del.bind("<Button-1>", lambda event, arg=data: delete_pr(event, arg))
                    
                    
                    
                    canvas.create_window((0,0), window=widget_frame, anchor=tk.NW)
                    widget_frame.update_idletasks()
                    bbox = canvas.bbox(tk.ALL)
                    
                    canvas.configure(scrollregion=bbox, width=359, height=500)
                    
        self.Button_projects = Button(self, text= "Projects", bg= "#78DBE2", font="Haettenschweiler 20", command= all_projects, cursor="hand2", fg = "black")
        self.Button_projects.grid(row=1, column=1)
        
        
        def func_files():
            
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            
            
            label_w = tk.Label(self, text = f"Files: {len(self.FILES_LIST)}", font= "@yugothic 13 bold", fg = "black")
            label_w.grid(row = 2, column= 0 , columnspan= 2, pady=5)
            
            
            def f():
                
                if self.FILES_LIST == []:
                    canv = tk.Canvas(self, bg= "gray", height= 2, width=350)
                    canv.grid(row = 3, columnspan= 5, pady= 4)
                    Label_nothing = tk.Label(self, text = "There are no existing images in your project.", font= "@yugothic 13", fg = "black")   
                    Label_nothing.grid(row = 4, columnspan = 5)     
                else:
                        
                   
                    master_frame = tk.Frame(self, bd=3, relief=tk.RIDGE)
                    master_frame.grid(columnspan=5)
                    master_frame.columnconfigure(0, weight=1)
                    frame2 = tk.Frame(master_frame, bd=2, relief=tk.FLAT)
                    frame2.grid(row=3, column=0, sticky=tk.NW)   
                    canvas = tk.Canvas(frame2)
                    canvas.grid(row=0, column=0)
                    # Create a vertical scrollbar linked to the canvas.
                    vsbar = tk.Scrollbar(frame2, orient=tk.VERTICAL, command=canvas.yview)
                    vsbar.grid(row=0, column=1, sticky=tk.NS)
                    canvas.configure(yscrollcommand=vsbar.set)
                    widget_frame = tk.Frame(canvas)

                    #ЗАПОМНИТЬ!!!!!!!!!!##########################################################################
                    
                    
                    
                    
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
                    
                        
                    def start_action(event, arg_e):
                        def close():
                            self.change_height +=0.1
                            canvas.destroy()
                        global count_threads
                        if count_threads >= 3:
                            info = messagebox.showinfo(title="Exceeded the limit", message="At least 3 threads are supported, please wait for the end of the work and try again.")
                            return
                        count_threads+=1
                        thread = threading.Thread(target=recognize, kwargs={"arg_elem": arg_e["elem"]})
                        print(threading.main_thread().name)
                        print(thread.name)
                        thread.start()
                        width= 150 
                        height=40
                        text_png = arg_e["elem"][-10::]
                        canvas =  tk.Canvas(self, bg = "#78DBE2", highlightbackground = "#7FFFD4" , height= height, width= width)
                        canvas.create_text(width/2, height/2, fill="black", text = f"add: {text_png}", font= "@yugothic 10")
                        self.change_height -=0.1
                        canvas.place(relx=0.60, rely=self.change_height)
                        canvas.after(3000, close)
                        
                    
                    
                    
                    def recognize(arg_elem):
                        global count_threads
                        res = Recording_text.text_recognition_res(arg_elem)        
                        window = tk.Tk()
                        label = tk.Label(window)
                        label["text"] = res
                        label.pack()
                        window.mainloop()
                        count_threads-=1
                    
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
                            Label_str = tk.Label(widget_frame, cursor="hand2" ,textvariable= elem, text = rf"{elem[-(index_start-1):-(index_start-11):]}..{elem[-4::]}", font= "@yugothic 15", fg = "black")
                            
                        else:
                            Label_str = tk.Label(widget_frame, cursor="hand2", textvariable= elem, text = rf"{elem[-(index_start-1)::]}", font= "@yugothic 15", fg = "black")
                                
                                    
                        
                        Label_str.grid(row = b, column=0, columnspan= 2 , pady= 3)
                        Label_str2 = tk.Label(widget_frame, text= "recognize text" , font= "@yugothic 15", cursor="hand2", fg = "black")#####################
                        Label_str2.grid(row = b, column= 2, columnspan= 3 , pady= 3,sticky= "w")
                        
                        Label_str3 = tk.Label(widget_frame, image= self.sub_icon_del, cursor="hand2", fg = "black")
                        Label_str3.grid(row = b, column= 4, pady= 10 ,sticky= "s")
                        
                        canv = tk.Canvas(widget_frame, bg= "gray", height= 2, width=350)
                        canv.grid(row = b+1, columnspan= 5, pady= 4)
                            
                        data={"self": self, "elem": elem }
                        
                        Label_str.bind("<Button-1>", lambda event, arg=data: func_c(event, arg))
                        Label_str.bind("<Enter>", on_enter)
                        Label_str.bind("<Leave>", on_leave)
                        
                        Label_str2.bind("<Button>", lambda event, arg=data: start_action(event, arg))
                        Label_str2.bind("<Enter>", on_enter2)
                        Label_str2.bind("<Leave>", on_leave2)
                        
                        
                        
                        Label_str3.bind("<Button-1>", lambda event, arg=data: on_click_del_file(event, arg))
                        Label_str3.bind("<Enter>", on_enter3)
                        Label_str3.bind("<Leave>", on_leave3)
                        
                        
                        canvas.create_window((0,0), window=widget_frame, anchor=tk.NW)
                        widget_frame.update_idletasks()
                        bbox = canvas.bbox(tk.ALL)
                        canvas.configure(scrollregion=bbox, width=359, height=500)
             
            f()
                   
        self.Button_files = Button(self, text= "Files", bg= "#78DBE2", font="Haettenschweiler 20",command= func_files, cursor="hand2", fg = "black")
        self.Button_files.grid(row=1, column=2)
        

        def Support():
            for label in self.grid_slaves():
                if int(label.grid_info()["row"]) > 1:
                    label.destroy()
            label = tk.Label(self, text = "1) In the upper left click on 'Open File'", font='Helvetica 12 bold')
            label.grid(row = 3 , column = 0, columnspan=5, pady= 25 )
            label_img = tk.Label(self, image = self.support_1, relief="groove", fg = "black")
            label_img.grid(row = 4 , column = 0 , columnspan= 2)
            label_img1 = tk.Label(self, image = self.support_2 , relief="groove", fg = "black" )
            label_img1.grid(row = 4, column= 2, columnspan=3)
            label_1 = tk.Label(self, text = "2) Uploading the file", font='Helvetica 12 bold', fg = "black")
            label_1.grid(row = 5 , column= 0, columnspan= 5, pady= 8)
            label_img_2 = tk.Label(self, image = self.support_3 )
            label_img_2.grid(row = 6, columnspan= 5)
            label_3 = tk.Label(self, text = "3) Click on the green button to recognize the text",  font='Helvetica 12 bold', fg = "black")
            label_3.grid(row = 7, column= 0, columnspan= 5, pady= 8)
            label_img_3 = tk.Label(self, image = self.support_4)
            label_img_3.grid(row = 8, columnspan= 5)
            
            label_4 = tk.Label(self, text = "4) Or save the project and upload recognize",font='Helvetica 12 bold', fg = "black")
            label_4.grid(row = 9, columnspan= 5, pady= 8)
            label_img_4 = tk.Label(self, image = self.support_6)
            label_img_4.grid(row = 10, columnspan= 5)
            pass
        
        
        self.Button_support = Button(self, text= "Support", bg= "#78DBE2", font="Haettenschweiler 20", cursor="hand2" , command= Support, fg = "black")
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
                        file = filedialog.asksaveasfile(filetypes = files, defaultextension = files,initialdir= f"{self.local_url}/projects")
                    except AttributeError:
                        return
                    write_res_to_file = open(file.name, "w", encoding= "utf-8")
                    
                    
                    for el in self.FILES_LIST:
                        write_res_to_file.write(rf"{str(el)}\n")
                    
                    write_res_to_file.close()
                    self.master.destroy()
                else:
                    self.master.destroy()
                    

        self.button_exit = Button(self, text= "Exit", bg= "red", font="Haettenschweiler 20", command=exit, cursor="hand2" ,fg = "black")
        self.button_exit.grid(row=1, column=4)
        self.pack() #<<<<<<<<<<< Запомнить

 
def main():
    
    window = tk.Tk()
    app = Example()
    app.Button_page.invoke()
    window.geometry("414x736")
    window.iconbitmap(rf"{app.local_url}/image/photo_photography_picture_camera_summer_icon_251688.ico")
    mainmenu = Menu(window)
    window.config(menu= mainmenu)
    
    file_menu = Menu(mainmenu, tearoff= 0)
    file_settings = Menu(mainmenu, tearoff= 0)
    def on_closing():
        if app.FILES_LIST == []:
            app.master.destroy()
            return
        else:
            answer = messagebox.askyesno(title="The saving process", message="Do you want to save the result of the current project?")
            if answer:
                save_project()
                app.master.destroy()
            else:
                app.master.destroy()
                return
        
    window.protocol("WM_DELETE_WINDOW", on_closing)
    
    
    def open_file():
        files = [('PNG', '*.png'),('JPG', '*.jpg')]
        
        try:
            name = filedialog.askopenfilename(filetypes = files, defaultextension = files, initialdir= rf"{app.local_url}/image" )
        except AttributeError:
            return
        if name == "":
            return
        save_image = Image_ch(name).save()    
        app.FILES_LIST.append(save_image)
        app.Button_files.invoke() # ИНВОК ЗАПУСКАЕТ ВИДЖЕТ БЕЗ КЛИКА!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    def save_project():
        if app.FILES_LIST == []:
            messagebox.showerror(title="Input error", message="Your project is empty, upload files to save.")
            return
        files = [('Text Document', '*.txt'),]
        try:
            file = filedialog.asksaveasfile(filetypes = files, defaultextension = files ,initialdir= rf"{app.local_url}/projects")
        except AttributeError:
            return
        write_res_to_file = open(file.name, "w", encoding= "utf-8")
                                
        for el in app.FILES_LIST:
            write_res_to_file.write(f"{str(el)}\n")
        write_res_to_file.close()
        app.FILES_LIST.clear()
        local_path_url = str(app.local_url)+"/projects/"
        counter = 0
        for x in file.name[::-1]:
            if x == "/":
                break
            counter +=1
        if local_path_url != file.name[:-counter]:
            app.Button_projects.invoke()        
            shutil.copy(str(file.name), local_path_url)
            messagebox.showinfo(title="The project is saved", message= "Your project has been saved successfully!")
        
        app.Button_projects.invoke()
        
    def info():
        window= tk.Tk()
        label = tk.Label(window, text = "Version 0.1.1", fg = "black")
        label.pack()
        window.mainloop()
        
    file_menu2 = Menu(file_menu, tearoff= 0)
    file_menu2.add_command(label="Work1")
    file_menu2.add_command(label="Work2")
    file_menu.add_command(label="Open File", command= open_file)
    file_menu.add_command(label="Save Project", command= save_project)
    file_settings.add_command(label="Info", command= info)
    mainmenu.add_cascade(label= "File", menu= file_menu )
    mainmenu.add_cascade(label= "Settings", menu =  file_settings)
    window.mainloop()

if __name__ == '__main__': 
    main()
        