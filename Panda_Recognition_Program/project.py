import tkinter as tk
from tkinter import messagebox
from Frame_Recording import Recording
from Frame_Files import Files
import os
import shutil
class Example(tk.Frame):
    local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    def __init__(self):
        super().__init__()
        
        self.img_panda = tk.PhotoImage(file = rf"{self.local_url}/image/panda.png" ).subsample(3,3)
        self.img_logo = tk.PhotoImage(file = rf"{self.local_url}/image/logo.png" )
        self.icon_menu = None
        self.icon_files = None

        self.app()
    
    def app(self):
        
        
        self.master.title("Panda Recognize Progam")
        Frame_app = tk.Frame()
        Frame_app.pack(side = tk.TOP)
        
        Frame_Instruction = tk.Frame(Frame_app, width=250, height=460, bg='#E0B0FF')
        Frame_Instruction.pack(side = tk.LEFT)
        
        
        
        
        ##################################  ИНСТРУКЦИЯ    ###################################################
        
        
        #Canvas_fr = tk.Canvas(Frame_Instruction)
        
        label_img_panda = tk.Label(Frame_Instruction ,image= self.img_panda , bg= "#E0B0FF")
        label_img_panda.place(x=40, y =18)
        label_logo = tk.Label(Frame_Instruction ,image= self.img_logo, bg= "#E0B0FF")
        label_logo.place(x=1, y =192)
        
        
        #############################
        

        
        
        Frame_Recording = tk.Frame(Frame_app, width=342, height=460, bg="#E0B0FF")##E0B0FF
        Frame_Recording.pack(side = tk.LEFT)
        
        
        
        
        
        ##################################  РЕДАКТИРОВАНИЕ    ###################################################
        
        
        Frame_recording = tk.LabelFrame(Frame_Recording ,text = "Editing projects", fg="#990066",font = "Arial 12 bold ", width= 340, height= 210, bg= "#E0B0FF")
        Frame_recording.place(x= 1, y= 1)
        
        Frame_Files = tk.LabelFrame(Frame_Recording ,text = "Files", fg="#990066",font = "Arial 12 bold ", width= 340, height= 235, bg= "#E0B0FF")
        Frame_Files.place(x= 1, y= 210)
        
        
        def update():
            Recording(Frame_recording, Frame_Files ).list_box_pr()
            self.master.after(1000, update)

        self.master.after(1000, update)


        Frame_Handler = tk.Frame(Frame_app, width=250, height=460, bg='red')##E0B0FF
        Frame_Handler.pack(side = tk.LEFT)
        
        
        
        
        
        
        ##################################  ОБРАБОТЧИК    ###################################################
        

        Load_frame_app = tk.Frame(bg = "#E0B0FF")
        Load_frame_app.pack(side= tk.TOP)
        label_Load = tk.Label(Load_frame_app, width=120, height=1,  text="ЗАГРУЗКА")
        label_Load.pack()
        
        
        
        
        
        
        
    

def main():
    window =  tk.Tk()
    app = Example()
    window.geometry("845x480")
    
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
    window["bg"] = "#E0B0FF"
    window.mainloop()
    
if __name__ == "__main__":
    main()