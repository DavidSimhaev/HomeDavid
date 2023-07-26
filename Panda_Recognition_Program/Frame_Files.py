import glob
import tkinter as tk
from tkinter import filedialog
import os
from check_width_and_height import Image_ch

b = 0
class Files(tk.Frame):
    FILES_LIST = []
    def __init__(self, file):
        super().__init__()
        self.file = file
        self.local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")

    
    def add_file(self, Frame_Files):
        self.FILES_LIST.append(self.file)
        self.list_files_from_pr(Frame_Files)
        

    def list_files_from_pr(self, Frame_Files):
            
            
            
        if self.FILES_LIST != []:
            """# По умолчанию по созданию проекта первое значение всегда ровно пробелу 
            def on_enter(e):
                e.widget['background'] = 'gray'                
            def on_leave(e):
                e.widget['background'] = 'SystemButtonFace'"""
            def new_file(event):
                files = [('PNG', '*.png'),('JPG', '*.jpg')]
                try:
                    name = filedialog.askopenfilename(filetypes = files, defaultextension = files, initialdir= rf"{self.local_url}" )
                except AttributeError:
                    return
                if name == "":
                    return  
                save_image = Image_ch(name).save()
                           
                self.FILES_LIST.append(save_image) 
                f()
                
                
            Label = tk.Label(Frame_Files, text = "Add a file",  relief= tk.GROOVE, cursor="hand2")
            Label.grid(row= 0 , columnspan=5, sticky= tk.SE, padx=70 )

            """Label.bind("<Enter>", on_enter)
            Label.bind("<Leave>", on_leave)"""
            Label.bind("<Button-1>", new_file)
            
            
                
            master_frame = tk.Frame(Frame_Files, bd=3, relief=tk.RIDGE, bg= "#CCCCFF")
            master_frame.grid(columnspan=5)
            master_frame.columnconfigure(0, weight=1)
            frame2 = tk.Frame(master_frame, bd=2, relief=tk.FLAT, bg= "#CCCCFF")
            frame2.grid(row=3, column=0, sticky=tk.NW)   
            canvas = tk.Canvas(frame2, bg= "#CCCCFF")
            canvas.grid(row=0, column=0)
            # Create a vertical scrollbar linked to the canvas.
            vsbar = tk.Scrollbar(frame2, bg= "#CCCCFF" , orient=tk.VERTICAL, command=canvas.yview)
            vsbar.grid(row=0, column=1, sticky=tk.NS)
            canvas.configure(yscrollcommand=vsbar.set)
            widget_frame = tk.Frame(canvas, bg= "#CCCCFF")
                            
            def f():
                global b
                b+=1
                
                label_name = tk.Label(widget_frame, text = self.FILES_LIST[b][-10::] , bg= "#CCCCFF") 
                label_name.grid(row=b-1, column=0)
                
            canvas.create_window((0,0), window=widget_frame, anchor=tk.NW)
            widget_frame.update_idletasks()
            bbox = canvas.bbox(tk.ALL)
            canvas.configure(scrollregion=bbox, width=310, height=190)
                        
                    
                