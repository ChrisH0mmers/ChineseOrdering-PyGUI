from tkinter import *

root = Tk()
root.title("ChineseOrder Sys")
root.geometry("1400x800")


app=Frame(root)
app.pack()
app.grid



lbl = Label(app, text = "Chinese System")
lbl.grid()

bttn1 = Button(app, text = "Start System")
bttn1.grid()



root.mainloop()
