import shutil
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage, messagebox ,filedialog, END
import os
from check_width_and_height import Image_ch

class Files:
    FILES_LIST = []
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    upload_bool_ = False
    def __init__(self, new_frame, FRAME_RECORDING):
        self.new_frame = new_frame
        self.image = None   
        self.FRAME_RECORDING = FRAME_RECORDING
        self.img_shove = tk.PhotoImage(file = rf"{self.local_url}/image/shove_.png" )
        self.img = Image.open(f"{self.local_url}/image/shove_.png")
        self.img_shove2 = ImageTk.PhotoImage(self.img)
        self.f = False
        
        super().__init__()
    
    def upload_bool(self):
        change = Files.upload_bool_ = True
        return change



    def upload_frame(self, files, name_pr):
        Files.FILES_LIST = []
        for file in files:
            save_image = Image_ch(file, name_pr).save()
            Files.FILES_LIST.append(save_image) 
        self.c = True
        self.list_files_from_pr(self.new_frame, self.FRAME_RECORDING)
    
    
        
    def load_frame(self, files):
        Files.FILES_LIST = []
        Files.FILES_LIST.extend(files)
        self.c = True
        self.list_files_from_pr(self.new_frame, self.FRAME_RECORDING)

    
    def add_frame(self):    
        Files.FILES_LIST = []
        Files.FILES_LIST.append(" ")
        
        return
        
    
    def add_file(self, name_pr):
        self.name_pr = name_pr
        self.f = True
        self.list_files_from_pr(self.new_frame, self.FRAME_RECORDING)
        
    
    def list_files_from_pr(self, New_Frame_Files, FRAME_RECORDING ):
        
        if self.FILES_LIST != []:
            #По умолчанию по созданию проекта первое значение всегда ровно пробелу 


            
            def on_enter_1(e):
                e.widget['background'] = 'gray'                
            def on_leave_1(e):
                e.widget['background'] = "SystemButtonFace"
            
            
            def new_file():
                files = [('PNG', '*.png'),('JPG', '*.jpg')]
                try:
                    name = filedialog.askopenfilename(filetypes = files,defaultextension=".png", initialdir= rf"{self.local_url}" )
                except AttributeError:
                    return
                if name == "":
                    return  
                
                save_image = Image_ch(name, self.name_pr).save()
                self.upload_bool()
                
                self.FILES_LIST.append(save_image) 
                f()    
            
            
            def f():
                b = 0 
                def rename_img(event, file_pr):
                    
                    def change_name(event, arg):
                        answer = messagebox.askyesno(message="Are you sure you want to change the name of the project?")
                        if answer:
                            
                            
                            b = 0
                            for el in str(file_pr["elem"]["textvariable"])[::-1]:
                                b+=1
                                if el == "/": 
                                    os.rename(file_pr["elem"]["textvariable"],file_pr["elem"]["textvariable"][:-b]+"/"+rename.get()+".png")
                                    index = self.FILES_LIST.index(str(arg["res_file"]))
                                    self.FILES_LIST[index] = str(file_pr["elem"]["textvariable"][:-b]+"/"+rename.get()+".png")
                                    New_Frame_Files.destroy()
                                    Frame_Files = tk.LabelFrame(FRAME_RECORDING  ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 250)                #
                                    Frame_Files.place(x= 1, y= 235)   
                                    print(self.FILES_LIST)
                                    self.list_files_from_pr(Frame_Files, FRAME_RECORDING)   
                                    w.destroy()
                                    
                                    break       
                        else:                   
                            w.destroy()
                    w = tk.Tk()              
                    w.geometry("150x40")      
                    rename = tk.Entry(w, font= 50)
                    rename.delete(0,END)
                    res = file_pr["elem"]["textvariable"]
                    rename.insert(0, str(res)[-10::])    
                    rename.place(width=150, height=40)
                    data = {"res_file": res}
                    rename.bind("<Return>",lambda event, arg=data: change_name(event, arg))
            
                def func_c(event, arg):
                        w = tk.Toplevel()
                        
                        arg["self"].image = PhotoImage(file = arg["elem"]["textvariable"])
                        label_img = tk.Label(w, image=arg["self"].image).pack()
                        
                        w.mainloop()
                frame2 = tk.Frame(New_Frame_Files, bd=3, relief=tk.FLAT)
                frame2.grid(row=3, column=0, sticky=tk.NW)   
                canvas = tk.Canvas(frame2)
                canvas.grid(row=0, column=0)
                # Create a vertical scrollbar linked to the canvas.
                vsbar = tk.Scrollbar(frame2 , orient=tk.VERTICAL, command=canvas.yview)
                vsbar.grid(row=0, column=1, sticky=tk.NS)
                canvas.configure(yscrollcommand=vsbar.set)
                widget_frame = tk.Frame(canvas)
                for file in self.FILES_LIST:
                    if file == " ":
                        continue
                    Label_name = tk.Label(widget_frame, textvariable= file , text = file[-10::], cursor="hand2")
                    Label_name.grid(row= b ,column=0, padx=(1, 220))
                    
                    
                    Icon_shove = tk.Label(widget_frame ,image=self.img_shove, cursor="hand2")
                    Icon_shove.grid(row= b , column=0, padx=(250, 1))
                    
                    Label_name.bind("<Enter>", on_enter_1)
                    Label_name.bind("<Leave>", on_leave_1)        
                    
                    Icon_shove.bind("<Enter>", on_enter_1)
                    Icon_shove.bind("<Leave>", on_leave_1)        

                    b+=1
                    
                    data= {"elem":Label_name , "self": self }
                    
                    Label_name.bind("<Button-1>", lambda event, arg=data: rename_img(event, arg))    
                    Icon_shove.bind("<Button-1>", lambda event, arg=data: func_c(event, arg))
                    
                    canvas.create_window((0,0), window=widget_frame, anchor=tk.NW)
                    widget_frame.update_idletasks()
                    bbox = canvas.bbox(tk.ALL)
                    canvas.configure(scrollregion=bbox, width=290, height=220)
                
            
            if self.f == True:
                new_file()
                return
            if self.c == True:
                    
                f()
                return
                
        elif self.FILES_LIST == []:
            if self.f == True:
                self.FILES_LIST.append(" ")
                self.list_files_from_pr( New_Frame_Files, FRAME_RECORDING )
            else:
                label = tk.Label(New_Frame_Files, text= "В этом проекте не имеются файлы") 
                label.pack()
                
                        
                    
                