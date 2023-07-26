import shutil
from tkinter import ttk
from tkinter import Frame, messagebox
import tkinter as tk
import os
import glob
from pathlib import Path
from Frame_Files import Files

class Recording(Frame):
    def __init__(self, frame, frame2):
        super().__init__()
        self.frame = frame
        self.frame2 = frame2
        self.local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
        self.count_new = 0
        self.First = True

    def list_box_pr(self):
        projects_url_res  =glob.glob(rf"{self.local_url}/projects*/*")
        projects= []
        for x in projects_url_res:
            projects.append(x.replace("\\", "/"))
        
        
        def on_enter(e):
            e.widget['background'] = 'gray'                
        def on_leave(e):
            e.widget['background'] = 'SystemButtonFace'
        
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
            for elem in list_files_pr:
                if elem == listbox.get():
                    res = glob.glob(rf"{self.local_url}/projects/{elem}*/*")
                    pass # Продолжить!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    
                    
        listbox = ttk.Combobox(self.frame, width= 50,values= list_files_pr)
        listbox.bind("<<ComboboxSelected>>", selected)
        listbox.place(x = 10, y = 90)     
        button_upload = tk.Label(self.frame, text= "Upload a project", relief= tk.GROOVE, cursor="hand2")
        button_upload.place(x = 40, y = 140)
        
        
        def add_new_pr(event):
            if self.First == True:
                self.First= False    
                self.count_new +=1
                add_new_pr = self.local_url + f"/projects/New_Project"
                Path(add_new_pr).mkdir(parents=True, exist_ok=True)
                label_pr_act = tk.Label(self.frame, text = f"New_Project", bg= "#CCCCFF", fg="#6666ff",  font= "Arial 14")
                label_pr_act.place(x = 100, y = 6)
                Files(" ").add_file(self.frame2)  ##############
            else:
                # У вас уже есть текущий проект хотите создать новый и сохранить?
                
                answer = messagebox.askyesno(title="Creating a project", message= "You already have a current project , do you want to save and create a new one?")              
                
                if answer:
                    shutil.rmtree(f"{self.local_url}/projects/New_project")
                    add_new_pr = self.local_url + f"/projects/New_Project/"
                    Path(add_new_pr).mkdir(parents=True, exist_ok=True)
                else:
                    return
        
        
        
        
        button = tk.Label(self.frame, text= "Add new project", relief= tk.GROOVE, cursor="hand2")
        button.place(x = 180, y = 140)
        
        button.bind("<Button-1>", add_new_pr)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button_upload.bind("<Enter>", on_enter)
        button_upload.bind("<Leave>", on_leave)
        
        
        