from tkinter import *
import tkinter.font as font




class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):

        bold_font = font.Font(weight="bold")

        self.inst_lbl = Label(self, text="Log-In Required", font=bold_font)
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.pw_lbl = Label(self, text = "Username")
        self.pw_lbl.grid(row =1, column = 0, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row =1, column = 1, sticky = W)

        self.pw_lbl = Label(self, text = "Password")
        self.pw_lbl.grid(row =2, column = 0, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row =2, column = 1, sticky = W)


        self.submit_bttn1 = Button(self, text="Submit", command = self.reveal)
        self.submit_bttn1.grid(row=3, column=0, columnspan=2, pady=10)
    def reveal(self):
        contents= self.pw_ent.get()

# region Root
root = Tk()
root.title("ChineseOrder Sys")
root.geometry("1400x800")

app = Application(master=root)
app.pack()
# endregion Root



root.mainloop()

