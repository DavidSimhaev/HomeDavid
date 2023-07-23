import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        b = tk.Button(self, text="Click to fade away", command=self.quit)
        b.pack()
        self.parent = parent
        

    def quit(self):
        self.fade_away()

    def fade_away(self):
        alpha = self.parent.attributes("-alpha")
        if alpha > 0:
            alpha -= .1
            self.parent.attributes("-alpha", alpha)
            self.after(100, self.fade_away)
        else:
            self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    g = tk.Label
    Example(root).pack(fill="both", expand=True)
    root.mainloop()