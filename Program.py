from tkinter import *
import tkinter.font as font
from tkinter.ttk import *



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

        self.pw_ent1 = Entry(self)
        self.pw_ent1.grid(row =1, column = 1, sticky = W)

        self.pw_lbl = Label(self, text = "Password")
        self.pw_lbl.grid(row =2, column = 0, sticky = W)

        self.pw_ent2 = Entry(self)
        self.pw_ent2.grid(row =2, column = 1, sticky = W)


        self.submit_bttn1 = Button(self, text="Submit", command = self.reveal)
        self.submit_bttn1.grid(row=3, column=0, columnspan=2, pady=10)

        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row=6, column=0, columnspan =2, sticky =W)

    def reveal(self):
        User1 = self.pw_ent1.get()
        Password1 = self.pw_ent2.get()
        if User1 == "Hoa-Wah" and Password1 == "m@ng0":
            message = "Login complete"
        else:
            message= "Login failed"  

        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)
        






# region Root
root = Tk()
root.title("ChineseOrder Sys")
root.geometry("1400x800")

app = Application(master=root)
app.pack()
# endregion Root




root.mainloop()

