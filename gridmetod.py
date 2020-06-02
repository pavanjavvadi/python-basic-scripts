from tkinter import *
parent = Tk()
name = Label(parent,text = "Name")
name.grid(row = 0,column = 0)
input1 = Entry(parent)
input1.grid(row = 0,column = 1)
password = Label(parent,text = "Password")
password.grid(row = 1, column = 0)
passinput = Entry(parent)
passinput.grid(row=1,column = 1)
submit = Button(parent,text = "submit",fg ="black",bg = "gray").grid(row = 4,column =1)

parent.mainloop()
