from tkinter import *
parent = Tk()
redbutton = Button(parent,text = "red",fg = "white",bg="red")
redbutton.pack(side=LEFT)
blackbutton = Button(parent,text = "black",fg = "black", bg="white")
blackbutton.pack(side = RIGHT)
bluebutton = Button(parent,text ="blue",fg = "blue" ,bg = "gray")
bluebutton.pack(side = TOP)
greenbutton = Button(parent,text = "green",fg = "green", bg = "yellow")
greenbutton.pack(side = BOTTOM)
parent.mainloop()