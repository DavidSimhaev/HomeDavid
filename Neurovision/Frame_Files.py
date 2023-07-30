import glob
import tkinter as tk
from tkinter import messagebox ,filedialog, END
import os
from check_width_and_height import Image_ch

class Files:
    FILES_LIST = []
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    def __init__(self, new_frame, FRAME_RECORDING):
        self.new_frame = new_frame
        self.upload_bool = False
        self.FRAME_RECORDING = FRAME_RECORDING
        self.img_shove = tk.PhotoImage(file = rf"{self.local_url}/image/shove_.png" )
        self.icon_del = tk.PhotoImage(file = rf"{self.local_url}/image/delete_icon.png" )
        
        super().__init__()
        
        
    def load_frame(self, files):
        self.FILES_LIST = []
        self.FILES_LIST.extend(files)
        self.c = True
        self.list_files_from_pr(self.new_frame, self.FRAME_RECORDING)
    
    
    def add_frame(self):    
        self.list_files_from_pr(self.new_frame, self.FRAME_RECORDING)
        
      
    
    
    def list_files_from_pr(self, New_Frame_Files, FRAME_RECORDING ):
            
        
        
        
        
        def clone_widget(widget, master=None):
                            
                            # Get main info
                                parent = master if master else widget.master
                                cls = widget.__class__

                                # Clone the widget configuration
                                cfg = {key: widget.cget(key) for key in widget.configure()}
                                cloned = cls(parent, **cfg)

                                # Clone the widget's children
                                for child in widget.winfo_children():
                                    child_cloned = clone_widget(child, master=cloned)
                                    if child.grid_info():
                                        grid_info = {k: v for k, v in child.grid_info().items() if k not in {'in'}}
                                        child_cloned.grid(**grid_info)
                                    elif child.place_info():
                                        place_info = {k: v for k, v in child.place_info().items() if k not in {'in'}}
                                        child_cloned.place(**place_info)
                                    else:
                                        pack_info = {k: v for k, v in child.pack_info().items() if k not in {'in'}}
                                        child_cloned.pack(**pack_info)

                                return cloned  
        
        
        
        
        
        
        
        

            
        if self.FILES_LIST != []:
            # По умолчанию по созданию проекта первое значение всегда ровно пробелу 
            def on_enter(e):
                e.widget['background'] = 'gray'                
            def on_leave(e):
                e.widget['background'] = 'SystemButtonFace'

            
            def on_enter_1(e):
                e.widget['background'] = 'gray'                
            def on_leave_1(e):
                e.widget['background'] = "#CCCCFF"
            
            
            def new_file(event):
                files = [('PNG', '*.png'),('JPG', '*.jpg')]
                try:
                    name = filedialog.askopenfilename(filetypes = files, defaultextension = files, initialdir= rf"{self.local_url}" )
                except AttributeError:
                    return
                if name == "":
                    return  
                save_image = Image_ch(name).save()
                self.upload_bool = True
                self.FILES_LIST.append(save_image) 
                f()    
            Label = tk.Label(New_Frame_Files, text = "Add a file",  relief= tk.GROOVE, cursor="hand2")
            Label.grid(row= 0 , columnspan=5, sticky= tk.SE, padx=70 )
            Label.bind("<Enter>", on_enter)
            Label.bind("<Leave>", on_leave)
            
            
            Label.bind("<Button-1>", new_file)
            self.master_frame = tk.Frame(New_Frame_Files, bd=3, relief=tk.RIDGE, bg= "#CCCCFF")
            self.master_frame.grid(columnspan=5)
            self.master_frame.columnconfigure(0, weight=1)
            self.frame2 = tk.Frame(self.master_frame, bd=2, relief=tk.FLAT, bg= "#CCCCFF")
            self.frame2.grid(row=3, column=0, sticky=tk.NW)   
            self.canvas = tk.Canvas(self.frame2, bg= "#CCCCFF")
            self.canvas.grid(row=0, column=0)
            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(self.frame2, bg= "#CCCCFF" , orient=tk.VERTICAL, command=self.canvas.yview)
            vsbar.grid(row=0, column=1, sticky=tk.NS)
            self.canvas.configure(yscrollcommand=vsbar.set)
            self.widget_frame = tk.Frame(self.canvas, bg= "#CCCCFF")
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
                                    Frame_Files = tk.LabelFrame(FRAME_RECORDING  ,text = "Files", fg="#6666ff",font = "Arial 12 bold ", width= 340, height= 235, bg= "#CCCCFF")                #
                                    Frame_Files.place(x= 1, y= 210)   
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
                
             
                for file in self.FILES_LIST:
                    if file == " ":
                        continue
                    
                    Label_name = tk.Label(self.widget_frame, textvariable= file ,font=10,bg="#CCCCFF", text = file[-10::], cursor="hand2")
                    Label_name.grid(row= b , column=0, padx= 3)
                    Label2 = tk.Label(self.widget_frame, font=10,bg="#CCCCFF", text = "                             ")
                    Label2.grid(row= b , column=1, padx= 3)
                    Icon_shove = tk.Label(self.widget_frame,bg="#CCCCFF" ,image=self.img_shove, cursor="hand2")
                    Icon_shove.grid(row= b , column=2)
                    Icon_del = tk.Label(self.widget_frame,bg="#CCCCFF" ,image=self.icon_del, cursor="hand2")
                    Icon_del.grid(row= b , column=3)
                    
                    #Label_name.bind("<Enter>", on_enter_1)
                    #Label_name.bind("<Leave>", on_leave_1)        
                    
                    Icon_shove.bind("<Enter>", on_enter_1)
                    Icon_shove.bind("<Leave>", on_leave_1)        
                    Icon_del.bind("<Enter>", on_enter_1)
                    Icon_del.bind("<Leave>", on_leave_1)
                    b+=1
                    
                    data= {"elem":Label_name, "self": self }
                    
                    Label_name.bind("<Button-1>", lambda event, arg=data: rename_img(event, arg))    
                    
                    
                    
                    
            if self.c == True:
                f()
            self.canvas.create_window((0,0), window=self.widget_frame, anchor=tk.NW)
            self.widget_frame.update_idletasks()
            bbox = self.canvas.bbox(tk.ALL)
            self.canvas.configure(scrollregion=bbox, width=310, height=190)
        elif len(self.FILES_LIST) == 1 or self.FILES_LIST == []:
            label = tk.Label(New_Frame_Files, text= "В этом проекте не имеются файлы") 
            label.pack()
            
                        
                    
                