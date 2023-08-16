import glob
import threading
import time
import tkinter as tk
from tkinter import messagebox, ttk, filedialog, Listbox, Menu
import os
import shutil
from PIL import Image, ImageTk
from pathlib import Path
from Frame_Files import Files
from frame_easyocr import Recording_text
import subprocess
import ctypes
from pandas.io import clipboard

OBJ = Files
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

switch_value = True
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
        
        
        self.light = tk.PhotoImage(file=rf"{self.local_url}/image/white_bg.png").subsample(1,1)
        self.dark = tk.PhotoImage(file=rf"{self.local_url}/image/black_bg.png").subsample(1,1)
        self.img_panda = tk.PhotoImage(file = rf"{self.local_url}/image/panda.png" ).subsample(3,3)
        self.img_panda_update = tk.PhotoImage(file = rf"{self.local_url}/image/panda_light.png" ).subsample(3,3)
        self.info_logo = tk.PhotoImage(file = rf"{self.local_url}/image/info_logo.png" ).subsample(1,1)
        
        
        
        
        
        self.img_en = tk.PhotoImage(file = rf"{self.local_url}/image/languages/en.png" ).subsample(2,2)
        self.img_fr = tk.PhotoImage(file = rf"{self.local_url}/image/languages/fr.png").subsample(2,2)
        self.img_ja = tk.PhotoImage(file = rf"{self.local_url}/image/languages/ja.png").subsample(2,2)
        
        self.img_ko = tk.PhotoImage(file = rf"{self.local_url}/image/languages/ko.png").subsample(2,2)
        self.img_ru = tk.PhotoImage(file = rf"{self.local_url}/image/languages/ru.png").subsample(2,2)
        self.img_zh = tk.PhotoImage(file = rf"{self.local_url}/image/languages/zh.png").subsample(2,2)
        
        
        
        
        
        
        
        
        self.list_funcs_settings = []
        self.lng = None
        self.master.title("Neurovision v.0.1.2")
        self.Frame_app = tk.Frame()
        self.Frame_app.pack(side = tk.TOP)
        
        self.Frame_Instruction = tk.Frame(self.Frame_app, width=250, height=490)              
        self.Frame_Instruction.pack(side = tk.LEFT)                                                         
        self.label_img_panda = tk.Label(self.Frame_Instruction ,image= self.img_panda)      
        self.label_img_panda.place(x=40, y =18)      
        self.count = 0
        self.copy = tk.PhotoImage(file = rf"{self.local_url}/image/copy.png")
        self.copy2 = tk.PhotoImage(file = rf"{self.local_url}/image/copy_to_pdf.png")
        self.copy3 = tk.PhotoImage(file = rf"{self.local_url}/image/copy_to_txt.png")
        
        self.black_manual = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/black_manual.png")
        self.white_manual = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/white_manual.png")
        self.page_1_black = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-1_black.png")
        self.page_1_white= tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-1_white.png")
        self.page_2_black = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-2_black.png")
        self.page_2_white = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-2_white.png")
        self.page_3_black = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-3_black.png")
        self.page_3_white = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-3_white.png")   
        self.page_4_black = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-4_black.png")   
        self.page_4_white = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/page-4_white.png")   
          
        self.arrow_r = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/arrow_r.png")     
        self.arrow_l = tk.PhotoImage(file = rf"{self.local_url}/image/instruction/arrow_l.png")     
        

        
        
    
        def toggle():
            global switch_value
            all_func = self.list_funcs_settings+ self.list_funcs_settings2
            if switch_value == True:
                self.switch.config(image=self.dark, bg="#26242f",
                            activebackground="#26242f")
                frames = [self.Frame_Instruction, self.Frame_Recording, self.Frame_Files, self.Frame_Handler]
                self.master.configure(bg="#26242f")
                self.label_img_panda.config(bg="#26242f", image=self.img_panda_update)
                self.logo_information.config(bg="#26242f")
                index = 0
                
                def on_enter(e):
                    e.widget['background'] = 'gray'                
                def on_leave(e):
                    e.widget['background'] = "black"
                
                for frame in frames:
                    frame.config(bg="#26242f")
                    for widjet in frame.winfo_children():
                        if "!combobox" in str(widjet):
                            continue
                        try:
                            widjet.config(bg="#26242f" ,fg = "white")
                        except:
                            switch_value = False
                            
                            self.Frame_Files.destroy()
                            self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg="#26242f", fg = "white")                #
                            self.Frame_Files.place(x= 1, y= 235)  
                            OBJ(self.Frame_Files, self.Frame_Recording, switch_value).load_frame(OBJ.FILES_LIST)
                            
                        if "!frame3" in str(widjet):
                            
                            #self.Additional_settings = tk.LabelFrame(self.Frame_Handler,text = "Additional settings",font = "Arial 12 bold ", width= 247, height= 325)                #
                            #self.Additional_settings.place(x= 1, y= 161)
                            
                            
                            
                            for data_frame in widjet.winfo_children():
                                
                                info = data_frame.grid_info()
                                b = 0
                                s = 0
                                Button = tk.Button(widjet, text= data_frame.cget('text'), cursor="hand2", command= all_func[index], bg="black", fg ="white")
                                
                                Button.bind("<Enter>", on_enter)
                                Button.bind("<Leave>", on_leave)    
                                
                                if index == 8:
                                    b+=7
                                    s+=1
                                if index == 9:
                                    s+=1
                                    b+=20
                                    
                                data_frame.destroy()
                                index += 1
                                Button.grid(row = info["row"] , column= info["column"] , columnspan= info["columnspan"] , ipadx= info["ipadx"] + b , ipady= info["ipady"] , padx= info["padx"] , pady= info["pady"]-s )
                switch_value = False

            else:
                self.switch.config(image=self.light, bg="SystemButtonFace",
                            activebackground="SystemButtonFace")
                frames = [self.Frame_Instruction, self.Frame_Recording, self.Frame_Files, self.Frame_Handler]
                self.master["bg"]= "SystemButtonFace"
                self.logo_information.config(bg="SystemButtonFace")
                self.label_img_panda.config(bg="SystemButtonFace", image= self.img_panda )
                
                index = 0
                for frame in frames: 
                    frame.config(bg="SystemButtonFace")
                    for widjet in frame.winfo_children():
                        if "!combobox" in str(widjet):
                            continue
                        try:
                            widjet.config(bg="SystemButtonFace" ,fg = "black")
                        except:
                            switch_value = True
                            self.Frame_Files.destroy()
                            self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg="SystemButtonFace",fg = "black")                #
                            self.Frame_Files.place(x= 1, y= 235)  
                            OBJ(self.Frame_Files, self.Frame_Recording, switch_value).load_frame(OBJ.FILES_LIST)

                        if "!frame3" in str(widjet):
                            
                            for data_frame in widjet.winfo_children():
                                info = data_frame.grid_info()
                                b = 0
                                s= 0
                                Button = ttk.Button(widjet, text= data_frame.cget('text'), cursor="hand2", command= all_func[index])
                                
                                 
                                if index == 8:
                                    b-=7
                                    s+=1
                                if index == 9:
                                    s+=1
                                    b-=20
                                
                                data_frame.destroy()
                                index += 1
                                Button.grid(row = info["row"] , column= info["column"] , columnspan= info["columnspan"] , ipadx= info["ipadx"] + b , ipady= info["ipady"] , padx= info["padx"] , pady= info["pady"]+s )
                    
                                    
                        
                switch_value = True

        def on_enter_s(e):
            e.widget['background'] = 'gray'                
        def on_leave_s(e):
            global switch_value
            if switch_value:
                e.widget['background'] = "SystemButtonFace"
            else:
                e.widget['background'] = "#26242f"
        self.switch = tk.Button(self.Frame_Instruction, image=self.light,
                    bd=0, bg="SystemButtonFace",
                    activebackground="SystemButtonFace",
                    command=toggle,cursor="hand2")
        self.switch.place(x = 174, y = 20 )
        self.switch.bind("<Enter>", on_enter_s)
        self.switch.bind("<Leave>", on_leave_s) 
        

             
        
        def info():
            global switch_value
            self.switch.place_forget()
            def on_enter(e):
                e.widget['background'] = 'gray'                
            def on_leave(e): 
                global switch_value
                if switch_value:
                    e.widget['background'] = "SystemButtonFace"
                else:
                    e.widget['background'] = "#26242f"
                    
                    
            
            if switch_value == False:
                bg_val = "#26242f"
                
                img = self.white_manual
                img1 = self.page_1_white
                img2 = self.page_2_white
                img3 = self.page_3_white
                img4 = self.page_4_white
            else:
                bg_val = "SystemButtonFace"
                
                img = self.black_manual
                img1 = self.page_1_black
                img2 = self.page_2_black
                img3 = self.page_3_black
                img4 = self.page_4_black
            
            
            window = tk.Toplevel(bg= bg_val)
            list_images = [img, img1, img2, img3, img4]
            window.geometry("580x430+670+360")
            window.resizable(False, False)
            
            def back_obj(event):
                self.count-=1
                
                if self.count == 0:
                    arrow_l.pack_forget()
                image_ins["image"] = list_images[self.count]
                
                arrow_r.pack(side="right")
            def next_obj(event):
                self.count+=1    
                if self.count == 4:
                    arrow_r.pack_forget()
                    
                image_ins["image"] = list_images[self.count]
                arrow_l.pack(side="left")
                
            arrow_l = tk.Label(window, image= self.arrow_l, bg= bg_val , cursor="hand2")
            arrow_r = tk.Label(window, image= self.arrow_r, bg= bg_val , cursor="hand2" )
            
            image_ins = tk.Label(window, image= img, bg= bg_val )
            image_ins.pack()
            arrow_r.pack(side="right")
            

            arrow_r.bind("<Button-1>", next_obj)
            arrow_l.bind("<Button-1>", back_obj)
            arrow_r.bind("<Enter>", on_enter)
            arrow_l.bind("<Enter>", on_enter)    
            arrow_r.bind("<Leave>", on_leave) 
            arrow_l.bind("<Leave>", on_leave) 

            def on_closing():
                self.count= 0
                self.switch.place(x = 174, y = 20 )
                window.destroy()
            window.protocol("WM_DELETE_WINDOW", on_closing)
        
        
        
        self.logo_information = tk.Button(self.Frame_Instruction, image=self.info_logo, bd=0, bg="SystemButtonFace", command= info, cursor="hand2" )
        self.logo_information.place(x = 8, y = 19 )
        self.logo_information.bind("<Enter>", on_enter_s)
        self.logo_information.bind("<Leave>", on_leave_s)
        #######################          

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
                global switch_value
                if switch_value:
                    e.widget['background'] = "SystemButtonFace"
                else:
                    e.widget['background'] = "#26242f"
            
            
               
                    
            def on_click_lng(event, arg):
                self.lng = arg
                window_language.destroy()
                window_language.quit()
            
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
                
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
                
            
            
            
            window_language = tk.Toplevel(bg = bg_val)
            window_language.geometry("340x90+840+500")
            window_language.resizable(False, False)
            
            
            
            
            frame_lng_main = tk.Frame(window_language, bg = bg_val)
            label_ =  tk.Label(frame_lng_main , text= "Select a language:", font = 46, bg = bg_val, fg = fg_val)
            label_.pack()
            frame_lng_main.pack(side="top")
            frame_first_lng = tk.Frame(window_language, bg = bg_val)
            label_en =  tk.Label( frame_first_lng, image= self.img_en,  cursor="hand2", bg = bg_val)
            label_en.pack(side = tk.LEFT, padx=2)
            label_fr =  tk.Label(frame_first_lng ,  image= self.img_fr, cursor="hand2", bg = bg_val)
            label_fr.pack(side = tk.LEFT, padx=2)
            label_ja =  tk.Label(frame_first_lng , image= self.img_ja, cursor="hand2", bg = bg_val)
            label_ja.pack(side = tk.LEFT, padx=2)
            label_ko =  tk.Label(frame_first_lng , image= self.img_ko, cursor="hand2", bg = bg_val)
            label_ko.pack(side = tk.LEFT, padx=2)
            label_ru =  tk.Label(frame_first_lng , image= self.img_ru, cursor="hand2", bg = bg_val)
            label_ru.pack(side = tk.LEFT, padx=2)
            label_zh =  tk.Label(frame_first_lng , image= self.img_zh, cursor="hand2", bg = bg_val)
            label_zh.pack(side = tk.LEFT, padx=2, pady= 3)
            frame_first_lng.pack(side="top")
            
            
            label_en.bind("<Enter>", on_enter)
            label_en.bind("<Leave>", on_leave)        
            label_fr.bind("<Enter>", on_enter)
            label_fr.bind("<Leave>", on_leave)        
            label_ja.bind("<Enter>", on_enter)
            label_ja.bind("<Leave>", on_leave)        
            label_ko.bind("<Enter>", on_enter)
            label_ko.bind("<Leave>", on_leave)        
            label_ru.bind("<Enter>", on_enter)
            label_ru.bind("<Leave>", on_leave)        
            label_zh.bind("<Enter>", on_enter)
            label_zh.bind("<Leave>", on_leave)        
            
            
            
            label_en.bind("<Button-1>",lambda event, arg="en": on_click_lng(event, arg))
            label_fr.bind("<Button-1>", lambda event, arg="fr": on_click_lng(event, arg))
            label_ja.bind("<Button-1>", lambda event, arg="ja": on_click_lng(event, arg))
            label_ko.bind("<Button-1>", lambda event, arg="ko": on_click_lng(event, arg))
            label_ru.bind("<Button-1>", lambda event, arg="ru": on_click_lng(event, arg))
            #label_zh.bind("<Button-1>", lambda event, arg="zho": on_click_lng(event, arg))
            
            
            
            
            window_language.mainloop()
            if self.lng == None:
                return
            
            windwo_load = tk.Tk()
            
            windwo_load["bg"] = bg_val
            windwo_load.geometry(("500x80+750+500"))
            windwo_load.resizable(False, False)
            self.master.withdraw()
            
            def action(windwo_load):
                global txt_res
                label_ = tk.Label(windwo_load, text = "Wait for the operation to be completed", font = "Arial 10 bold", bg = bg_val, fg = fg_val)
                label_.pack()
                label_name_file_load = tk.Label(windwo_load, bg = bg_val, fg = fg_val)
                label_name_file_load.pack()
                Load_frame_app = tk.Frame(windwo_load, bg = bg_val)                                                     
                Load_frame_app.pack(side= tk.TOP)                                                             
                progress = ttk.Progressbar(Load_frame_app,orient="horizontal", 
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
                        label_error = tk.Label(windwo_load, bg = bg_val, fg = "red", text = "Something went wrong. Perhaps the quality of the image is not subject to recognition")
                        label_error.pack()
                        time.sleep(3)
                        return
                    txt_res+= result
                    if result == "":
                        label_error_2 = tk.Label(windwo_load, bg = bg_val, text = "Some files do not contain a text value or are not of good quality.", fg= "red")
                        label_error_2.pack()
                        time.sleep(3)
                        return
                    label_["text"] = "Processing of the final result"
                windwo_load.quit()

            
            windwo_load.title("Recognition process...")
            thread  = threading.Thread(target=action, kwargs= {"windwo_load":windwo_load}).start()
            windwo_load.mainloop()
            
            self.master.deiconify()
 
            window = tk.Toplevel(bg = bg_val)
            frame = tk.Frame(window, bg = bg_val)
            label_copy = tk.Label(frame, image = self.copy, cursor="hand2", bg = bg_val, fg = fg_val)
            label_copy2 = tk.Label(frame, image = self.copy2,  cursor="hand2", bg = bg_val, fg = fg_val)
            label_copy3 = tk.Label(frame, image = self.copy3,  cursor="hand2", bg = bg_val, fg = fg_val)
            label_copy.pack(side="left")
            label_copy2.pack(side="left")
            label_copy3.pack(side="left")
            def copy_text_click(event):
                clipboard.copy(txt_res)   
                def label_animation_add():
                    check_mark.destroy()
                check_mark = tk.Label(frame, text = "✓" , fg= "green", font = 38,bg = bg_val)
                check_mark.place(x=1, y = 30)
                check_mark.after(2000, label_animation_add)
                
            label_copy.bind("<Button-1>", copy_text_click )
            label_copy.bind("<Enter>", on_enter)
            label_copy.bind("<Leave>", on_leave)   
            
            
            def PDF_file(event):
                messagebox.showinfo(title="Development will be introduced", message="This function is not yet available")
                return
            label_copy2.bind("<Button-1>", PDF_file )
            label_copy2.bind("<Enter>", on_enter)
            label_copy2.bind("<Leave>", on_leave)  
            
            
            def TXT_file(event):
                Files = [('Text Document', '*.txt')]
                file = filedialog.asksaveasfile(filetypes = Files, defaultextension = Files)
                with open(file.name, "w",  encoding= "utf-8") as f:
                    f.write(txt_res)
                    f.close()
                messagebox.showinfo(title="Successfully", message="The file was saved successfully!")
                window.destroy()
            
            label_copy3.bind("<Button-1>", TXT_file )
            label_copy3.bind("<Enter>", on_enter)
            label_copy3.bind("<Leave>", on_leave)
            
            frame.pack(side="top")
            frame2 = tk.Frame(window, bg = bg_val)
            label = tk.Label(frame2, bg = bg_val, fg = fg_val)
            label["text"] = txt_res
            if label["text"] == "":
                window.destroy()
                windwo_load.destroy()
                return
            label.pack()
            frame2.pack(side="top")
            windwo_load.destroy()
            window.mainloop()
            
        def recognize_file():
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
                
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
            
            file = filedialog.askopenfile()
            if file == "" or file == None:
                return
            window_language = tk.Toplevel(bg = bg_val)
            window_language.geometry("340x90+840+500")
            window_language.resizable(False, False)
            
            
            
            
            def on_enter(e):
                e.widget['background'] = '#006B9E'                
            def on_leave(e):
                global switch_value
                if switch_value:
                    e.widget['background'] = "SystemButtonFace"
                else:
                    e.widget['background'] = "#26242f"
                
            def on_click_lng(event, arg):
                self.lng = arg
                window_language.destroy()
                window_language.quit()
                
            frame_lng_main = tk.Frame(window_language, bg = bg_val)
            label_ =  tk.Label(frame_lng_main , text= "Select a language:", font = 46, bg = bg_val, fg = fg_val)
            label_.pack()
            frame_lng_main.pack(side="top")
            frame_first_lng = tk.Frame(window_language, bg = bg_val)
            label_en =  tk.Label( frame_first_lng, image= self.img_en,  cursor="hand2", bg = bg_val)
            label_en.pack(side = tk.LEFT, padx=2)
            label_fr =  tk.Label(frame_first_lng ,  image= self.img_fr, cursor="hand2", bg = bg_val)
            label_fr.pack(side = tk.LEFT, padx=2)
            label_ja =  tk.Label(frame_first_lng , image= self.img_ja, cursor="hand2", bg = bg_val)
            label_ja.pack(side = tk.LEFT, padx=2)
            label_ko =  tk.Label(frame_first_lng , image= self.img_ko, cursor="hand2", bg = bg_val)
            label_ko.pack(side = tk.LEFT, padx=2)
            label_ru =  tk.Label(frame_first_lng , image= self.img_ru, cursor="hand2", bg = bg_val)
            label_ru.pack(side = tk.LEFT, padx=2)
            label_zh =  tk.Label(frame_first_lng , image= self.img_zh, cursor="hand2", bg = bg_val)
            label_zh.pack(side = tk.LEFT, padx=2, pady= 3)
            frame_first_lng.pack(side="top")
            
            
            label_en.bind("<Enter>", on_enter)
            label_en.bind("<Leave>", on_leave)        
            label_fr.bind("<Enter>", on_enter)
            label_fr.bind("<Leave>", on_leave)        
            label_ja.bind("<Enter>", on_enter)
            label_ja.bind("<Leave>", on_leave)        
            label_ko.bind("<Enter>", on_enter)
            label_ko.bind("<Leave>", on_leave)        
            label_ru.bind("<Enter>", on_enter)
            label_ru.bind("<Leave>", on_leave)        
            label_zh.bind("<Enter>", on_enter)
            label_zh.bind("<Leave>", on_leave)        
            
            
            
            label_en.bind("<Button-1>",lambda event, arg="en": on_click_lng(event, arg))
            label_fr.bind("<Button-1>", lambda event, arg="fr": on_click_lng(event, arg))
            label_ja.bind("<Button-1>", lambda event, arg="ja": on_click_lng(event, arg))
            label_ko.bind("<Button-1>", lambda event, arg="ko": on_click_lng(event, arg))
            label_ru.bind("<Button-1>", lambda event, arg="ru": on_click_lng(event, arg))
            #label_zh.bind("<Button-1>", lambda event, arg="zho": on_click_lng(event, arg))
            
            window_language.mainloop()
            
            if self.lng == None:
                return
            windwo_load = tk.Tk()
            windwo_load["bg"] = bg_val
            windwo_load.geometry(("500x80+750+500"))
            windwo_load.resizable(False, False)
            
            ##
            self.master.withdraw()
            def action(windwo_load):
                global txt_res
                label_ = tk.Label(windwo_load, bg = bg_val, fg = fg_val,  text = "Wait for the operation to be completed", font = "Arial 10 bold")
                label_.pack()
                label_name_file_load = tk.Label(windwo_load, bg = bg_val, fg = fg_val)
                label_name_file_load.pack()
                Load_frame_app = tk.Frame(windwo_load, bg = bg_val)                                                     
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
                    label_error = tk.Label(windwo_load, bg = bg_val, fg = "red", text = "Something went wrong. Perhaps the quality of the image is not subject to recognition")
                    label_error.pack()
                    time.sleep(3)
                    return
                txt_res+= result
                if result == "":
                    label_error_2 = tk.Label(windwo_load, bg = bg_val, fg = "red", text = "Some files do not contain a text value or are not of good quality.")
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
            
            
            
            
            
            
            
            
            
            
            
            
            window = tk.Toplevel(bg = bg_val)
            frame = tk.Frame(window, bg = bg_val)
            def copy_text_click(event):
                clipboard.copy(txt_res)   
                def label_animation_add():
                    check_mark.destroy()
                    
                check_mark = tk.Label(frame, text = "✓" , fg= "green", font = 38,bg = bg_val)
                check_mark.place(x=1, y = 30)
                check_mark.after(2000, label_animation_add)
            label_copy = tk.Label(frame, image = self.copy, cursor="hand2", bg = bg_val, fg = fg_val)
            label_copy.bind("<Button-1>", copy_text_click )
            label_copy.bind("<Enter>", on_enter)
            label_copy.bind("<Leave>", on_leave)   
            def PDF_file(event):
                messagebox.showinfo(title="Development will be introduced", message="This function is not yet available")
                return
            label_copy2 = tk.Label(frame, image = self.copy2, cursor="hand2", bg = bg_val, fg = fg_val)
            label_copy2.bind("<Button-1>", PDF_file )
            label_copy2.bind("<Enter>", on_enter)
            label_copy2.bind("<Leave>", on_leave)   
            
            
            
            
            def TXT_file(event):
                Files = [('Text Document', '*.txt')]
                file = filedialog.asksaveasfile(filetypes = Files, defaultextension = Files)
                with open(file.name, "w",  encoding= "utf-8") as f:
                    f.write(txt_res)
                    f.close()
                messagebox.showinfo(title="Successfully", message="The file was saved successfully!")
                window.destroy()
            
            label_copy3 = tk.Label(frame, image = self.copy3, cursor="hand2", bg = bg_val, fg = fg_val)

            label_copy3.bind("<Button-1>", TXT_file )
            label_copy3.bind("<Enter>", on_enter)
            label_copy3.bind("<Leave>", on_leave)   
            label_copy.pack(side="left")
            label_copy2.pack(side="left")
            label_copy3.pack(side="left")
            frame.pack(side="top")
            frame2 = tk.Frame(window, bg = bg_val)
            label = tk.Label(frame2, bg = bg_val, fg = fg_val)
            label["text"] = txt_res
            if label["text"] == "":
                window.destroy()
                windwo_load.destroy()
                return
            label.pack()
            frame2.pack(side="top")
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
                global switch_value
                if switch_value:
                    e.widget['background'] = "SystemButtonFace"
                else:
                    e.widget['background'] = "#26242f"
                    
            
            
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
                
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
                
            
            
            def on_click_lng(event, arg):
                self.lng = arg
                window_language.destroy()
                window_language.quit()
                
            window_language = tk.Toplevel(bg = bg_val)
            window_language.geometry("340x90+840+500")
            window_language.resizable(False, False)
            
            
            
            frame_lng_main = tk.Frame(window_language, bg = bg_val)
            label_ =  tk.Label(frame_lng_main , text= "Select a language:", font = 46, bg = bg_val, fg = fg_val)
            label_.pack()
            frame_lng_main.pack(side="top")
            frame_first_lng = tk.Frame(window_language, bg = bg_val)
            label_en =  tk.Label( frame_first_lng, image= self.img_en,  cursor="hand2", bg = bg_val)
            label_en.pack(side = tk.LEFT, padx=2)
            label_fr =  tk.Label(frame_first_lng ,  image= self.img_fr, cursor="hand2", bg = bg_val)
            label_fr.pack(side = tk.LEFT, padx=2)
            label_ja =  tk.Label(frame_first_lng , image= self.img_ja, cursor="hand2", bg = bg_val)
            label_ja.pack(side = tk.LEFT, padx=2)
            label_ko =  tk.Label(frame_first_lng , image= self.img_ko, cursor="hand2", bg = bg_val)
            label_ko.pack(side = tk.LEFT, padx=2)
            label_ru =  tk.Label(frame_first_lng , image= self.img_ru, cursor="hand2", bg = bg_val)
            label_ru.pack(side = tk.LEFT, padx=2)
            label_zh =  tk.Label(frame_first_lng , image= self.img_zh, cursor="hand2", bg = bg_val)
            label_zh.pack(side = tk.LEFT, padx=2, pady= 3)
            frame_first_lng.pack(side="top")
            
            
            label_en.bind("<Enter>", on_enter)
            label_en.bind("<Leave>", on_leave)        
            label_fr.bind("<Enter>", on_enter)
            label_fr.bind("<Leave>", on_leave)        
            label_ja.bind("<Enter>", on_enter)
            label_ja.bind("<Leave>", on_leave)        
            label_ko.bind("<Enter>", on_enter)
            label_ko.bind("<Leave>", on_leave)        
            label_ru.bind("<Enter>", on_enter)
            label_ru.bind("<Leave>", on_leave)        
            label_zh.bind("<Enter>", on_enter)
            label_zh.bind("<Leave>", on_leave)        
            
            
            
            label_en.bind("<Button-1>",lambda event, arg="en": on_click_lng(event, arg))
            label_fr.bind("<Button-1>", lambda event, arg="fr": on_click_lng(event, arg))
            label_ja.bind("<Button-1>", lambda event, arg="ja": on_click_lng(event, arg))
            label_ko.bind("<Button-1>", lambda event, arg="ko": on_click_lng(event, arg))
            label_ru.bind("<Button-1>", lambda event, arg="ru": on_click_lng(event, arg))
            #label_zh.bind("<Button-1>", lambda event, arg="zho": on_click_lng(event, arg))
            
            

            
            
            
            window_language.mainloop()
            if self.lng == None:
                return
            
            
            windwo_load = tk.Tk()
            windwo_load["bg"] = bg_val
            windwo_load.geometry(("500x80+750+500"))
            windwo_load.resizable(False, False)
            self.master.withdraw()
            def action(windwo_load):
                global txt_res
                label_ = tk.Label(windwo_load, bg = bg_val, fg = fg_val, text = "Wait for the operation to be completed", font = "Arial 10 bold")
                label_.pack()
                label_name_file_load = tk.Label(windwo_load, bg = bg_val, fg = fg_val)
                label_name_file_load.pack()
                Load_frame_app = tk.Frame(windwo_load, bg = bg_val)                                                     
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
                        label_error = tk.Label(windwo_load,bg = bg_val, fg = "red", text = "Something went wrong. Perhaps the quality of the image is not subject to recognition")
                        label_error.pack()
                        time.sleep(3)
                        txt_res = []
                        return
                    txt_res.append(result)
                    if result == []:
                        label_error_2 = tk.Label(windwo_load, bg = bg_val, text = "Some files do not contain a text value or are not of good quality.", fg= "red")
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
                window = tk.Toplevel(bg = bg_val)
                frame = tk.Frame(window, bg = bg_val)
                data= {"elem":ready_text , "self": self }
                def copy_text_click(event, arg):
                    clipboard.copy(arg["elem"])   
                    def label_animation_add():
                        check_mark.destroy() 
                    check_mark = tk.Label(frame, text = "✓" , fg= "green", font = 38, bg = bg_val)
                    check_mark.place(x=1, y = 30)
                    check_mark.after(2000,  label_animation_add)
                
                label_copy = tk.Label(frame, image = self.copy, cursor="hand2", bg = bg_val)
                label_copy.pack(side="left")
                
                label_copy.bind("<Button-1>", lambda event, arg=data: copy_text_click(event, arg) )
                
                label_copy.bind("<Enter>", on_enter)
                label_copy.bind("<Leave>", on_leave) 
                
                def PDF_file(event, arg):
                    messagebox.showinfo(title="Development will be introduced", message="This function is not yet available")
                    return
                label_copy2 = tk.Label(frame, image = self.copy2, cursor="hand2", bg = bg_val)
                label_copy2.pack(side="left")
                label_copy2.bind("<Button-1>", lambda event, arg=data: PDF_file(event, arg))
                label_copy2.bind("<Enter>", on_enter)
                label_copy2.bind("<Leave>", on_leave)   
                
                
                
                def TXT_file(event, arg):
                    Files = [('Text Document', '*.txt')]
                    file = filedialog.asksaveasfile(filetypes = Files, defaultextension = Files)
                    with open(file.name, "w",  encoding= "utf-8") as f:
                        f.write(arg["elem"])
                        f.close()
                    messagebox.showinfo(title="Successfully", message="The file was saved successfully!")
                    window.destroy()
            
                label_copy3 = tk.Label(frame, image = self.copy3, cursor="hand2", bg = bg_val, fg = fg_val)
                label_copy3.pack(side="left")
                label_copy3.bind("<Button-1>", lambda event, arg=data: TXT_file(event, arg))
                label_copy3.bind("<Enter>", on_enter)
                label_copy3.bind("<Leave>", on_leave)   
                
                
                
                frame.pack(side="top")
                frame2 = tk.Frame(window, bg = bg_val)
                label = tk.Label(frame2, bg = bg_val, fg = fg_val)
                label["text"] = ready_text
                if label["text"] == "":
                    window.destroy()
                    windwo_load.destroy()
                    return
                label.pack()
                frame2.pack(side="top")
            windwo_load.destroy()
        
        self.Label_get2 = ttk.Button(self.Handler, text = "Recognize separately",  cursor="hand2", command=thread_process_2)
        self.Label_get2.grid(row=2, column=0, columnspan=2, ipadx=56, ipady=4, padx=5, pady=5)
        self.Additional_settings = tk.LabelFrame(self.Frame_Handler,text = "Additional settings",font = "Arial 12 bold ", width= 247, height= 325)                #
        self.Additional_settings.place(x= 1, y= 161)
        self.list_funcs_settings =recognize_file,thred_process, thread_process_2
        self.list_funcs_settings2=None
        
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
        global switch_value
        if switch_value == False:
            bg_val = "#26242f"
            fg_val = "white"
            fg_val2 = "black"
        else:
            bg_val = "SystemButtonFace"
            fg_val = "black"
            fg_val2 = "SystemButtonFace"
        if self.pr_activion:
            
            if self.label_pr_act["text"] == "New Project":
                save_window = tk.Toplevel(bg=bg_val)
                save_window.resizable(False, False)
                save_window.title("Save")
                save_window.geometry("220x90+860+450")
                label_name_write = tk.Label(save_window, text = "Project name",font = "Arial 12 bold", bg= bg_val, fg=fg_val)
                label_name_write.pack(anchor= tk.N, padx= 5)
                def on_enter(e):
                    e.widget['background'] = 'gray'
                def on_leave(e):
                    
                    if switch_value:
                        e.widget['background'] = "SystemButtonFace"
                    else:
                        e.widget['background'] = "#26242f"
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
                    
                    
                Entry = tk.Entry(save_window,width=33, bg= fg_val2, fg=fg_val)
                Entry.pack(anchor= tk.CENTER, padx= 5)
                icon_image = tk.Label(save_window, image=self.bg, bg=bg_val)
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
                
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
                self.Frame_Files.place(x= 1, y= 235)      
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235, bg= bg_val, fg=fg_val) #
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

        global switch_value
        if switch_value == False:
            bg_val = "#26242f"
            fg_val = "white"
        else:
            bg_val = "SystemButtonFace"
            fg_val = "black"
        def selected(event):
            def pr_load(): 
        
                global OBJ
                global switch_value
                if switch_value == False:
                    bg_val = "#26242f"
                    fg_val = "white"
                else:
                    bg_val = "SystemButtonFace"
                    fg_val = "black"
                if OBJ.upload_bool_:
                    self.pr_activion = True

                    selected(event)            
                    pr_load()
                    try:
                        index= list(self.listbox["values"]).index(self.selected_before)
                        self.listbox.current(index)
                    except:
                        self.selected_before = self.listbox.get()
                    self.label_pr_act = tk.Label(self.Frame_Recording, text = self.selected_before,  font= "Arial 14", bg= bg_val, fg=fg_val) #
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
                        self.label_pr_act = tk.Label(self.Frame_Recording,  font= "Arial 14", bg= bg_val, fg=fg_val) #
                        self.label_pr_act.place(x=126, y =37)
                        self.label_pr_act["text"] = self.listbox.get() 
                        self.Frame_Files.destroy()
                        self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
                        self.Frame_Files.place(x= 1, y= 235)      
                        OBJ(self.Frame_Files, self.Frame_Recording, switch_value).load_frame(res_files)
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
        
        
        
        label = tk.Label(self.Frame_Recording, text = "Current Project:", font= "Arial 12", bg= bg_val, fg=fg_val)
        label.place(x = 10, y = 40)
        label = tk.Label(self.Frame_Recording,text = "Select a project: ", font= "Arial 12", bg= bg_val, fg=fg_val)
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
            
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
            
            if self.label_pr_act["text"] == "New Project" and len(OBJ.FILES_LIST) == 1 and OBJ.FILES_LIST[0]==" " :
                messagebox.showinfo(title="Deleting an empty project", message="An empty project is automatically erased after the program is closed.")
                return
            
            if self.label_pr_act["text"] == "New Project" and OBJ.FILES_LIST== []:
                messagebox.showinfo(title="Deleting an empty project", message="An empty project is automatically erased after the program is closed.")
                return
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
                    self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
                    self.Frame_Files.place(x= 1, y= 235)  
                    self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235, bg= bg_val, fg=fg_val) #
                    self.Frame_recording.place(x= 1, y= 1)
                    self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10 bold", bg= bg_val, fg=fg_val)
                    self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
                    
                    self.label_pr_act["text"] = ""
                    self.Recording_Frame()
                    messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                    
                else:
                    return
            
        self.Remove_a_project = ttk.Button(self.Additional_settings, text = "Remove a project",  cursor="hand2", command=Remove_pr)
        self.Remove_a_project.grid(row=0, column=0, columnspan=2, ipadx=65, ipady=4, padx=5, pady=5)
        
        
        def Remove_all_files():
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
            
            if self.label_pr_act["text"] == "New Project" and len(OBJ.FILES_LIST) == 1 and OBJ.FILES_LIST[0]==" ":
                messagebox.showinfo(title="The project is empty", message="There are no files in the current project.")
                return
            if self.label_pr_act["text"] == "New Project" and OBJ.FILES_LIST== [] :
                messagebox.showinfo(title="Deleting an empty project", message="An empty project is automatically erased after the program is closed.")
                return
            
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
                    for file in files:
                        os.remove(file)
                    self.Frame_Files.destroy()
                    
                    self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
                    self.Frame_Files.place(x= 1, y= 235)  
                    self.pr_activion = False
                    OBJ.upload_bool_ = False
                    OBJ(self.Frame_Files, self.Frame_Recording, switch_value).add_frame()
                    OBJ(self.Frame_Files, self.Frame_Recording, switch_value).load_frame("")
                    self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10", bg= bg_val, fg=fg_val)
                    self.label_info_fr_file.pack()
                    OBJ.FILES_LIST = []
                    messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                    
                else:
                    return
        
        self.Remove_all_files = ttk.Button(self.Additional_settings, text = "Remove all files",  cursor="hand2", command= Remove_all_files)
        self.Remove_all_files.grid(row=1, column=0, columnspan=2, ipadx=70, ipady=4, padx=5, pady=5)
        
        
        def Remove_all_pr():
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
            answer = messagebox.askyesno(title="Remove process", message= "Are you sure you want to remove all projects?")
            if answer: 
                if self.label_pr_act["text"] == "New Project":
                    messagebox.showwarning(title="Session error", message= "Please delete or save the current project to continue the operation.")
                    return
                for file_pr in self.urls_project_files():
                    shutil.rmtree(self.local_url +f"/projects/{file_pr}")
                self.Frame_Files.destroy()
                self.Frame_recording.destroy()
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
                self.Frame_Files.place(x= 1, y= 235)  
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235, bg= bg_val, fg=fg_val) #
                self.Frame_recording.place(x= 1, y= 1)
                self.Recording_Frame()
                self.label_pr_act["text"] = ""
                self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Please upload or select a project", font = "Arial 10 bold", bg= bg_val, fg=fg_val)
                self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
                messagebox.showinfo(title="Successfully!", message= "The project has been deleted.")
                
            else:
                return
            
        
        self.Remove_all_projects = ttk.Button(self.Additional_settings, text = "Remove all projects",  cursor="hand2", command=Remove_all_pr)
        self.Remove_all_projects.grid(row=2, column=0, columnspan=2, ipadx=59, ipady=4, padx=5, pady=5)
        
        
        def upload_project():
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
                
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
            self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
            self.Frame_Files.place(x= 1, y= 235)  
            for sym in falder[::-1]:
                index +=1
                if sym == "/": 
                    
                    self.Frame_recording.destroy()
                    self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235, bg= bg_val, fg=fg_val) #
                    self.Frame_recording.place(x= 1, y= 1)
                    
                    self.label_pr_act = tk.Label(self.Frame_Recording, text= falder[-index+1::],  font= "Arial 14", bg= bg_val, fg=fg_val) #
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
            OBJ(self.Frame_Files, self.Frame_Recording, switch_value).upload_frame(files, name_pr)         
            
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
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
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
                
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235, bg= bg_val, fg=fg_val) #
                self.Frame_recording.place(x= 1, y= 1)
                
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250,  bg= bg_val, fg=fg_val)                #
                self.Frame_Files.place(x= 1, y= 235)      
                
                self.label_info_fr_file = tk.Label(self.Frame_Files, text = "Upload images to the project", font = "Arial 10 bold ",  bg= bg_val, fg=fg_val)
                self.label_info_fr_file.place(relx=.5, rely=.5, anchor="c")
                
                OBJ(self.Frame_Files, self.Frame_Recording, switch_value).add_frame()
                self.label_pr_act = tk.Label(self.Frame_Recording, text = "New Project", font= "Arial 14", bg= bg_val, fg=fg_val) #
                
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
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
                
            if self.label_pr_act["text"] == "" or self.label_pr_act["text"] == " ":
                messagebox.showinfo(title="Project not found", message="Select or upload the project to continue.")
            else:
                self.Frame_Files.destroy()
                self.Frame_Files = tk.LabelFrame(self.Frame_Recording ,text = "Files",font = "Arial 12 bold ", width= 320, height= 250, bg= bg_val, fg=fg_val)                #
                self.Frame_Files.place(x= 1, y= 235)  
                OBJ(self.Frame_Files, self.Frame_Recording, switch_value).add_file(self.label_pr_act["text"])
        self.Add_a_file = ttk.Button(self.Additional_settings, text = "Add a file", cursor="hand2", command= add_file)
        self.Add_a_file.grid(row=5, column=0, columnspan=2, ipadx=77, ipady=4, padx=5, pady=5)
        def save(): 
            global switch_value
            if switch_value == False:
                bg_val = "#26242f"
                fg_val = "white"
            else:
                bg_val = "SystemButtonFace"
                fg_val = "black"
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
                self.Frame_recording = tk.LabelFrame(self.Frame_Recording ,text = "Editing projects",font = "Arial 12 bold ", width= 320, height= 235, bg= bg_val, fg=fg_val) #
                self.Frame_recording.place(x= 1, y= 1)
                self.new_pr_bool = False
                self.pr_activion = False
                self.blocker_new_pr = None
                OBJ.upload_bool_ = False
                self.Recording_Frame()
                self.label_pr_act = tk.Label(self.Frame_Recording,  font= "Arial 14", bg= bg_val, fg=fg_val) #
                self.label_pr_act.place(x=126, y =37)
                self.label_pr_act["text"] = self.save_text_new_pr
                self.listbox.current(index)
                self.save_text_new_pr = None
                self.selected_before = self.save_text_new_pr
                def label_animation_add():
                    canvas.destroy()
                    
                width= 210
                height=30
                canvas =  tk.Canvas(self.Frame_Instruction, bg = "#ccffcc", highlightbackground = "#ADFFAD" , height= height, width= width)
                canvas.create_text(width/2, height/2, fill="black", text = f"Your project has been saved!", font= "@yugothic 9")
                canvas.place(relx=0.10, rely=0.88)
                canvas.after(2000, label_animation_add)
                
            else:
                messagebox.showinfo(title= "Repeated operation", message= "Saved projects are automatically saved.")
        self.exit = ttk.Button(self.Additional_settings, text = "Save",  cursor="hand2", command= save)
        self.exit.grid(row=7, column=0, columnspan=2, ipadx=77, ipady=4, padx=5, pady=5)
        self.list_funcs_settings2 = Remove_pr, Remove_all_files ,Remove_all_pr, upload_project, add_new_pr, add_file, save
        
        
        
        def check_appearance():
            """Checks DARK/LIGHT mode of macos."""
            cmd = 'defaults read -g AppleInterfaceStyle'
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
            return bool(p.communicate()[0])
        res_OC_BG= check_appearance()
        if res_OC_BG:
            self.switch.invoke()    
        
        
def main():
    window =  tk.Tk()
    window.resizable(False, False)
    
    
    #mainmenu.add_cascade(label="Файл", menu=filemenu)
    
        
    
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
                    app.save_pr_and_file() 
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
    window.geometry(f"845x510+550+300")
    
    #window.wm_attributes('-transparentcolor','red')
    window.mainloop()
    
if __name__ == "__main__":
    main()