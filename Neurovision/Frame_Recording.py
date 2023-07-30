import shutil
from tkinter import filedialog, ttk
from tkinter import Frame, messagebox
import tkinter as tk
import os
import glob
from pathlib import Path
from Frame_Files import Files
from PIL import Image, ImageTk
class Recording(tk.Frame):
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    def __init__(self, frame, frame2, frame_main):
        super().__init__()
        self.img = Image.open(f"{self.local_url}/image/save.png")
        self.bg = ImageTk.PhotoImage(self.img)
        self.frame = frame
        self.frame2 = frame2
        self.frame_main = frame_main
        
        self.New_Frame_Files = None
        self.label_pr_act = tk.Label(self.frame, bg= "#CCCCFF", fg="#6666ff",  font= "Arial 14")
        self.pr_activion = False

    def list_box_pr(self):
        
        projects_url_res  =glob.glob(rf"{self.local_url}/projects*/*")
        projects= []
        
        for x in projects_url_res:
            projects.append(x.replace("\\", "/"))
        
        
        """def on_enter(e):
            e.widget['background'] = 'gray'                
        def on_leave(e):
            e.widget['background'] = 'SystemButtonFace'"""
        
        label = tk.Label(self.frame,bg= "#CCCCFF", fg="#6666ff", text = "Orientation:", font= "Arial 12")
        label.place(x = 10, y = 10)
        
        label = tk.Label(self.frame, bg= "#CCCCFF", fg="#6666ff",text = "Select a project", font= "Arial 12")
        label.place(x = 10, y = 60)
        
        
        index = 0
        list_files_pr =[]            
        for elem_list in projects:
            for elem in elem_list[::-1]:
                index +=1 
                if elem == "/":
                    list_files_pr.append(elem_list[-index+1::])
                    index=0
                    break  
        
            
            
        def selected(event):
            
            def pr_load():
                
                self.label_pr_act["text"] = listbox.get() 
                for elem in list_files_pr:
                    if elem == listbox.get():
                        
                        self.pr_activion = True
                        check_files = glob.glob(rf"{self.local_url}/projects/{elem}*/*")
                        res_files= []
                        for x in check_files:
                            res_files.append(x.replace("\\", "/"))
                        self.frame2.destroy()
                        self.frame = tk.LabelFrame(self.frame_main ,text = "Editing projects", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 210, bg= "#CCCCFF")
                        self.frame.place(x= 1, y= 1)
                        Frame_Files = tk.LabelFrame(self.frame_main ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 235, bg= "#CCCCFF")
                        Frame_Files.place(x= 1, y= 210)
                        Files(Frame_Files).load_frame(res_files)
                        break # Продолжить!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        
            
            if self.pr_activion:
                
                answer = messagebox.askyesno(title="Creating a project", message= "You already have a current project , do you want to save and create a new one?")              
                if answer:
                    # СОХРАНИТЬ ПРОЕКТ. ОЧИСТИТЬ , И ЗАГРУЗИТЬ ДРУГОЙ!!!!
                    save_pr_and_file()
                    pr_load() 
                    
                elif answer == None:
                    # do nothing
                    return
                else:
                    pass   
            
            else:
                self.pr_activion = True
                pr_load()
                
                
                ##########
  
        listbox = ttk.Combobox(self.frame, width= 50,values= list_files_pr)
        listbox.bind("<<ComboboxSelected>>", selected)
        listbox.place(x = 10, y = 90)     
        button_upload = tk.Label(self.frame, text= "Upload a project", relief= tk.GROOVE, cursor="hand2")
        button_upload.place(x = 40, y = 140)
        
        
        
        def save_pr_and_file():
            if self.pr_activion:
                save_window = tk.Toplevel()
                save_window.resizable(False, False)
                save_window.title("Save")
                save_window["bg"] = "#CCCCFF"
                save_window.geometry("220x90+860+450")
                label_name_write = tk.Label(save_window, text = "Project name", fg="#6666ff",font = "Arial 12 bold ", bg= "#CCCCFF")
                label_name_write.pack(anchor= tk.N, padx= 5)
                def on_enter(e):
                    e.widget['background'] = 'gray'
                def on_leave(e):
                    e.widget['background'] = "#CCCCFF"
                def res_enter(event):
                    path = filedialog.askdirectory()
                    files_pr = Files("").FILES_LIST
                    text = Entry.get()
                    add_new_project = self.local_url + f"/projects/{text}"
                    add_cur_project = path + f"/{text}"
                    Path(add_new_project).mkdir(parents=True, exist_ok=True)
                    Path(add_cur_project).mkdir(parents=True, exist_ok=True)
                    for copy_file in files_pr:
                        if copy_file == " ":
                            continue
                        shutil.copy(str(copy_file), f"{path}/{text}")
                        shutil.copy(str(copy_file), f"{self.local_url}/projects/{text}")
                    save_window.destroy()
                    Files("").FILES_LIST.clear()
                    self.frame = tk.LabelFrame(self.frame_main ,text = "Editing projects", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 210, bg= "#CCCCFF")
                    self.frame.place(x= 1, y= 1)
                    self.frame2 = tk.LabelFrame(self.frame_main ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 235, bg= "#CCCCFF")
                    self.frame2.place(x= 1, y= 210)

                    
                    Recording(self.frame, self.frame2, self.frame_main).list_box_pr()  
                    
                    
                    if self.pr_activion == True:
                        self.pr_activion = False
                        add_new_pr(event)
                    messagebox.showinfo(title="The project is saved", message= "Your project has been saved successfully!")
                    
                    
                    
                    
                Entry = tk.Entry(save_window,width=33)
                Entry.pack(anchor= tk.CENTER, padx= 5)
                icon_image = tk.Label(save_window, image=self.bg, bg="#CCCCFF")
                icon_image.pack(anchor= tk.CENTER)
                Entry.bind("<Return>", res_enter)
                icon_image.bind("<Enter>", on_enter)
                icon_image.bind("<Leave>",  on_leave)
                icon_image.bind("<Button-1>", res_enter)
                save_window.mainloop()
                self.pr_activion = False
        
        def add_new_pr(event):
            if self.pr_activion == False:
                self.pr_activion= True    

                add_new_project = self.local_url + f"/projects/New_Project"
                Path(add_new_project).mkdir(parents=True, exist_ok=True)
                
                self.label_pr_act["text"] =  "New_Project"
                self.label_pr_act.place(x = 100, y = 6)
                self.New_Frame_Files = Files(self.frame2).add_frame(" ")  ##############
            
            else:
                # У вас уже есть текущий проект хотите создать новый и сохранить?
                answer = messagebox.askyesno(title="Creating a project", message= "You already have a current project , do you want to save and create a new one?")              
                if answer:
                    save_pr_and_file()
                    # СОХРАНИТЬ ТЕКУЩИЙ ПРОЕКТ И ОБНУЛИТЬ СТАТУС 
                else:
                    return
        
        button = tk.Label(self.frame, text= "Add new project", relief= tk.GROOVE, cursor="hand2")
        button.place(x = 180, y = 140)
        
        button.bind("<Button-1>", add_new_pr)
        """
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button_upload.bind("<Enter>", on_enter)
        button_upload.bind("<Leave>", on_leave)
        """
        
        