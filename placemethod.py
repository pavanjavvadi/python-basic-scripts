from tkinter import *
parent = Tk()
parent.geometry("400x250")
name = Label(parent,text = "Name")
name.place(x=150,y=100)
entryname = Entry(parent)
entryname.place(x=200,y=100)
password = Label(parent,text = "Password")
password.place(x=150,y=125)
entrypassword = Entry(parent)
entrypassword.place(x=200,y=125)
parent.mainloop()