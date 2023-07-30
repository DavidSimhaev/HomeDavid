import glob
import tkinter as tk
from tkinter import messagebox, ttk, filedialog, Listbox
import os
import shutil
from PIL import Image, ImageTk
from pathlib import Path
from Frame_Files import Files

from check_width_and_height import Image_ch
class Example(tk.Frame):
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    def __init__(self):
        super().__init__()
        
        self.img_panda = tk.PhotoImage(file = rf"{self.local_url}/image/panda.png" ).subsample(3,3)
        self.img_logo = tk.PhotoImage(file = rf"{self.local_url}/image/logo.png" )
        self.icon_menu = None
        self.icon_files = None
        
        
        self.master.title("Panda Recognize Progam")
        self.Frame_app = tk.Frame()
        self.Frame_app.pack(side = tk.TOP)
        
        
        
        ##################################  ИНСТРУКЦИЯ    ###################################################
        self.Frame_Instruction = tk.Frame(self.Frame_app, width=250, height=460, bg='#CCCCFF')              #
        self.Frame_Instruction.pack(side = tk.LEFT)                                                         #
        self.label_img_panda = tk.Label(self.Frame_Instruction ,image= self.img_panda , bg= "#CCCCFF")      #
        self.label_img_panda.place(x=40, y =18)                                                             #
        self.label_logo = tk.Label(self.Frame_Instruction ,image= self.img_logo, bg= "#CCCCFF")             #
        self.label_logo.place(x=1, y =192)                                                                  #
        #####################################################################################################

        
        
        
        
        ##################################  РЕДАКТИРОВАНИЕ    ###############################################################################################################
        self.Frame_Recording = tk.Frame(self.Frame_app, width=342, height=460, bg="#CCCCFF")                                                                                #
        self.Frame_Recording.pack(side = tk.LEFT)                                                                                                                           #
        self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 210, bg= "#CCCCFF") #
        self.Frame_recording.place(x= 1, y= 1)                                                                                                                              #
        self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 235, bg= "#CCCCFF")                #
        self.Frame_Files.place(x= 1, y= 210)                                                                                                                                #
        #####################################################################################################################################################################
        
            
        
            
        ##################################  ОБРАБОТЧИК    ###################################################            
        self.Frame_Handler = tk.Frame(self.Frame_app, width=250, height=460, bg='#CCCCFF')##E0B0FF          #
        self.Frame_Handler.pack(side = tk.LEFT)                                                             #
        #####################################################################################################


        ################################## ЗАГРУЗКА ########################################################
        self.Load_frame_app = tk.Frame(bg = "#CCCCFF")                                                     #
        self.Load_frame_app.pack(side= tk.TOP)                                                             #
        self.label_Load = tk.Label(self.Load_frame_app, width=120, height=1,  text="ЗАГРУЗКА")             #
        self.label_Load.pack()                                                                             #
        ####################################################################################################

class FRAME_RECORDING(Example):
    def __init__(self):
        super().__init__()
        self.img = Image.open(f"{self.local_url}/image/save.png")
        self.bg = ImageTk.PhotoImage(self.img)
        self.remove_selected = []
        self.FilesFRAME = None
        
        ####################################################################################################
        self.label_pr_act = tk.Label(self.Frame_Recording, bg= "#CCCCFF", fg="#6666ff",  font= "Arial 14") #
        self.label_pr_act.place(x=100, y =37)
        self.pr_activion = False                                                                           #
        self.New_Frame_Files = None                                                                        #
        ####################################################################################################
    
        self.Recording_Frame()
    
    
    
    
    
    
        
    
    
    def Recording_Frame(self):
        
        
        
        
        
        
        
        
        def selected(event):
            def pr_load(): 
                self.label_pr_act["text"] = self.listbox.get() 
                
                for elem in urls_project_files():
                    if elem == self.listbox.get():
                        
                        check_files = glob.glob(rf"{self.local_url}/projects/{elem}*/*")
                        res_files= []
                        for x in check_files:
                            res_files.append(x.replace("\\", "/"))
                        self.Frame_Files.destroy()
                        self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 235, bg= "#CCCCFF")                #
                        self.Frame_Files.place(x= 1, y= 210)      
                        self.FilesFRAME = Files(self.Frame_Files, self.Frame_Recording).load_frame(res_files)
                        
                        
                        break
            if self.pr_activion:
                
                    # ПРОВЕРИТЬ ИЗМЕНЕНИЯ , , проверить если список файлов в папке пустой
                        answer = messagebox.askyesno(title="Save Changes", message= "Changes have been detected do you want to save them?")              
                
                        if answer:
                            # СОХРАНИТЬ ПРОЕКТ. ОЧИСТИТЬ , И ЗАГРУЗИТЬ ДРУГОЙ!!!!
                            s = save_pr_and_file()
                            messagebox.showinfo(title="The project is saved", message= "Your project has been saved successfully!")
                            
                            pr_load() 
                            
                            self.pr_activion = False
                        else:
                            self.pr_activion = False       
            else:
                try:
                    if self.FilesFRAME.upload_bool == True:
                        self.pr_activion = True
                        self.FilesFRAME.upload_bool = False
                        selected(event)
                except AttributeError:
                    pass
                
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
                        files_pr = self.FilesFRAME.FILES_LIST
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
                        
                        
                        self.FilesFRAME.FILES_LIST.clear()
                        self.pr_activion = False
                        save_window.destroy()
                        save_window.quit()
                        
                        
                        
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
                    return
        def add_new_pr(event):
            if self.pr_activion == False:
                self.pr_activion= True    
                add_new_project = self.local_url + f"/projects/New_Project"
                Path(add_new_project).mkdir(parents=True, exist_ok=True)
                self.label_pr_act["text"] =  "New_Project"
                self.label_pr_act.place(x = 100, y = 36)
                
                self.Frame_Files.destroy()
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 235, bg= "#CCCCFF")                #
                self.Frame_Files.place(x= 1, y= 210)      
                self.FilesFRAME = Files(self.Frame_Files)
                self.FilesFRAME.add_frame()
                
                
                
            elif self.pr_activion == True:
                # У вас уже есть текущий проект хотите создать новый и сохранить?
                answer = messagebox.askyesno(title="Creating a project", message= "You already have a current project , do you want to save and create a new one?")              
                if answer:
                    save_pr_and_file()
                    # СОХРАНИТЬ ТЕКУЩИЙ ПРОЕКТ И ОБНУЛИТЬ СТАТУС 
                else:
                    return

















        
        
        
        
        label = tk.Label(self.Frame_Recording,bg= "#CCCCFF", fg="#6666ff", text = "Orientation:", font= "Arial 12")
        label.place(x = 10, y = 40)
        label = tk.Label(self.Frame_Recording, bg= "#CCCCFF", fg="#6666ff",text = "Select a project", font= "Arial 12")
        label.place(x = 10, y = 70)
        self.listbox = ttk.Combobox(self.Frame_Recording, width= 50,values= urls_project_files())
        self.listbox.bind("<<ComboboxSelected>>", selected)
        self.listbox.place(x = 10, y = 90)     
        button = tk.Label(self.Frame_Recording, text= "Add new project", relief= tk.GROOVE, cursor="hand2")
        button.place(x = 180, y = 140)
        #self.button_upload = tk.Label(self.Frame_Recording, text= "Upload a project", relief= tk.GROOVE, cursor="hand2")
        #self.button_upload.place(x = 40, y = 140)
        #button.bind("<Button-1>", add_new_pr)
        
        
        





def main():
    window =  tk.Tk()
    app = FRAME_RECORDING()
    
    window.geometry("845x480+550+300")
    
    def on_closing():
        if Files.FILES_LIST == []:
            app.master.destroy()
            return
        else:
            answer = messagebox.askyesno(title="The saving process", message="Do you want to save the result of the current project?")
            if answer:
                
                #save_project()##############################################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                app.master.destroy()
            else:
                shutil.rmtree(f"{Example.local_url}/projects/New_project")
                app.master.destroy()
                return
    
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    #window.wm_attributes('-transparentcolor','red')
    window["bg"] = "#CCCCFF"
    window.mainloop()
    
if __name__ == "__main__":
    main()