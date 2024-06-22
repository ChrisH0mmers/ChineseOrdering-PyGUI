from tkinter import *
import tkinter.font as font

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        bold_font = font.Font(weight="bold")

        self.inst_lbl = Label(self, text="Log-In Required", font=bold_font)
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        self.user_lbl = Label(self, text="Username")
        self.user_lbl.grid(row=1, column=0, sticky=W)

        self.user_ent = Entry(self)
        self.user_ent.grid(row=1, column=1, sticky=W)

        self.pw_lbl = Label(self, text="Password")
        self.pw_lbl.grid(row=2, column=0, sticky=W)

        self.pw_ent = Entry(self, show='*')
        self.pw_ent.grid(row=2, column=1, sticky=W)

        self.submit_bttn = Button(self, text="Submit", command=self.reveal)
        self.submit_bttn.grid(row=3, column=0, columnspan=2, pady=10)

        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=4, column=0, columnspan=2, sticky=W)

    def reveal(self):
        username = self.user_ent.get()
        password = self.pw_ent.get()
        if username == "Ho-Wah" and password == "m@ng0":
            message = "Login complete"
            self.show_menu()
        else:
            message = "Login failed"
            self.pw_ent.delete(0, END)  

        self.secret_txt.delete(1.0, END)
        self.secret_txt.insert(1.0, message)

    def show_menu(self):
        self.inst_lbl.grid_remove()
        self.user_lbl.grid_remove()
        self.user_ent.grid_remove()
        self.pw_lbl.grid_remove()
        self.pw_ent.grid_remove()
        self.submit_bttn.grid_remove()
        self.secret_txt.grid_remove()

        bold_font = font.Font(weight="bold")
        menu_lbl = Label(self, text="Choose amount with numbers", font=bold_font)
        menu_lbl.grid(row=0, column=0, sticky=W)

        self.cr1_lbl = Label(self, text="Chinese-Rijsttafel 1 persoon")
        self.cr1_lbl.grid(row=1, column=0, sticky=W)

        self.cr1_ent1 = Entry(self)
        self.cr1_ent1.grid(row=1, column=1, sticky=W) 

        self.cr2_lbl = Label(self, text="Chinese-Rijsttafel 2 personen")
        self.cr2_lbl.grid(row=2, column=0, sticky=W)

        self.cr2_ent1 = Entry(self)
        self.cr2_ent1.grid(row=2, column=1, sticky=W)

        self.submit_menu_bttn = Button(self, text="Submit", command=self.process_menu)
        self.submit_menu_bttn.grid(row=3, column=0, columnspan=2, pady=10)

        self.menu_result_txt = Text(self, width=35, height=5, wrap=WORD)
        self.menu_result_txt.grid(row=4, column=0, columnspan=2, sticky=W)

    def process_menu(self):
        amount1 = self.cr1_ent1.get()
        amount2 = self.cr2_ent1.get()


        total_amount = 0
        if amount1.isdigit():
            total_amount += int(amount1)
        if amount2.isdigit():
            total_amount += int(amount2)

        result_message = f"There are {total_amount} things ordered"
        self.menu_result_txt.delete(1.0, END)
        self.menu_result_txt.insert(1.0, result_message)

# region Root
root = Tk()
root.title("ChineseOrder Sys")
root.geometry("800x600")

app = Application(master=root)
app.pack()
# endregion Root

root.mainloop()
