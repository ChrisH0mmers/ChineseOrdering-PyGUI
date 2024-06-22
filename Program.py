from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):

        self.inst_lbl = Label(self, text="Log-In Required")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.pw_lbl = Label(self, text = "Username")
        self.pw_lbl.grid(row =1, column = 0, sticky = W)

        self.pw_lbl = Label(self, text = "Password")
        self.pw_lbl.grid(row =2, column = 0, sticky = W)


        self.inst_bttn1 = Button(self, text="Start System")
        self.inst_bttn1.grid(row=3, column=0, columnspan=2, pady=10)





root = Tk()
root.title("ChineseOrder Sys")
root.geometry("1400x800")

app = Application(master=root)
app.pack()

root.mainloop()

