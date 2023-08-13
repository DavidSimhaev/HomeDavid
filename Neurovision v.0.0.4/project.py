import glob
import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk, filedialog, Listbox
import os
import shutil
from PIL import Image, ImageTk
from pathlib import Path
from Frame_Files import Files
from frame_easyocr import Recording_text
OBJ = Files
txt_res = None
class Example(tk.Frame):
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    def __init__(self):
        super().__init__()
        
        """self.img_logo_rus = Image.open(f"{self.local_url}/image/logo_rus.png")
        self.img_logo_eng = Image.open(f"{self.local_url}/image/logo_england.png")
        self.img_logo_he = Image.open(f"{self.local_url}/image/logo_he.png" )
        
        self.img_rus = ImageTk.PhotoImage(self.img_logo_rus)
        self.img_eng = ImageTk.PhotoImage(self.img_logo_eng)
        self.img_he = ImageTk.PhotoImage(self.img_logo_he)"""
        
        self.img_panda = tk.PhotoImage(file = rf"{self.local_url}/image/panda.png" ).subsample(3,3)
        
        self.img_rus = tk.PhotoImage(file = rf"{self.local_url}/image/logo_rus.png" ).subsample(2,2)
        self.img_eng = tk.PhotoImage(file = rf"{self.local_url}/image/logo_england.png").subsample(2,2)
        self.img_he = tk.PhotoImage(file = rf"{self.local_url}/image/logo_he.png" ).subsample(2,2)
        
        self.lng = None
        self.master.title("Neurovision v.0.0.4")
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
            global txt_res
            try:
                OBJ.FILES_LIST.remove(" ")
            except:
                pass
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " " or self.label_pr_act["text"]== None:
                messagebox.showerror(title="Project not found", message="Select or upload the project to continue.")
                return
            elif OBJ.FILES_LIST == []:
                messagebox.showerror(title="Files not found", message="There are no files in the project.")
                return
            def on_enter(e):
                e.widget['background'] = '#006B9E'                
            def on_leave(e): 
                e.widget['background'] = 'SystemButtonFace'
            def on_click_lng(event, arg):
                self.lng = arg
                window_language.destroy()
                window_language.quit()
            window_language = tk.Toplevel()
            window_language.geometry("180x90+900+500")
            window_language.resizable(False, False)
            label_ =  tk.Label(window_language , text= "Select a language:", font = 50)
            label_.pack()
            label_rus =  tk.Label(window_language , image= self.img_rus,  cursor="hand2")
            label_rus.pack(side = tk.LEFT, padx=2)
            label_eng =  tk.Label(window_language ,  image= self.img_eng, cursor="hand2")
            label_eng.pack(side = tk.LEFT, padx=2)
            label_heb =  tk.Label(window_language , image= self.img_he, cursor="hand2")
            label_heb.pack(side = tk.LEFT, padx=2)
            label_rus.bind("<Enter>", on_enter)
            label_rus.bind("<Leave>", on_leave)        
            label_eng.bind("<Enter>", on_enter)
            label_eng.bind("<Leave>", on_leave)        
            label_heb.bind("<Enter>", on_enter)
            label_heb.bind("<Leave>", on_leave)        
            label_rus.bind("<Button-1>",lambda event, arg="ru": on_click_lng(event, arg))
            label_eng.bind("<Button-1>", lambda event, arg="en": on_click_lng(event, arg))
            label_heb.bind("<Button-1>", lambda event, arg="he": on_click_lng(event, arg))
            window_language.mainloop()
            if self.lng == None:
                return
            
            windwo_load = tk.Tk()
            windwo_load.geometry(("500x80+750+500"))
            windwo_load.resizable(False, False)
            self.master.withdraw()
            
            def action(windwo_load):
                global txt_res
                label_ = tk.Label(windwo_load, text = "Wait for the operation to be completed", font = "Arial 10 bold")
                label_.pack()
                label_name_file_load = tk.Label(windwo_load)
                label_name_file_load.pack()
                Load_frame_app = tk.Frame(windwo_load)                                                     
                Load_frame_app.pack(side= tk.TOP)                                                             
                progress = ttk.Progressbar(Load_frame_app, orient="horizontal", 
                                                length=500,mode="determinate")         
                progress.pack()   
                progress["value"] = 0
                progress["maximum"] = len(OBJ.FILES_LIST) 
                count = 0
                txt_res =""
                for file in OBJ.FILES_LIST:
                    count += 1
                    progress["value"] = count
                    if file == " ":
                        continue
                    try:
                        index = file[::-1].find("/")
                        
                        label_name_file_load["text"] = file[-index::]
                        result= Recording_text.text_recognition_res(file, self.lng)  
                    except:
                        label_error = tk.Label(windwo_load, text = "Something went wrong. Perhaps the quality of the image is not subject to recognition")
                        label_error.pack()
                        time.sleep(3)
                        return
                    txt_res+= result
                    if result == "":
                        label_error_2 = tk.Label(windwo_load, text = "Some files do not contain a text value or are not of good quality.", fg= "red")
                        label_error_2.pack()
                        time.sleep(3)
                        return
                    label_["text"] = "Processing of the final result"
                windwo_load.quit()

            
            windwo_load.title("Recognition process...")
            thread  = threading.Thread(target=action, kwargs= {"windwo_load":windwo_load}).start()
            windwo_load.mainloop()
            
            self.master.deiconify()
            
            window = tk.Tk()
            label = tk.Label(window)
            label["text"] = txt_res
            if label["text"] == "":
                window.destroy()
                windwo_load.destroy()
                
                return
            label.pack()
            windwo_load.destroy()
            window.mainloop()
            
        def recognize_file():
            
            file = filedialog.askopenfile()
            if file == "" or file == None:
                return
            window_language = tk.Toplevel()
            window_language.geometry("180x90+900+500")
            window_language.resizable(False, False)
            
            def on_enter(e):
                e.widget['background'] = '#006B9E'                
            def on_leave(e):
                e.widget['background'] = 'SystemButtonFace'
            def on_click_lng(event, arg):
                self.lng = arg
                window_language.destroy()
                window_language.quit()
                
            label_ =  tk.Label(window_language , text= "Select a language:", font = 50)
            label_.pack()
            label_rus =  tk.Label(window_language , image= self.img_rus,  cursor="hand2")
            label_rus.pack(side = tk.LEFT, padx=2)
            label_eng =  tk.Label(window_language ,  image= self.img_eng, cursor="hand2")
            label_eng.pack(side = tk.LEFT, padx=2)
            label_heb =  tk.Label(window_language , image= self.img_he, cursor="hand2")
            label_heb.pack(side = tk.LEFT, padx=2)
            
            label_rus.bind("<Enter>", on_enter)
            label_rus.bind("<Leave>", on_leave)        
            label_eng.bind("<Enter>", on_enter)
            label_eng.bind("<Leave>", on_leave)        
            label_heb.bind("<Enter>", on_enter)
            label_heb.bind("<Leave>", on_leave)        
            label_rus.bind("<Button-1>",lambda event, arg="ru": on_click_lng(event, arg))
            label_eng.bind("<Button-1>", lambda event, arg="en": on_click_lng(event, arg))
            label_heb.bind("<Button-1>", lambda event, arg="he": on_click_lng(event, arg))
            window_language.mainloop()
            
            if self.lng == None:
                return
            windwo_load = tk.Tk()
            windwo_load.geometry(("500x80+750+500"))
            windwo_load.resizable(False, False)
            
            ##
            self.master.withdraw()
            def action(windwo_load):
                global txt_res
                label_ = tk.Label(windwo_load, text = "Wait for the operation to be completed", font = "Arial 10 bold")
                label_.pack()
                label_name_file_load = tk.Label(windwo_load)
                label_name_file_load.pack()
                Load_frame_app = tk.Frame(windwo_load)                                                     
                Load_frame_app.pack(side= tk.TOP)                                                             
                progress = ttk.Progressbar(Load_frame_app, orient="horizontal", 
                                                length=500,mode="determinate")         
                progress.pack()   
                progress["value"] = 0
                progress["maximum"] = len(OBJ.FILES_LIST) 
                count = 0
                txt_res =""
                
                
                try:
                    index = file.name[::-1].find("/")
                        
                    label_name_file_load["text"] = file.name[-index::]
                    result= Recording_text.text_recognition_res(file.name, self.lng)  
                    count += 1
                    progress["value"] = count
                    time.sleep(1)
                    
                except:
                    label_error = tk.Label(windwo_load, text = "Something went wrong. Perhaps the quality of the image is not subject to recognition")
                    label_error.pack()
                    time.sleep(3)
                    return
                txt_res+= result
                if result == "":
                    label_error_2 = tk.Label(windwo_load, text = "Some files do not contain a text value or are not of good quality.", fg= "red")
                    label_error_2.pack()
                    time.sleep(3)
                    return
                label_["text"] = "Processing of the final result"
                windwo_load.quit()
            ##
            windwo_load.title("Recognition process...")
            thread  = threading.Thread(target=action, kwargs= {"windwo_load":windwo_load}).start()
            windwo_load.mainloop()
            
            self.master.deiconify()
            
            window = tk.Tk()
            label = tk.Label(window)
            label["text"] = txt_res
            if label["text"] == "":
                window.destroy()
                windwo_load.destroy()
                return
            label.pack()
            windwo_load.destroy()
            window.mainloop()
            
        
        self.Label_get = ttk.Button(self.Handler, text = "Recognize a file",  cursor="hand2", command=recognize_file)
        self.Label_get.grid(row=0, column=0, columnspan=2, ipadx=71, ipady=4, padx=5, pady=5)
            
        
        self.Label_get = ttk.Button(self.Handler, text = "Recognize a project",  cursor="hand2", command=thred_process)
        self.Label_get.grid(row=1, column=0, columnspan=2, ipadx=60, ipady=4, padx=5, pady=5)
        
        
    
        def thread_process_2():
            global txt_res
            try:
                OBJ.FILES_LIST.remove(" ")
            except:
                pass
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " " or self.label_pr_act["text"]== None:
                messagebox.showerror(title="Project not found", message="Select or upload the project to continue.")
                return
            elif OBJ.FILES_LIST == []:
                messagebox.showerror(title="Files not found", message="There are no files in the project.")
                return
            def on_enter(e):
                e.widget['background'] = '#006B9E'                
            def on_leave(e): 
                e.widget['background'] = 'SystemButtonFace'
            def on_click_lng(event, arg):
                self.lng = arg
                window_language.destroy()
                window_language.quit()
                
            window_language = tk.Toplevel()
            window_language.geometry("180x90+900+500")
            window_language.resizable(False, False)
            
            label_ =  tk.Label(window_language , text= "Select a language:", font = 50)
            label_.pack()
            label_rus =  tk.Label(window_language , image= self.img_rus,  cursor="hand2")
            label_rus.pack(side = tk.LEFT, padx=2)
            label_eng =  tk.Label(window_language ,  image= self.img_eng, cursor="hand2")
            label_eng.pack(side = tk.LEFT, padx=2)
            label_heb =  tk.Label(window_language , image= self.img_he, cursor="hand2")
            label_heb.pack(side = tk.LEFT, padx=2)
            
            label_rus.bind("<Enter>", on_enter)
            label_rus.bind("<Leave>", on_leave)        
            label_eng.bind("<Enter>", on_enter)
            label_eng.bind("<Leave>", on_leave)        
            label_heb.bind("<Enter>", on_enter)
            label_heb.bind("<Leave>", on_leave)        
            label_rus.bind("<Button-1>",lambda event, arg="ru": on_click_lng(event, arg))
            label_eng.bind("<Button-1>", lambda event, arg="en": on_click_lng(event, arg))
            label_heb.bind("<Button-1>", lambda event, arg="he": on_click_lng(event, arg))
            window_language.mainloop()
            if self.lng == None:
                return
            
            
            windwo_load = tk.Tk()
            windwo_load.geometry(("500x80+750+500"))
            windwo_load.resizable(False, False)
            self.master.withdraw()
            def action(windwo_load):
                global txt_res
                label_ = tk.Label(windwo_load, text = "Wait for the operation to be completed", font = "Arial 10 bold")
                label_.pack()
                label_name_file_load = tk.Label(windwo_load)
                label_name_file_load.pack()
                Load_frame_app = tk.Frame(windwo_load)                                                     
                Load_frame_app.pack(side= tk.TOP)                                                             
                progress = ttk.Progressbar(Load_frame_app, orient="horizontal", 
                                                length=500,mode="determinate")         
                progress.pack()   
                progress["value"] = 0
                progress["maximum"] = len(OBJ.FILES_LIST) 
                count = 0
                txt_res = []
                for file in OBJ.FILES_LIST:
                    count += 1
                    progress["value"] = count
                    if file == " ":
                        continue
                    try:
                        index = file[::-1].find("/")
                        
                        label_name_file_load["text"] = file[-index::]
                        result= Recording_text.text_recognition_res(file, self.lng)  
                    except:
                        label_error = tk.Label(windwo_load, text = "Something went wrong. Perhaps the quality of the image is not subject to recognition")
                        label_error.pack()
                        time.sleep(3)
                        txt_res = []
                        return
                    txt_res.append(result)
                    if result == []:
                        label_error_2 = tk.Label(windwo_load, text = "Some files do not contain a text value or are not of good quality.", fg= "red")
                        label_error_2.pack()
                        time.sleep(3)
                        return
                label_["text"] = "Processing of the final result"
                windwo_load.quit()

            
            windwo_load.title("Recognition process...")
            thread  = threading.Thread(target=action, kwargs= {"windwo_load":windwo_load}).start()
            windwo_load.mainloop()
            self.master.deiconify()
            
            
            for ready_text in txt_res:
                window = tk.Tk()
                label = tk.Label(window)
                label["text"] = ready_text
                if label["text"] == "":
                    window.destroy()
                    windwo_load.destroy()
                    return
                label.pack()
                windwo_load.destroy()
        
        self.Label_get2 = ttk.Button(self.Handler, text = "Recognize separately",  cursor="hand2", command=thread_process_2)
        self.Label_get2.grid(row=2, column=0, columnspan=2, ipadx=56, ipady=4, padx=5, pady=5)
        self.Additional_settings = tk.LabelFrame(self.Frame_Handler,text = "Additional settings",font = "Arial 12 bold ", width= 247, height= 325)                #
        self.Additional_settings.place(x= 1, y= 161)
        

        
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
        self.blocker_new_pr = None
        self.save_text_new_pr = None
        self.Recording_Frame()
        self.Handler_Frame()
        
        
    def save_pr_and_file(self):
        if self.pr_activion:
            if self.label_pr_act["text"] == "New Project":
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
                    if Entry.get() == "" :
                        
                        messagebox.showerror(title="Creation error", message= "Enter the correct project name to create")
                        return
                    
                    
                    self.save_text_new_pr = Entry.get()
                    add_new_project = self.local_url + f"/projects/{self.save_text_new_pr}"
                    
                    Path(add_new_project).mkdir(parents=True, exist_ok=True)
                    Processed_list = []
                    for copy_file in OBJ.FILES_LIST:

                        if copy_file == " ":
                                continue
                        
                        
                        shutil.copy(str(copy_file), f"{self.local_url}/projects/{self.save_text_new_pr}")
                        res_copy = copy_file.replace("New Project", self.save_text_new_pr)
                        Processed_list.append(res_copy)
                    
                    OBJ.FILES_LIST = Processed_list
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
                shutil.rmtree(f"{self.local_url}/projects/New Project")
                OBJ.upload_bool_ = False
                self.pr_activion = False
                self.new_pr_bool = False
                
                self.Recording_Frame()

                return
                
                
            else:
                files_pr = OBJ.FILES_LIST
                name_pr = self.label_pr_act["text"]
                
                for copy_file in files_pr:
                    if copy_file == " ":
                        continue  
                    try:      
                        shutil.copy(str(copy_file), f"{self.local_url}/projects/{name_pr}")
                    except shutil.SameFileError:
                        pass
                self.Frame_recording.destroy()
                self.Frame_Files.destroy()
                
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                self.Frame_Files.place(x= 1, y= 235)      
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                OBJ.upload_bool_ = False
                OBJ.FILES_LIST.clear()
                self.pr_activion = False
                
                self.Recording_Frame()
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
                    pr_load()
                    try:
                        index= list(self.listbox["values"]).index(self.selected_before)
                        self.listbox.current(index)
                    except:
                        self.selected_before = self.listbox.get()
                    self.label_pr_act = tk.Label(self.Frame_Recording, text = self.selected_before,  font= "Arial 14") #
                    self.label_pr_act.place(x=126, y =37)
                    self.selected_before = None
                    self.new_pr_bool = False
                    return
                
                if self.label_pr_act["text"] == "New Project":

                    clean_pr_new = list(self.listbox["values"])
                    try:
                        clean_pr_new.remove("New Project")
                    except:
                        pass
                    try:
                        index= clean_pr_new.index(self.selected_before) # 
                    except:
                        index = clean_pr_new.index(self.listbox.get())
                    self.listbox.destroy()
                    self.listbox = ttk.Combobox(self.Frame_Recording,values= clean_pr_new)
            
                    self.listbox.current(index)
                    
                    self.listbox.place(x = 10, y = 130, width=300)
                    self.listbox.bind("<<ComboboxSelected>>", selected)
                    self.selected_before = None
                    self.blocker_new_pr = None
                    try:
                        shutil.rmtree(self.local_url +f"/projects/New Project") 
                    except:
                        pass
                    
                for elem in urls_project_files():
                    if elem == self.listbox.get() or elem == self.selected_before:
                        
                        check_files = glob.glob(glob.escape(rf"{self.local_url}/projects/{elem}") + "/*")
                        
                        res_files= []
                        for x in check_files:
                            res_files.append(x.replace("\\", "/"))
                        self.label_pr_act.destroy()
                        self.label_pr_act = tk.Label(self.Frame_Recording,  font= "Arial 14") #
                        self.label_pr_act.place(x=126, y =37)
                        self.label_pr_act["text"] = self.listbox.get() 
                        self.Frame_Files.destroy()
                        self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250)                #
                        self.Frame_Files.place(x= 1, y= 235)      
                        OBJ(self.Frame_Files, self.Frame_Recording).load_frame(res_files)
                        break
            if self.pr_activion:
                if self.label_pr_act["text"] == "New Project":
                        answer = messagebox.askyesno(title="Save Changes", message= "Changes have been detected do you want to save them?")              
                        if answer:
                            self.selected_before = self.listbox.get()
                            self.save_pr_and_file()
                            OBJ.upload_bool_ = False
                            self.pr_activion = False     
                                                    
                            messagebox.showinfo(title="The project is saved", message= "Your project has been saved successfully!")
                            
                        else:
                            if self.label_pr_act["text"] == "New Project":
                                index= list(self.listbox["values"]).index("New Project")
                                list_res =  list(self.listbox["values"])
                                self.selected_before = self.listbox.get()
                                del list_res[index]
                                index_cur = list_res.index(self.selected_before)
                                self.listbox.destroy()                        
                                self.listbox = ttk.Combobox(self.Frame_Recording,values= list_res)
                                self.listbox.current(index_cur)
                                self.listbox.place(x = 10, y = 130, width=300)
                                self.listbox.bind("<<ComboboxSelected>>", selected)
                            OBJ.upload_bool_ = False
                            self.pr_activion = False
                            pr_load() 
                else:
                    self.selected_before = self.listbox.get()
                    OBJ.upload_bool_ = False
                    self.pr_activion = False
                    

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
        label = tk.Label(self.Frame_Recording,text = "Select a project: ", font= "Arial 12")
        label.place(x = 10, y = 100)
        
        
        
        self.listbox = ttk.Combobox(self.Frame_Recording,values= urls_project_files() )
        if self.new_pr_bool == True:
            self.listbox.insert(0, "New Project")
            index= list(self.listbox["values"]).index("New Project")
            self.listbox.current(index)
            

        self.listbox.bind("<<ComboboxSelected>>", selected)
        self.listbox.place(x = 10, y = 130, width=300)  
        self.listbox['state'] = 'readonly'  
        return
            
            
            
            
            
        
    def Handler_Frame(self):
        def Remove_pr():
            
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " " or self.label_pr_act["text"]== None:
                messagebox.showerror(title="Project not found", message="Select or upload the project to continue.")
                return
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
                    self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10 bold")
                    self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
                    
                    self.label_pr_act["text"] = ""
                    self.Recording_Frame()
                    messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                    
                else:
                    return
            
        self.Remove_a_project = ttk.Button(self.Additional_settings, text = "Remove a project",  cursor="hand2", command=Remove_pr)
        self.Remove_a_project.grid(row=0, column=0, columnspan=2, ipadx=65, ipady=4, padx=5, pady=5)
        
        
        def Remove_all_files():
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " ":
                messagebox.showerror(title="Project not found", message="Select or upload the project to continue.")
            else:
                answer = messagebox.askyesno(title="Remove process", message= "Are you sure you want to remove all the files of this project?")
                if answer:
                    if self.label_pr_act["text"] == "New Project":
                        messagebox.showwarning(title="Session error", message= "Please delete or save the current project to continue the operation.")
                        return
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
                    self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10")
                    self.label_info_fr_file.pack()
                    OBJ.FILES_LIST = []
                    messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                    
                else:
                    return
        
        self.Remove_all_files = ttk.Button(self.Additional_settings, text = "Remove all files",  cursor="hand2", command= Remove_all_files)
        self.Remove_all_files.grid(row=1, column=0, columnspan=2, ipadx=70, ipady=4, padx=5, pady=5)
        
        
        def Remove_all_pr():
            
            answer = messagebox.askyesno(title="Remove process", message= "Are you sure you want to remove all projects?")
            if answer: 
                if self.label_pr_act["text"] == "New Project":
                    messagebox.showwarning(title="Session error", message= "Please delete or save the current project to continue the operation.")
                    return
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
                self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10 bold")
                self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
                messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                
            else:
                return
            
        
        self.Remove_all_projects = ttk.Button(self.Additional_settings, text = "Remove all projects",  cursor="hand2", command=Remove_all_pr)
        self.Remove_all_projects.grid(row=2, column=0, columnspan=2, ipadx=59, ipady=4, padx=5, pady=5)
        
        
        def upload_project():
            falder = filedialog.askdirectory()
            if falder == None or falder == "" :
                return
            
            index = 0


            files_j = glob.glob(f"{falder}/*.jpg")
            files_p = glob.glob(f"{falder}/*.png")
            files_no_ready = files_j + files_p
            files = []
            for file in files_no_ready:
                files.append(file.replace("\\", "/"))
            if files == []:
                
                messagebox.showerror(title="Nothing found", message= "No photos found in this folder")
                return 
            
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
            name_pr = self.label_pr_act["text"]
            Path(self.local_url +f"/projects/{name_pr}").mkdir(parents=True, exist_ok=True)
            list_res =  list(self.listbox["values"])
            list_res.append(name_pr)
            self.listbox["values"] = list_res
            index_frame_selected= list(self.listbox["values"]).index(name_pr)
            self.listbox.current(index_frame_selected)
            OBJ(self.Frame_Files, self.Frame_Recording).upload_frame(files, name_pr)         
            
            def label_animation_add():
                canvas.destroy()
            
            width= 210
            height=30
            canvas =  tk.Canvas(self.Frame_Instruction, bg = "#ccffcc", highlightbackground = "#ADFFAD" , height= height, width= width)
            canvas.create_text(width/2, height/2, fill="black", text = f"A new project has been created!", font= "@yugothic 9")
            canvas.place(relx=0.10, rely=0.88)
            canvas.after(2000, label_animation_add)

        self.Upload_a_project = ttk.Button(self.Additional_settings, text = "Upload a project", cursor="hand2", command= upload_project)
        self.Upload_a_project.grid(row=3, column=0, columnspan=2, ipadx=67, ipady=4, padx=5, pady=5)
        
        def add_new_pr():
            
            if self.pr_activion == False:
                
                if self.blocker_new_pr == None:
                    self.blocker_new_pr = False
                else:
                    if OBJ.upload_bool_ == False:
                        messagebox.showerror(title="Repeated operation", message= "This project has already been created")
                        return
                    else:
                        answer = messagebox.askyesno(title="The saving process", message= "Before creating a new project, do you want to save the current one?")
                        if answer:
                            save()
                            
                            OBJ.upload_bool_ = False
                            self.pr_activion = False
                            self.blocker_new_pr = None
                        else:
                            OBJ.FILES_LIST = []
                            OBJ.upload_bool_ = False
                            self.pr_activion = False
                            self.blocker_new_pr = None
                            add_new_pr()
                            return
                        
                """def on_click_lng(event, arg):
                    self.lng = arg
                    window_language.quit()
                """
                OBJ.FILES_LIST = []
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
                self.label_pr_act = tk.Label(self.Frame_Recording, text = "New Project", font= "Arial 14") #
                self.label_pr_act.place(x=126, y =37)
                self.label_pr_act["text"] = "New Project"
                
                self.new_pr_bool = True
                self.pr_activion = False
                self.Recording_Frame()
                
                def label_animation_add():
                   canvas.destroy()
                    
                width= 210
                height=30
                canvas =  tk.Canvas(self.Frame_Instruction, bg = "#ccffcc", highlightbackground = "#ADFFAD" , height= height, width= width)
                canvas.create_text(width/2, height/2, fill="black", text = f"A new project has been created!", font= "@yugothic 9")
                canvas.place(relx=0.10, rely=0.88)
                canvas.after(2000, label_animation_add)
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
            if OBJ.FILES_LIST == [] :
                messagebox.showerror(title="Your project is empty!", message= "Add files to save the project")
                return
            if self.label_pr_act["text"] == "New Project":
                self.pr_activion = True        
                self.save_pr_and_file()
                try:
                    shutil.rmtree(f"{Example.local_url}/projects/New project")
                except:
                    pass
                clean_pr_new= list(self.listbox["values"])
                index = clean_pr_new.index(self.save_text_new_pr)
                self.Frame_recording.destroy()
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235) #
                self.Frame_recording.place(x= 1, y= 1)
                self.new_pr_bool = False
                self.pr_activion = False
                self.blocker_new_pr = None
                OBJ.upload_bool_ = False
                self.Recording_Frame()
                self.label_pr_act = tk.Label(self.Frame_Recording,  font= "Arial 14") #
                self.label_pr_act.place(x=126, y =37)
                self.label_pr_act["text"] = self.save_text_new_pr
                self.listbox.current(index)
                self.save_text_new_pr = None
                self.selected_before = self.save_text_new_pr
                messagebox.showinfo(title="Successfully!", message= "The project has been saved successfully")
            else:
                messagebox.showinfo(title= "Repeated operation", message= "Saved projects are automatically saved.")
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
                    try:
                        shutil.rmtree(f"{Example.local_url}/projects/New project")
                        app.master.destroy()
                    except:
                        pass
                else:
                    try:
                        shutil.rmtree(f"{Example.local_url}/projects/New project")
                        app.master.destroy()
                        return
                    except:
                        pass
            else:
                app.master.destroy()
        
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.geometry("845x510+550+300")
    
    #window.wm_attributes('-transparentcolor','red')
    window.mainloop()
    
if __name__ == "__main__":
    main()