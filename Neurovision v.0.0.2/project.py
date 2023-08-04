import glob
import threading
import tkinter as tk
from tkinter import messagebox, ttk, filedialog, Listbox
import os
import shutil
from PIL import Image, ImageTk
from pathlib import Path
from Frame_Files import Files
from frame_easyocr import Recording_text
OBJ = Files
class Example(tk.Frame):
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    def __init__(self):
        super().__init__()
        
        self.img_panda = tk.PhotoImage(file = rf"{self.local_url}/image/panda.png" ).subsample(3,3)
  
        self.master.title("Neurovision v.0.0.2")
        self.Frame_app = tk.Frame()
        self.Frame_app.pack(side = tk.TOP)
        
        self.Frame_Instruction = tk.Frame(self.Frame_app, width=250, height=490)              
        self.Frame_Instruction.pack(side = tk.LEFT)                                                         
        self.label_img_panda = tk.Label(self.Frame_Instruction ,image= self.img_panda)      
        self.label_img_panda.place(x=40, y =18)                     

        
        
        self.Frame_Recording = tk.Frame(self.Frame_app, width=332, height=490)                                                                                
        self.Frame_Recording.pack(side = tk.LEFT)                                                                                                                           
        self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) 
        self.Frame_recording.place(x= 1, y= 1)                                                                                                                              
        self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files", font = "Arial 12 bold", width= 320, height= 250)                
        self.Frame_Files.place(x= 1, y= 235)                                                                                                                                
        self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10 bold")
        self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
        
            
        
            

        self.Frame_Handler = tk.Frame(self.Frame_app, width=250, height=490)
        self.Frame_Handler.pack(side = tk.LEFT)
        
        self.Handler = tk.LabelFrame(self.Frame_Handler ,text = "Handler",font = "Arial 12 bold ", width= 247, height= 120) #
        self.Handler.place(x= 1, y= 1)
        
        for c in range(2): self.Handler.columnconfigure(index=c, weight=1)
        for r in range(2): self.Handler.rowconfigure(index=r, weight=1)
        
        
        
        def thred_process():
            thread = threading.Thread(target=recognize_pr).start()
        
        
        
        def recognize_pr():
            self.grab_set() 
            res =""
            self.progress["value"] = 0
            self.progress["maximum"] = len(OBJ.FILES_LIST) 
            count = 0
            for file in OBJ.FILES_LIST:
                count += 1
                self.progress["value"] = count
                if file == " ":
                    continue
                
                result= Recording_text.text_recognition_res(file)  
                res+= result
                if result == "":
                    messagebox.showerror(title= "Something gone wrong" , message=  "Some files do not contain a text value or are not of good quality.")
                    
            window = tk.Tk()
            label = tk.Label(window)
            label["text"] = res
            label.pack()
            self.Load_frame_app.after(2000)
            self.progress.destroy()
            self.progress = ttk.Progressbar(self.Load_frame_app, orient="horizontal", 
                                            length=844,mode="determinate")
            self.progress.pack()    
            self.grab_release()
            window.mainloop()  
        
        
        
        
        def thred_process_2():
            file = filedialog.askopenfile().name
            thread = threading.Thread(target=recognize_file, kwargs= {"arg_elem":file} ).start()
        
        
        def recognize_file(arg_elem):
            self.grab_set() 
            res = Recording_text.text_recognition_res(arg_elem)
            if res == "":
                messagebox.showerror(title= "Something gone wrong" , message=  "Some files do not contain a text value or are not of good quality.")
                self.grab_release()
                return
            window = tk.Tk()
            label = tk.Label(window)
            label["text"] = res
            label.pack()
            self.Load_frame_app.after(2000)    
            self.progress.destroy()
            self.progress = ttk.Progressbar(self.Load_frame_app, orient="horizontal", 
                                            length=844,mode="determinate")
            self.progress.pack()    
            self.grab_release()
            window.mainloop()  
        
        self.Label_get = ttk.Button(self.Handler, text = "Recognize a file",  cursor="hand2", command=thred_process_2)
        self.Label_get.grid(row=0, column=0, columnspan=2, ipadx=71, ipady=4, padx=5, pady=5)
            
        
        self.Label_get = ttk.Button(self.Handler, text = "Recognize a project",  cursor="hand2", command=thred_process)
        self.Label_get.grid(row=1, column=0, columnspan=2, ipadx=60, ipady=4, padx=5, pady=5)
        
        
        
        def thred_process_3():
            thread = threading.Thread(target=recognize_pr_2).start()
        
        def recognize_pr_2():
            self.grab_set() 
            res =""
            self.progress["value"] = 0
            self.progress["maximum"] = len(OBJ.FILES_LIST) 
            count = 0
            def thrd(file_txt):
                res = Recording_text.text_recognition_res(file_txt)    
                window = tk.Tk()
                label = tk.Label(window)
                label["text"] = res  
                label.pack()
                window.mainloop() 
                
            for file in OBJ.FILES_LIST:
                count += 1
                self.progress["value"] = count
                if file == " ":
                    continue
                threading.Thread(target=thrd, kwargs= {"file_txt": file}).start()
                
            self.Load_frame_app.after(2000)
            self.progress.destroy()
            self.progress = ttk.Progressbar(self.Load_frame_app, orient="horizontal", 
                                            length=844,mode="determinate")
            self.progress.pack()    
            self.grab_release()
            
        
        self.Label_get2 = ttk.Button(self.Handler, text = "Recognize separately",  cursor="hand2", command=thred_process_3)
        self.Label_get2.grid(row=2, column=0, columnspan=2, ipadx=56, ipady=4, padx=5, pady=5)
        
        
        
        self.Additional_settings = tk.LabelFrame(self.Frame_Handler,text = "Additional settings",font = "Arial 12 bold ", width= 247, height= 325)                #
        self.Additional_settings.place(x= 1, y= 161)
        
        
        
        

        self.Load_frame_app = tk.Frame()                                                     
        self.Load_frame_app.pack(side= tk.TOP)                                                             
        
        self.progress = ttk.Progressbar(self.Load_frame_app, orient="horizontal", 
                                        length=844,mode="determinate")         
        self.progress.pack()                                                                             
        
class FRAME_RECORDING(Example):
    def __init__(self):
        super().__init__()
        self.img = Image.open(f"{self.local_url}/image/save.png")
        self.bg = ImageTk.PhotoImage(self.img)
        self.remove_selected = []
        self.OBJ = Files
        self.selected_before =  None
        self.label_pr_act = tk.Label(self.Frame_Recording,  font= "Arial 14") #
        self.label_pr_act.place(x=126, y =37)
        self.pr_activion = False                                                                           
        self.new_pr_bool = False                       
    
        self.Recording_Frame()
        self.Handler_Frame()
        
        
    def save_pr_and_file(self):
        if self.pr_activion:
            save_window = tk.Toplevel()
            save_window.resizable(False, False)
            save_window.title("Save")
            save_window.geometry("220x90+860+450")
            label_name_write = tk.Label(save_window, text = "Project name",font = "Arial 12 bold ")
            label_name_write.pack(anchor= tk.N, padx= 5)
            def on_enter(e):
                e.widget['background'] = 'gray'
            def on_leave(e):
                e.widget['background'] = "SystemButtonFace"
            def res_enter(event):
                path = filedialog.askdirectory()
                files_pr = OBJ.FILES_LIST
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
        
                self.Frame_recording.destroy()
                self.Frame_Files.destroy()
                
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                self.Frame_Files.place(x= 1, y= 235)      
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                OBJ.FILES_LIST.clear()
                self.pr_activion = False
                self.Recording_Frame()
                save_window.destroy()
                save_window.quit()
                    
                    
                    
            Entry = tk.Entry(save_window,width=33)
            Entry.pack(anchor= tk.CENTER, padx= 5)
            icon_image = tk.Label(save_window, image=self.bg)
            icon_image.pack(anchor= tk.CENTER)
            Entry.bind("<Return>", res_enter)
            icon_image.bind("<Enter>", on_enter)
            icon_image.bind("<Leave>",  on_leave)
            icon_image.bind("<Button-1>", res_enter)
            save_window.mainloop()
            self.pr_activion = False
            return
    

    def urls_project_files(self):
        projects_url_res  =glob.glob(rf"{self.local_url}/projects*/*")
        projects= []
        for x in projects_url_res:
            projects.append(x.replace("\\", "/"))   
        
        index = 0
        list_files_pr =[]            
        for elem_list in projects:
            for elem in elem_list[::-1]:
                index +=1 
                if elem == "/":
                    list_files_pr.append(elem_list[-index+1::])
                    index=0
                    break   
        return list_files_pr
    
    
    def Recording_Frame(self):
        def selected(event):
            def pr_load(): 
        
                global OBJ
                if OBJ.upload_bool_:
                    self.pr_activion = True
                    selected(event)
                    return
                
                for elem in urls_project_files():
                    if elem == self.listbox.get() or elem == self.selected_before:
                        
                        check_files = glob.glob(rf"{self.local_url}/projects/{elem}*/*")
                        res_files= []
                        for x in check_files:
                            res_files.append(x.replace("\\", "/"))
                        self.label_pr_act["text"] = self.listbox.get() 
                        self.Frame_Files.destroy()
                        self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                        self.Frame_Files.place(x= 1, y= 235)      
                        OBJ(self.Frame_Files, self.Frame_Recording).load_frame(res_files)
                        break
            if self.pr_activion:
                        answer = messagebox.askyesno(title="Save Changes", message= "Changes have been detected do you want to save them?")              
                        if answer:
                            self.save_pr_and_file()
                            OBJ.upload_bool_ = False
                            self.pr_activion = False                            
                            messagebox.showinfo(title="The project is saved", message= "Your project has been saved successfully!")
                            
                            pr_load() 
                        else:
                            if self.label_pr_act["text"] == "New Project":
                                index= list(self.listbox["values"]).index("New Project")
                                list_res =  list(self.listbox["values"])
                                self.selected_before = self.listbox.get()
                                del list_res[index]
                                index_cur = list_res.index(self.selected_before)
                                self.listbox.destroy()                        
                                self.listbox = ttk.Combobox(self.Frame_Recording, width= 45,values= list_res)
                                self.listbox.current(index_cur)
                                self.listbox.place(x = 10, y = 130)
                                self.listbox.bind("<<ComboboxSelected>>", selected)
                            OBJ.upload_bool_ = False
                            self.pr_activion = False
                            pr_load() 
            else:
                pr_load()
                        
        def urls_project_files():
            projects_url_res  =glob.glob(rf"{self.local_url}/projects*/*")
            projects= []
            for x in projects_url_res:
                projects.append(x.replace("\\", "/"))   
            
            index = 0
            list_files_pr =[]            
            for elem_list in projects:
                for elem in elem_list[::-1]:
                    index +=1 
                    if elem == "/":
                        list_files_pr.append(elem_list[-index+1::])
                        index=0
                        break   
            return list_files_pr
        

        
        label = tk.Label(self.Frame_Recording, text = "Current Project:", font= "Arial 12")
        label.place(x = 10, y = 40)
        label = tk.Label(self.Frame_Recording,text = "Select a project", font= "Arial 12")
        label.place(x = 10, y = 100)
        
        
        
        self.listbox = ttk.Combobox(self.Frame_Recording, width= 45,values= urls_project_files() )
        if self.new_pr_bool == True:
            
            self.label_pr_act["text"] = "New Project"
            self.listbox.insert(0, "New Project")
            index= list(self.listbox["values"]).index("New Project")
            self.listbox.current(index)
            self.pr_activion = False
            
        self.listbox.bind("<<ComboboxSelected>>", selected)
        self.listbox.place(x = 10, y = 130)  
        self.listbox['state'] = 'readonly'  

            
        
    def Handler_Frame(self):
        def Remove_pr():
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " ":
                messagebox.showinfo(title="Project not found", message="Select or upload the project to continue.")
            else:
                answer = messagebox.askyesno(title="Remove process", message= "Are you sure you want to remove the project?")
                if answer:
                    name = self.label_pr_act["text"]
                    shutil.rmtree(self.local_url +f"/projects/{name}") 
                    
                    self.Frame_Files.destroy()
                    self.Frame_recording.destroy()
                    self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                    self.Frame_Files.place(x= 1, y= 235)  
                    self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                    self.Frame_recording.place(x= 1, y= 1)
                    self.Recording_Frame()
                    self.label_pr_act["text"] = ""
                    messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                    
                else:
                    return
            
        self.Remove_a_project = ttk.Button(self.Additional_settings, text = "Remove a project",  cursor="hand2", command=Remove_pr)
        self.Remove_a_project.grid(row=0, column=0, columnspan=2, ipadx=65, ipady=4, padx=5, pady=5)
        
        
        def Remove_all_files():
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " ":
                messagebox.showinfo(title="Project not found", message="Select or upload the project to continue.")
            else:
                answer = messagebox.askyesno(title="Remove process", message= "Are you sure you want to remove all the files of this project?")
                if answer:
                    name = self.label_pr_act["text"]
                    files = glob.glob(self.local_url+f"/projects/{name}/*")
                    print(files)
                    for file in files:
                        os.remove(file)
                        
                    self.Frame_Files.destroy()
                    
                    self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                    self.Frame_Files.place(x= 1, y= 235)  
                    self.pr_activion = False
                    OBJ.upload_bool_ = False
                    OBJ(self.Frame_Files, self.Frame_Recording).add_frame()
                    OBJ(self.Frame_Files, self.Frame_Recording).load_frame("")
                        
                    messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                    
                else:
                    return
        
        self.Remove_all_files = ttk.Button(self.Additional_settings, text = "Remove all files",  cursor="hand2", command= Remove_all_files)
        self.Remove_all_files.grid(row=1, column=0, columnspan=2, ipadx=70, ipady=4, padx=5, pady=5)
        
        
        def Remove_all_pr():

            answer = messagebox.askyesno(title="Remove process", message= "Are you sure you want to remove all projects?")
            if answer: 
                print(self.urls_project_files())
                for file_pr in self.urls_project_files():
                    shutil.rmtree(self.local_url +f"/projects/{file_pr}")
                self.Frame_Files.destroy()
                self.Frame_recording.destroy()
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                self.Frame_Files.place(x= 1, y= 235)  
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                self.Recording_Frame()
                self.label_pr_act["text"] = ""
                messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                
            else:
                return
            
        
        self.Remove_all_projects = ttk.Button(self.Additional_settings, text = "Remove all projects",  cursor="hand2", command=Remove_all_pr)
        self.Remove_all_projects.grid(row=2, column=0, columnspan=2, ipadx=59, ipady=4, padx=5, pady=5)
        
        
        def upload_project():
            falder = filedialog.askdirectory()
            index = 0
            files_no_ready = glob.glob(f"{falder}/*")
            files = []
            for file in files_no_ready:
                files.append(file.replace("\\", "/"))
            if files == []:
                return "no data"
            
            self.Frame_Files.destroy()
            self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
            self.Frame_Files.place(x= 1, y= 235)  
            for sym in falder[::-1]:
                index +=1
                if sym == "/": 
                    
                    self.Frame_recording.destroy()
                    self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                    self.Frame_recording.place(x= 1, y= 1)
                    
                    self.label_pr_act = tk.Label(self.Frame_Recording, text= falder[-index+1::],  font= "Arial 14") #
                    self.label_pr_act.place(x=126, y =37)
                    self.Recording_Frame()
                    
                    break

            OBJ(self.Frame_Files, self.Frame_Recording).load_frame(files)         
            

        
        self.Upload_a_project = ttk.Button(self.Additional_settings, text = "Upload a project", cursor="hand2", command= upload_project)
        self.Upload_a_project.grid(row=3, column=0, columnspan=2, ipadx=67, ipady=4, padx=5, pady=5)

        def add_new_pr():
            
            if self.pr_activion == False:
                
                self.pr_activion= True    
                add_new_project = self.local_url + f"/projects/New Project"
                Path(add_new_project).mkdir(parents=True, exist_ok=True)
                self.Frame_recording.destroy()
                self.Frame_Files.destroy()
                
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                self.Frame_Files.place(x= 1, y= 235)      
                self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Upload images to the project", font = "Arial 10 bold ")
                self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
                OBJ(self.Frame_Files, self.Frame_Recording).add_frame()
                
                self.new_pr_bool = True
                self.label_pr_act.destroy()
                self.label_pr_act = tk.Label(self.Frame_Recording, text = "New Project", font= "Arial 14") #
                self.label_pr_act.place(x=126, y =37)
                
                self.Recording_Frame()
                
                messagebox.showinfo(title= "Create process",message="The project has been created!")
                
                
                
            elif self.pr_activion == True:
                answer = messagebox.askyesno(title="Creating a project", message= "You already have a current project , do you want to save and create a new one?")              
                if answer:
                    self.save_pr_and_file()
                else:
                    return

        
        
        self.Add_a_project = ttk.Button(self.Additional_settings, text = "Add a project", cursor="hand2", command= add_new_pr)
        self.Add_a_project.grid(row=4, column=0, columnspan=2, ipadx=74, ipady=4, padx=5, pady=5)
        
        
        def add_file():
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " ":
                messagebox.showinfo(title="Project not found", message="Select or upload the project to continue.")
            else:
                self.Frame_Files.destroy()
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                self.Frame_Files.place(x= 1, y= 235)  
                OBJ(self.Frame_Files, self.Frame_Recording).add_file(self.label_pr_act["text"])
                
        
        self.Add_a_file = ttk.Button(self.Additional_settings, text = "Add a file", cursor="hand2", command= add_file)
        self.Add_a_file.grid(row=5, column=0, columnspan=2, ipadx=77, ipady=4, padx=5, pady=5)
        
        
        
        def save(): 
            if self.label_pr_act["text"] == "New Project":
                self.pr_activion = True        
                self.save_pr_and_file()
                shutil.rmtree(f"{Example.local_url}/projects/New project")
                self.Frame_recording.destroy()
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                self.new_pr_bool = False
                self.pr_activion = False
                OBJ.upload_bool_ = False
                self.Recording_Frame()
            else:
                self.pr_activion = True        
                self.save_pr_and_file()
                self.pr_activion = False
                OBJ.upload_bool_ = False
                self.Frame_recording.destroy()
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                
                self.Recording_Frame()

        self.exit = ttk.Button(self.Additional_settings, text = "Save",  cursor="hand2", command= save)
        self.exit.grid(row=7, column=0, columnspan=2, ipadx=77, ipady=4, padx=5, pady=5)
        
        

def main():
    window =  tk.Tk()
    window.resizable(False,False)
    app = FRAME_RECORDING()
    
    def on_closing():
        if OBJ.upload_bool_ == False:
            if app.label_pr_act["text"] == "New Project":
                shutil.rmtree(f"{Example.local_url}/projects/New project")
            app.master.destroy()
            return
        else:
            if app.label_pr_act["text"] == "New Project":
                answer = messagebox.askyesno(title="The saving process", message="Do you want to save the result of the current project?")
                if answer:
                    
                    app.pr_activion = True
                    app.save_pr_and_file()##############################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    
                    shutil.rmtree(f"{Example.local_url}/projects/New project")
                    app.master.destroy()
                else:
                    shutil.rmtree(f"{Example.local_url}/projects/New project")
                    app.master.destroy()
                    return
            else:
                app.master.destroy()
        
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.geometry("845x510+550+300")
    
    #window.wm_attributes('-transparentcolor','red')
    window.mainloop()
    
if __name__ == "__main__":
    main()